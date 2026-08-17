import PyJammer

jam = PyJammer.PyJammer()

def standard(bpm=120):
    jam.set_bpm(bpm)
    jam.play_progression("", pattern="standard", bass_line="none", instrument = "none", repetitions=200)

def bombo(bpm=120):
    jam.set_bpm(bpm)
    jam.play_progression("", pattern="bass", bass_line="none", instrument = "none", repetitions=200)

def rock(bpm=120):
    jam.set_bpm(bpm)
    jam.play_progression("", pattern="rock", bass_line="none", instrument = "none", repetitions=200)

def country(bpm=200):
    jam.set_bpm(bpm)
    jam.play_progression("", pattern="standard", instrument='none', bass_line='none', arpeggio=False, repetitions=200)

def walz(bpm=120):
    jam.set_bpm(bpm)
    jam.play_progression("", pattern="waltz", instrument='none', bass_line='none', arpeggio=False, repetitions=200)

#bombo(100)
#country(200)
#walz(90)

pat = "standard"
bpm = 120

while (True):
        jam.set_bpm(bpm)
        jam.play_progression("", pattern=pat, instrument='none', bass_line='none', arpeggio=False, repetitions=200)


jam.close()
