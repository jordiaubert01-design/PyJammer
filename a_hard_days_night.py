import PyJammer as bb

intro = "_|_"
progr1 = "G|C|G|F|G"

jammer = bb.PyJammer()
jammer.set_bpm(180)

jammer.play_progression(intro, pattern="disco", instrument='guitar', bass_line='none', arpeggio=False)
jammer.play_progression(progr1, pattern="standard", instrument='electric_guitar', bass_line='none', arpeggio=False, repetitions=4)

jammer.close()
