import PyJammer as bb

intro = "_"
progr1 = "D|A,G|D|D"
progr2 = "G|G|D|D|A|G|D|D"

jammer = bb.PyJammer()
jammer.set_bpm(170)

jammer.play_progression(intro, pattern="hihat", instrument='none', bass_line='simple', arpeggio=False)
jammer.play_progression(progr1, pattern="rock", instrument='piano', bass_line='country', repetitions=2, text="intro")

for i in range(3):
    jammer.play_progression(progr1, pattern="rock", instrument='piano', bass_line='simple', repetitions=4, text="verse")
    jammer.play_progression(progr2, pattern="rock", instrument='piano', bass_line='simple', repetitions=1, text="chorus")
    jammer.play_progression(progr1, pattern="rock", instrument='piano', bass_line='simple', repetitions=2, text="bridge")

jammer.close()
