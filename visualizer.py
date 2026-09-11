import pygame
import threading
import queue
import random
import time

class PyJammerVisualizer:
    # Colors RGB per a cada instrument de bateria
    DRUM_COLORS = {
        'K': (255, 50, 50),     # Bombo: Vermell potents
        'B': (255, 50, 50),
        'S': (50, 255, 100),    # Caixes: Verd brillant
        'H': (230, 230, 50),    # Hi-hat: Groc
        'C': (200, 50, 255),    # Aplaudiment: Lila
        'O': (50, 200, 255),    # Cencerro: Blau cel
        'Y': (255, 255, 255)    # Plats: Blanc pur
    }

    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.event_queue = queue.Queue()
        self.running = False
        self.thread = None
        self.particles = []

    def start(self):
        """Activa la finestra visualitzadora en un fil independent."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()

    def stop(self):
        """Desactiva la finestra visualitzadora."""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)

    def trigger_drum(self, drum_chars):
        """Envia els caràcters de la bateria que estan sonant actualment."""
        if self.running and drum_chars:
            self.event_queue.put(drum_chars)

    def _spawn_waterfall_particle(self, char):
        """Crea partícules que cauen en cascada segons el tipus de copa o cop de bateria."""
        color = self.DRUM_COLORS.get(char, (200, 200, 200))
        
        # Mapejar posició X segons el tipus de percussió
        x_positions = {'K': 0.2, 'B': 0.2, 'S': 0.4, 'H': 0.6, 'C': 0.7, 'O': 0.8, 'Y': 0.9}
        pos_ratio = x_positions.get(char, random.uniform(0.1, 0.9))
        
        x_pos = int(self.width * pos_ratio) + random.randint(-20, 20)
        
        # Partícula principal (Cascada)
        particle = {
            'x': x_pos,
            'y': 0,
            'vx': random.uniform(-0.5, 0.5),
            'vy': random.uniform(4, 9),      # Velocitat de caiguda
            'radius': random.randint(12, 22),
            'color': color,
            'alpha': 255
        }
        self.particles.append(particle)

    def _run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("PyJammer Light Cascade")
        clock = pygame.time.Clock()

        # Superfície amb canal alfa per a efecte de deixant/brillantor
        fade_surface = pygame.Surface((self.width, self.height))
        fade_surface.set_alpha(60) 
        fade_surface.fill((10, 10, 15))

        while self.running:
            # Gestionar tancament de la finestra Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Processar esdeveniments de la cua (ritme de la música)
            while not self.event_queue.empty():
                drum_chars = self.event_queue.get()
                for char in drum_chars:
                    self._spawn_waterfall_particle(char)

            # Redibuixar fons amb rastre nocturn
            screen.blit(fade_surface, (0, 0))

            # Actualitzar i dibuixar partícules
            for p in self.particles[:]:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['radius'] = max(1, p['radius'] - 0.15) # Es fan petites mentre cauen

                # Dibuixar resplendor/llum exterior
                glow_surface = pygame.Surface((p['radius'] * 4, p['radius'] * 4), pygame.SRCALPHA)
                glow_color = (*p['color'], 50)
                pygame.draw.circle(glow_surface, glow_color, (int(p['radius'] * 2), int(p['radius'] * 2)), int(p['radius'] * 2))
                screen.blit(glow_surface, (int(p['x'] - p['radius'] * 2), int(p['y'] - p['radius'] * 2)))

                # Núcleo brillant de la partícula
                pygame.draw.circle(screen, p['color'], (int(p['x']), int(p['y'])), int(p['radius']))

                # Eliminar si surten de la pantalla o desapareixen
                if p['y'] > self.height or p['radius'] <= 1:
                    self.particles.remove(p)

            pygame.display.flip()
            clock.tick(60) # 60 FPS fons fluid

        pygame.quit()
        