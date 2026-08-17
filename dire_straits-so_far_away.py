import PyJammer

jam = PyJammer.PyJammer()

jam.set_bpm(125)

p1 = "B|A|E|E"
v1 = "E|B|B|E"
ch1 = "A|C#m|B|E"
ch2 = "A|C#m|B|A|E"

jam.Volume_Instrument = 20

jam.play_progression(" | ", pattern="hihat", bass_line="", instrument = "none")
jam.play_progression(p1, pattern="standard", bass_line="half", instrument = "none", repetitions=2, text = "intro")

for i in range(4):
    jam.play_progression(p1, pattern="standard", bass_line="half", instrument = "none", repetitions=2, text = "intro")

    jam.play_progression(v1, pattern="standard", bass_line="half", instrument = "none", repetitions=2, text = "verse 1")
    jam.play_progression(ch1, pattern="standard", bass_line="half", instrument = "none", repetitions=1, text = "chorus")
    jam.play_progression(ch2, pattern="standard", bass_line="half", instrument = "none", repetitions=1, text = "chorus")

jam.play_progression(p1, pattern="standard", bass_line="half", instrument = "none", repetitions=8, text = "intro")

jam.close()
