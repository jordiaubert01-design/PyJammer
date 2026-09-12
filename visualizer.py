import pygame
import threading
import queue
import random
import time

class PyJammerVisualizer:
    DRUM_COLORS = {
        'K': (255, 50, 50),     'B': (255, 50, 50),
        'S': (50, 255, 100),    'H': (230, 230, 50),
        'C': (200, 50, 255),    'O': (50, 200, 255),
        'Y': (255, 255, 255)
    }

    CHORD_COLORS = {
        'C': (40, 20, 70),       'D': (20, 50, 80),
        'E': (70, 20, 30),       'F': (20, 70, 40),
        'G': (80, 60, 20),       'A': (70, 30, 70),
        'B': (30, 70, 70),       'DEFAULT': (20, 20, 30)
    }

    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.event_queue = queue.Queue()
        self.running = False
        self.thread = None
        self.particles = []
        
        self.target_bg_color = list(self.CHORD_COLORS['DEFAULT'])
        self.current_bg_color = list(self.CHORD_COLORS['DEFAULT'])

        # Llista per emmagatzemar les línies del prompter
        # Cada element serà un diccionari: {'text': str, 'y': float, 'target_y': float}
        self.prompter_lines = []

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)

    def trigger_drum(self, drum_chars):
        if self.running and drum_chars:
            self.event_queue.put(('drum', drum_chars))

    def trigger_chord(self, chord_name):
        if self.running and chord_name:
            root_note = chord_name[0].upper() if chord_name else 'DEFAULT'
            target_color = self.CHORD_COLORS.get(root_note, self.CHORD_COLORS['DEFAULT'])
            self.event_queue.put(('chord', target_color))

    def trigger_text(self, text):
        """Envia text informatiu o d'acords per afegir al prompter."""
        if self.running and text:
            self.event_queue.put(('text', text))

    def _spawn_waterfall_particle(self, char):
        color = self.DRUM_COLORS.get(char, (200, 200, 200))
        x_positions = {'K': 0.2, 'B': 0.2, 'S': 0.4, 'H': 0.6, 'C': 0.7, 'O': 0.8, 'Y': 0.9}
        pos_ratio = x_positions.get(char, random.uniform(0.1, 0.9))
        
        x_pos = int(self.width * pos_ratio) + random.randint(-20, 20)
        
        particle = {
            'x': x_pos, 'y': 0,
            'vx': random.uniform(-0.5, 0.5), 'vy': random.uniform(4, 9),
            'radius': random.randint(12, 22), 'color': color
        }
        self.particles.append(particle)

    def _add_prompter_line(self, new_text):
        """Afegeix una nova línia a la part inferior i empeny les anteriors cap amunt."""
        line_height = 40
        start_y = self.height - 50

        # Si l'última línia és idèntica, no la tornem a afegir
        if self.prompter_lines and self.prompter_lines[-1]['text'] == new_text:
            return

        # Desplacem totes les línies existents cap amunt
        for line in self.prompter_lines:
            line['target_y'] -= line_height

        # Afegim la nova línia a la part inferior
        self.prompter_lines.append({
            'text': new_text,
            'y': start_y + 20, # Comença lleugerament més avall per fer efecte d'entrada
            'target_y': start_y
        })

        # Limitem a un màxim de 5 línies en pantalla
        if len(self.prompter_lines) > 5:
            self.prompter_lines.pop(0)

    def _update_bg_color(self):
        speed = 0.03
        for i in range(3):
            self.current_bg_color[i] += (self.target_bg_color[i] - self.current_bg_color[i]) * speed

    def _run(self):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("PyJammer Light Cascade & Prompter - Press ESC to exit")
        clock = pygame.time.Clock()

        # Font per al prompter
        font = pygame.font.SysFont("Courier New", 28, bold=True)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # Processar la cua d'esdeveniments
            while not self.event_queue.empty():
                event_type, data = self.event_queue.get()
                if event_type == 'drum':
                    for char in data:
                        self._spawn_waterfall_particle(char)
                elif event_type == 'chord':
                    self.target_bg_color = list(data)
                elif event_type == 'text':
                    self._add_prompter_line(data)

            self._update_bg_color()

            # Dibuixar fons
            fade_surface = pygame.Surface((self.width, self.height))
            fade_surface.set_alpha(35)
            fade_surface.fill([int(c) for c in self.current_bg_color])
            screen.blit(fade_surface, (0, 0))

            # Dibuixar partícules de la cascada
            for p in self.particles[:]:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['radius'] = max(1, p['radius'] - 0.15)

                glow_surface = pygame.Surface((p['radius'] * 4, p['radius'] * 4), pygame.SRCALPHA)
                glow_color = (*p['color'], 50)
                pygame.draw.circle(glow_surface, glow_color, (int(p['radius'] * 2), int(p['radius'] * 2)), int(p['radius'] * 2))
                screen.blit(glow_surface, (int(p['x'] - p['radius'] * 2), int(p['y'] - p['radius'] * 2)))

                pygame.draw.circle(screen, p['color'], (int(p['x']), int(p['y'])), int(p['radius']))

                if p['y'] > self.height or p['radius'] <= 1:
                    self.particles.remove(p)

            # --- DIBUIXAR EL PROMPTER AMB TRANSICIÓ ACCENTUADA A NEGRE ---
            for line in self.prompter_lines:
                # Transició d'animació suau cap a target_y
                line['y'] += (line['target_y'] - line['y']) * 0.2

                # 1. Mapeig base de la posició Y (1.0 a baix, 0.0 a dalt)
                y_ratio = line['y'] / self.height
                linear_factor = max(0.0, min(1.0, (y_ratio - 0.25) * 1.6))

                # 2. ACCENTUACIÓ EXPONENCIAL: Elevador al quadrat/cub per enfosquir fortament
                # Això fa que el color caigui a negre molt més ràpidament en pujar
                dark_factor = linear_factor ** 2.8

                # 3. Interpolem des de negre gairebé pur (15) fins a blanc intens (255)
                text_val = int(15 + (255 - 15) * dark_factor)
                text_color = (text_val, text_val, text_val)

                # 4. Ombra que desapareix immediatament en perdre brillantor
                shadow_val = int(50 * dark_factor)
                shadow_color = (shadow_val, shadow_val, shadow_val)

                # Renderització directa
                raw_shadow = font.render(line['text'], True, shadow_color)
                raw_text = font.render(line['text'], True, text_color)

                rect = raw_text.get_rect(center=(self.width // 2, int(line['y'])))
                
                screen.blit(raw_shadow, (rect.x + 2, rect.y + 2))
                screen.blit(raw_text, rect)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
