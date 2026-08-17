import time
import keyboard
import PyJammer as pj

# Extract available patterns from PyJammer
AVAILABLE_PATTERNS = list(pj.PyJammer.DRUM_PATTERNS.keys())
AVAILABLE_BASS = list(pj.PyJammer.BASS_MAJOR.keys())

class InteractiveJammer:
    def __init__(self):
        self.jammer = pj.PyJammer()
        self.current_bpm = 105
        self.pattern_idx = 0
        self.bass_idx = 0
        self.running = True
        self.chord = ""
        self.minor = False

        self.jammer.set_bpm(self.current_bpm)
        self.setup_key_listeners()

    def setup_key_listeners(self):
        """Bind keyboard events to control parameters."""
        # BPM controls (+ / -)
        keyboard.add_hotkey('+', self.increase_bpm)
        keyboard.add_hotkey('-', self.decrease_bpm)
        
        # Pattern controls (Up / Down arrows)
        keyboard.add_hotkey('up', self.next_pattern)
        keyboard.add_hotkey('down', self.prev_pattern)

        # Bass style controls (Right / Left arrows)
        keyboard.add_hotkey('right', self.next_bass)
        keyboard.add_hotkey('left', self.prev_bass)

        # Chord controls (A..F, Space, M)
        keyboard.add_hotkey('A', self.play_chord, args=('A',))
        keyboard.add_hotkey('b', self.play_chord, args=('B',))
        keyboard.add_hotkey('c', self.play_chord, args=('C',))
        keyboard.add_hotkey('d', self.play_chord, args=('D',))
        keyboard.add_hotkey('e', self.play_chord, args=('E',))
        keyboard.add_hotkey('f', self.play_chord, args=('F',))
        keyboard.add_hotkey('g', self.play_chord, args=('G',))
        keyboard.add_hotkey(' ', self.play_chord, args=(' ',))
        keyboard.add_hotkey('m', self.play_chord, args=('m',))

        # Exit script (Esc)
        keyboard.add_hotkey('esc', self.stop)

    def increase_bpm(self):
        self.current_bpm = min(240, self.current_bpm + 5)
        self.jammer.set_bpm(self.current_bpm)
        self.print_status()

    def decrease_bpm(self):
        self.current_bpm = max(40, self.current_bpm - 5)
        self.jammer.set_bpm(self.current_bpm)
        self.print_status()

    def next_pattern(self):
        self.pattern_idx = (self.pattern_idx + 1) % len(AVAILABLE_PATTERNS)
        self.print_status()

    def prev_pattern(self):
        self.pattern_idx = (self.pattern_idx - 1) % len(AVAILABLE_PATTERNS)
        self.print_status()

    def next_bass(self):
        self.bass_idx = (self.bass_idx + 1) % len(AVAILABLE_BASS)
        self.print_status()

    def prev_bass(self):
        self.bass_idx = (self.bass_idx - 1) % len(AVAILABLE_BASS)
        self.print_status()

    def stop(self):
        self.running = False

    def play_chord(self, args):
        ch = args[0]
        if ch=='m':
            self.minor = not self.minor
            #print(f"Minor chord selected. self.minor = {self.minor}")

        else:
            # Placeholder for chord functionality
            #print(f"Chord {ch} selected.")
            self.chord = ch
        self.print_status()

    def print_status(self):
        if self.minor:
            chord = f"{self.chord}m"
        else:
            chord = self.chord        
        current_pattern = AVAILABLE_PATTERNS[self.pattern_idx]
        current_bass = AVAILABLE_BASS[self.bass_idx]
        status_text = f"\nchord: {chord} | BPM: {self.current_bpm} | Drum: {current_pattern} | Bass: {current_bass}"
        print(status_text)

    def start_session(self):
        print("\n=== INTERACTIVE JAMMER CONTROLS ===")
        print("  [+] / [-]  : Change BPM")
        print("  [UP] / [DOWN] : Change Drum Pattern")
        print("  [LEFT] / [RIGHT] : Change Bass Style")
        print("  [A] / [B] : Change Chord")
        print("  [M]        : Toggle Minor Chord")
        print("  [ESC]      : Quit\n")

        try:
            self.print_status()
            while self.running:
                current_pattern = AVAILABLE_PATTERNS[self.pattern_idx]
                current_bass = AVAILABLE_BASS[self.bass_idx]
                
                if self.minor:
                    chord = f"{self.chord}m"
                else:
                    chord = self.chord

                #self.print_status()

                # Play 1 repetition per loop pass to check for updated settings
                self.jammer.play_progression(
                    chord,
                    pattern=current_pattern,
                    bass_line=current_bass,
                    instrument='piano',
                    repetitions=1
                )

        except KeyboardInterrupt:
            pass
        finally:
            print("\nShutting down PyJammer...")
            self.jammer.close()

if __name__ == "__main__":
    # Define your chord progression
    
    player = InteractiveJammer()
    player.start_session()
