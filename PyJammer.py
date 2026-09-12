#--------------------------------------------------------
# PyJammer:
# A simple chord progression in python
# Play drums, bass, lead instrument like piano, etc
#
# Author: Jordi Aubert, 2026
#--------------------------------------------------------

import pygame.midi
import time
import re
from visualizer import PyJammerVisualizer

class PyJammer:
    NOTE_MAP = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
        'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
        'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
    }
    
    INSTRUMENTS = {
        'piano': 1,
        'guitar': 25,
        'electric_guitar': 27,
        'bass': 33,      # Electric Bass (fingered)
        'synth_pad': 89,
        'strings': 45,
        'choir': 53,
        'organ': 16,
        'church_organ': 20
    }

    # Map characters to MIDI notes
    DRUM_MAP = {
        'K': 36, # Kick
        'S': 38, # Snare
        'H': 42, # Hi-hat
        'B': 36, # Bass drum
        'C': 39, # Hand clap
        'O': 56, # Cow bell
        'Y': 49  # Cymbal
    }
    
# DRUM PATTERNS (Length determines the step count of the measure)
    DRUM_PATTERNS = {
        'standard': ["KH",  "",   "SH",  "",   "KH",  "",   "SH",  ""],
        'rock':     ["KH",  "H",  "SH",  "H",   "H",  "KH",  "SH",  "H"],
        'ballad':   ["BH", "H", "H", "SH", "H", "BH", "BH", "H", "H", "SH", "H", "H"], # 12/8 ballad
        'hihat':    ["H",   "",   "H",   "",   "H",   "",   "H",   ""],
        'bass':     ["B",   "",   "B",   "",   "B",   "",   "B",   ""],
        'clap':     ["",    "",   "C",   "",   "",    "",   "C",   ""],
        'bell':     ["O",   "",   "O",   "",   "O",   "",   "O",   ""],
        'snare':    ["",    "",   "S",   "",   "",    "",   "S",   ""],
        'swing':    ["KH",  "",   "",    "H",  "SH",  "",   "",    "H"],
        'disco':    ["K",   "",   "SH",  "",   "K",   "",   "SH",  ""],
        'rumba':    ["B",   "",   "C",   "C",  "",    "",   "C",   ""],
        'waltz':    ["K",   "",   "SH",  "",   "SH",  ""], # 3/4 Waltz (6 Eighth-note steps)
        'blues12':  ["KH", "H", "H", "SH", "H", "H", "KH", "H", "H", "SH", "H", "H"], # 12/8 Blues / Slow Rock (12 Eighth-note steps)
        'none':     ["",    "",   "",    "",   "",    "",   "",    ""]
    }

    # BASS PATTERNS
    BASS_MAJOR = {
        'simple' : [0, None, 0, None, 0, None, 0, None],
        'double' : [0, 0 , 0, 0, 0, 0, 0, 0],
        'half'   : [0, None, None, None, 0, 0, None, None],
        'blues'  : [0, None, 4, None, 5, None, 7, None], 
        'blues2' : [0, None, 4, None, 7, None, 9, None], 
        'pop'    : [0, None, 0, None, 7, None, 0, None], 
        'ballad' : [0, None, None, None, 0, None, 7, None],
        'country': [0, None, None, None, 7, None, None, None],
        # 3/4 Waltz Bass (6 steps)
        'blues12': [-12, None, None, None, None, -12, -12, None, None, None, None, None],
        'waltz':   [0, None, None, None, 7, None],
        'none'   : []
    }
    
    BASS_MINOR = {
        'simple' : [0, None, 0, None, 0, None, 0, None],
        'double' : [0, 0 , 0, 0, 0, 0, 0, 0],
        'half'   : [0, None, None, None, 0, None, None, None],
        'blues'  : [0, None, 3, None, 5, None, 7, None],
        'blues2' : [0, None, 3, None, 7, None, 9, None],
        'pop'    : [0, 0, 0, 0, 7, 7, 7, 7],
        'ballad' : [0, None, None, None, 0, None, 7, None],
        'country': [0, None, None, None, 7, None, None, None],
        # 3/4 Waltz Bass (6 steps)
        'blues12': [-12, None, None, None, None, -12, -12, None, None, None, None, None],
        'waltz':   [0, None, None, None, 7, None],
        'none'   : []
    }
    
    INTERVAL_MINOR = [0, 3, 7]
    INTERVAL_MAJOR = [0, 4, 7]
    INTERVAL_MAJ7 =  [0, 4, 7, 11]
    INTERVAL_SEVEN = -2
    INTERVAL_SIXTH = -3

    bpm = 120
    transpose = 0

    def __init__(self):
        pygame.midi.init()
        
        print("******************************************")
        print("* \033[1;31m PyJAMMER: Python-based Song composer \033[0m *")
        print("******************************************")

        port = pygame.midi.get_default_output_id()
        if port == -1:
            raise Exception("No MIDI output found.")
        self.midi_out = pygame.midi.Output(port)
        self.set_instrument('piano', channel=1)
        self.set_instrument('bass', channel=2) # Initialize bass channel
        self.Volume_Bass = 80
        self.Volume_Inst = 60
        self.Volume_Drums = 100

        # Inicialització del mòdul visualitzador
        self.visualizer = PyJammerVisualizer()

    def start_visualizer(self):
        """Funció per activar les llums"""
        self.visualizer.start()

    def stop_visualizer(self):
        """Funció per desactivar les llums"""
        self.visualizer.stop()

    def set_instrument(self, name, channel=1):
        if name in self.INSTRUMENTS:
            program_number = self.INSTRUMENTS[name]
            self.midi_out.set_instrument(program_number, channel)
        else:
            print(f"Instrument '{name}' not found.")

    def set_transpose(self, semitones):
        self.transpose = semitones
        
    def _parse_chord(self, chord_str):
        if chord_str.lower() in ["rest", "0", "pause", "_"]:
            return None 

        parts = chord_str.split('/')
        main_chord = parts[0]
        bass_note = parts[1] if len(parts) > 1 else None

        match = re.match(r"([A-G][#b]?)(maj7)?(m)?(7)?(6)?(\.)?", main_chord)
        if not match: return None
        
        root_name, is_maj7, is_minor, is_seven, is_sixth, is_ending = match.groups()
        root_offset = self.NOTE_MAP[root_name]
        
        if is_maj7:
            intervals = list(self.INTERVAL_MAJ7)
        elif is_minor:
            intervals = list(self.INTERVAL_MINOR)
        else:
            intervals = list(self.INTERVAL_MAJOR)
            
        if is_seven and not is_maj7:
            intervals.append(self.INTERVAL_SEVEN)

        if is_sixth and not is_maj7:
            intervals.append(self.INTERVAL_SIXTH)

        bass_offset = self.NOTE_MAP[bass_note] if bass_note else None
        return root_offset, intervals, bass_offset, is_minor, is_ending
        
    def set_bpm(self, new_bpm):
        self.bpm = new_bpm
        print(f"bpm = {self.bpm}")
        
    def print_progression_status(self, progression_list, i, text):
        # Si la lista está vacía, borramos la línea por completo
        if not progression_list:
            # \r vuelve al inicio y \033[K borra todo hasta el final de la línea
            print("\r\033[K", end="", flush=True)
            return

        # Build the display string highlighting the current index
        display_prog = []
        current_chord = ""
        for j, name in enumerate(progression_list):
            if i == j:
                # Highlight current chord: Bold Red
                display_prog.append(f"\033[1;31m{name}\033[0m")
                current_chord = name
            else:
                display_prog.append(name)

        # Enviar el text de l'acord/progressió al visualitzador
        prompter_text = f"[{current_chord}]  {' | '.join(progression_list)}"
        self.visualizer.trigger_text(text)

        # Use \r (carriage return) to keep the progression on a single line
        print(f"\rProgression: {' | '.join(display_prog)}        {text}", end="", flush=True)

    def play_progression(self, progression, silence_drums=False, pattern="standard", instrument='piano', arpeggio=False, bass_line='none', repetitions=1, text=""):
        self.set_instrument(instrument, channel=1)
        
        # Quarter note duration
        beat_len = 60 / self.bpm
        step_len = beat_len / 2  
        
        CHORD_CH, BASS_CH, DRUM_CH = 1, 2, 9
        progression = progression.replace(" ", "")  # clean all spaces in chord progression, added just for readibility
        progression_list = progression.split('|')   # split chords by '|' char
        
        try:
            for rep in range(repetitions):
                for i, segment_name in enumerate(progression_list):

                    self.print_progression_status(progression_list, i, text)
                    
                    sub_chords = segment_name.split(',')
                    num_sub_chords = len(sub_chords)
                    
                    active_chord_notes = []
                    last_chord_name = None
                    current_note = 0

                    # 1. DYNAMIC STEP COUNT DETECTOR (Supports 1 to 12 steps per measure)
                    selected_pattern = self.DRUM_PATTERNS.get(pattern, self.DRUM_PATTERNS['standard'])
                    nr_notes = len(selected_pattern) if selected_pattern else 8

                    for step in range(nr_notes):
                        # 2. DYNAMIC CHORD MAPPING
                        # Distributes sub-chords evenly across whatever nr_notes equals (6, 8, 12, etc.)
                        chord_idx = int(step / (nr_notes / num_sub_chords))
                        current_chord_name = sub_chords[chord_idx]

                        # --- DETECT CHORD CHANGE WITHIN THE MEASURE ---
                        if current_chord_name != last_chord_name:
                            for n in active_chord_notes:
                                self.midi_out.note_off(n, 0, CHORD_CH)
                            active_chord_notes = []

                            parsed = self._parse_chord(current_chord_name)
                            is_rest = parsed is None

                            if not is_rest:
                                root, intervals, bass, is_minor, is_ending = parsed
                                active_chord_notes = [(5 * 12 + self.transpose + root) + i_val for i_val in intervals]
                                if len(active_chord_notes) < 4:
                                    active_chord_notes.append(active_chord_notes[0] + 12)
                                
                                actual_bass_root = bass if bass is not None else root
                                bass_midi_root = (3 * 12 + self.transpose + actual_bass_root)

                                if not arpeggio:
                                    for n in active_chord_notes:
                                        self.midi_out.note_on(n, self.Volume_Inst, CHORD_CH)

                            last_chord_name = current_chord_name

                        # --- BASS LINE LOGIC ---
                        if not is_rest and bass_line != 'none':
                            bass_dict = self.BASS_MINOR if is_minor else self.BASS_MAJOR
                            bass_pattern = bass_dict.get(bass_line, [])

                            # 3. SAFE BASS STEP INDEXING
                            # Uses modulo to prevent IndexError if bass pattern length != nr_notes
                            if bass_pattern:
                                note = bass_pattern[step % len(bass_pattern)]
                            else:
                                note = None

                            if note is not None:
                                self.midi_out.note_off(current_note, 0, BASS_CH)
                                current_note = bass_midi_root + note
                                self.midi_out.note_on(current_note, self.Volume_Bass, BASS_CH)

                            # End-of-measure crash cymbal trigger
                            if step == (nr_notes - 1) and is_ending:
                                self.midi_out.note_on(self.DRUM_MAP['Y'], self.Volume_Drums, DRUM_CH)

                        # --- CHORD / ARPEGGIO LOGIC ---
                        if not is_rest and arpeggio:
                            note_to_play = active_chord_notes[step % len(active_chord_notes)]
                            self.midi_out.note_on(note_to_play, self.Volume_Inst, CHORD_CH)

                        # --- DRUM LOGIC ---
                        if not (is_rest and silence_drums):
                            self._play_pattern_beat(pattern, step, step_len, DRUM_CH)
                        else:
                            time.sleep(step_len)

                        # --- CLEANUP AT STEP END ---
                        if arpeggio and not is_rest:
                            time.sleep(0.02)
                            self.midi_out.note_off(note_to_play, 0, CHORD_CH)
                        
                        if not is_rest and bass_line != 'none':
                            self.midi_out.note_off(bass_midi_root, 0, BASS_CH)

                    # --- CLEANUP AT MEASURE END ---
                    if not arpeggio:
                        for n in active_chord_notes:
                            self.midi_out.note_off(n, 0, CHORD_CH)
                
            self.print_progression_status([], 0, "")

        except KeyboardInterrupt:
            print("\nSession ended.")

    def _play_pattern_beat(self, pattern_name, beat, beat_len, channel):
        """Plays drums based on the DRUM_PATTERNS table."""
        pattern = self.DRUM_PATTERNS.get(pattern_name, self.DRUM_PATTERNS['standard'])
        instructions = pattern[beat]

        # ENVIAR ESDEVENIMENT AL VISUALITZADOR
        if instructions:
            self.visualizer.trigger_drum(instructions)

        # Trigger notes based on characters
        for char in instructions:
            if char in self.DRUM_MAP:
                self.midi_out.note_on(self.DRUM_MAP[char], self.Volume_Drums, channel)
        
        time.sleep(beat_len)

        # Release all notes
        for char in instructions:
            if char in self.DRUM_MAP:
                self.midi_out.note_off(self.DRUM_MAP[char], 0, channel)

    def close(self):
        self.midi_out.close()
        pygame.midi.quit()

if __name__ == "__main__":
    jammer = PyJammer()
    
    jammer.set_bpm(105)
    jammer.set_transpose(0)
    #play intro beat
    #jammer.play_progression("_", pattern="hihat", bass_line='none', arpeggio=False, silence_drums=False, repetitions=1)
    
    jammer.start_visualizer()

    #play progression with each instrument
    prog = "Cmaj7|Am7|Fmaj7|G7."
    for i in range(5):
        jammer.play_progression(prog, pattern='standard', instrument='piano', bass_line='blues', arpeggio=False)
     
    jammer.close()

