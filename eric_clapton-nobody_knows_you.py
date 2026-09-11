import PyJammer as bb

intro = "_"
progr1 = "C,E|A7|Dm,A7|Dm"
progr2 = "F,D7|C,A7|D7|G7"

jammer = bb.PyJammer()
jammer.set_bpm(90)

jammer.play_progression(intro, pattern="hihat", instrument='none', bass_line='', arpeggio=False)

for i in range(3):
    jammer.play_progression(progr1, pattern="rock", instrument='piano', bass_line='simple', text="")
    jammer.play_progression(progr2, pattern="rock", instrument='piano', bass_line='simple', text="")

jammer.close()
