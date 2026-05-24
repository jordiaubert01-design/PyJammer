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

    # The Pattern Table: Each list contains 4 beats, each beat contains instructions
    DRUM_PATTERNS = {
        'hihat':    ["H", "H", "H", "H"],
        'bass':     ["B", "B", "B", "B"],
        'clap':     ["C", "C", "C", "C"],
        'bell':     ["O", "O", "O", "O"],
        'snare':    ["S", "S", "S", "S"],
        'swing':    ["KH", "H", "SH", "H"], # Logic can be adjusted for swing feel
        'disco':    ["K", "SH", "K", "SH"],
        'standard': ["KH", "SH", "KH", "SH"],
        'none':     ["", "", "", ""]
    }

    #different bass styles, where each defines a note for each beat
    BASS_MAJOR = {
        'simple' : [0,0,0,0],
        'half' : [0,None,0,None],
        'blues' : [0,3,5,7],
        'pop' : [0,0,0,7],
        'ballad' : [0,None,0,7],
        'country' : [0, None, 7, None],
        'none' : []
    }
    BASS_MINOR = {
        'simple' : [0,0,0,0],
        'half' : [0,None,0,None],
        'blues' : [0,3,5,7],
        'pop' : [0,0,0,7],
        'ballad' : [0,None,0,7],
        'country' : [0, None, 7, None],
        'none' : []
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
        self.Volume_Bass = 70
        self.Volume_Inst = 50
        self.Volume_Drums = 90
        
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
        
    def print_progression_status(self, progression_list, i):
        # Build the display string highlighting the current index
        display_prog = []
        for j, name in enumerate(progression_list):
            if i == j:
                # Highlight current chord: Bold Red
                display_prog.append(f"\033[1;31m{name}\033[0m")
            else:
                display_prog.append(name)
        
        # Use \r (carriage return) to keep the progression on a single line
        print(f"\rProgression: {' | '.join(display_prog)}", end="", flush=True)

    def play_progression(self, progression, silence_drums=False, pattern="standard", instrument='piano', arpeggio=False, bass_line='none', repetitions=1):
        self.set_instrument(instrument, channel=1)
        beat_len = 60 / self.bpm
        CHORD_CH, BASS_CH, DRUM_CH = 1, 2, 9
        
        progression_list = progression.split('|')
        
        try:
            for rep in range(repetitions):
                for i, segment_name in enumerate(progression_list):

                    self.print_progression_status(progression_list, i)
                    
                    # Split the segment by commas to see if there are sub-chords
                    # e.g., "C" -> ["C"] | "C,G" -> ["C", "G"]
                    sub_chords = segment_name.split(',')
                    num_sub_chords = len(sub_chords)
                    
                    # Keep track of active notes to turn them off when chords change
                    active_chord_notes = []
                    last_chord_name = None

                    for beat in range(4):
                        # Determine which chord belongs to the current beat
                        # If 1 chord: index 0 for all 4 beats
                        # If 2 chords ("C,G"): beats 0,1 get index 0 ("C"), beats 2,3 get index 1 ("G")
                        chord_idx = int(beat / (4 / num_sub_chords))
                        current_chord_name = sub_chords[chord_idx]

                        # --- DETECT CHORD CHANGE WITHIN THE MEASURE ---
                        if current_chord_name != last_chord_name:
                            # Turn off the previous chord notes if any are playing
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

                                # Trigger the new instrument chord (Block mode)
                                if not arpeggio:
                                    for n in active_chord_notes:
                                        self.midi_out.note_on(n, self.Volume_Inst, CHORD_CH)

                            last_chord_name = current_chord_name

                        # --- BASS LINE LOGIC ---
                        if not is_rest and bass_line != 'none':
                            if is_minor:
                                note = self.BASS_MINOR[bass_line][beat]
                            else:
                                note = self.BASS_MAJOR[bass_line][beat]
                                
                            if note is not None:
                                self.midi_out.note_on(bass_midi_root + note, self.Volume_Bass, BASS_CH)

                            if beat == 3 and is_ending:
                                self.midi_out.note_on(self.DRUM_MAP['Y'], self.Volume_Drums, DRUM_CH)

                        # --- CHORD / ARPEGGIO LOGIC ---
                        if not is_rest and arpeggio:
                            note_to_play = active_chord_notes[beat % len(active_chord_notes)]
                            self.midi_out.note_on(note_to_play, self.Volume_Inst, CHORD_CH)

                        # --- DRUM LOGIC ---
                        if not (is_rest and silence_drums):
                            self._play_pattern_beat(pattern, beat, beat_len, DRUM_CH)
                        else:
                            time.sleep(beat_len)

                        # --- CLEANUP AT THE END OF EACH BEAT ---
                        if arpeggio and not is_rest:
                            time.sleep(0.05) 
                            self.midi_out.note_off(note_to_play, 0, CHORD_CH)
                        
                        if not is_rest and bass_line != 'none':
                            self.midi_out.note_off(bass_midi_root, 0, BASS_CH)

                    # --- CLEANUP AT THE END OF THE MEASURE ---
                    if not arpeggio:
                        for n in active_chord_notes:
                            self.midi_out.note_off(n, 0, CHORD_CH)
                
            self.print_progression_status([], 0)

        except KeyboardInterrupt:
            print("\nSession ended.")

    def _play_pattern_beat(self, pattern_name, beat, beat_len, channel):
        """Plays drums based on the DRUM_PATTERNS table."""
        pattern = self.DRUM_PATTERNS.get(pattern_name, self.DRUM_PATTERNS['standard'])
        instructions = pattern[beat]

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
    jammer.play_progression("_", pattern="hihat", bass_line='none', arpeggio=False, silence_drums=False)
    
    #play progression with each instrument
    prog = "Cmaj7|Am7|Fmaj7|G7."
    for i in range(1):
        jammer.play_progression(prog, pattern='swing', instrument='piano', bass_line='blues', arpeggio=False)
     
    jammer.close()

