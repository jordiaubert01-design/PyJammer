import PyJammer

jam = PyJammer.PyJammer()

jam.set_bpm(120)

jam.play_progression("", pattern="standard", repetitions=200)

jam.close()
