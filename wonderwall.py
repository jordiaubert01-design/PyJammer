import PyJammer as bb

intro = "_"
progr1 = "Em|G|D|A7"

jammer = bb.PyJammer()
jammer.set_bpm(110)

jammer.play_progression(intro, pattern="hihat", instrument='none', bass_line='simple', arpeggio=False)
jammer.play_progression(progr1, pattern="hihat", instrument='none', bass_line='simple', arpeggio=False)
    
jammer.close()
