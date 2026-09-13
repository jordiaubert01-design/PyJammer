import PyJammer as bb

intro = "_"
progr1 = "Em7,G|D,A7"
prog2 = "C,Em7|G,Em7"

jammer = bb.PyJammer()
jammer.set_bpm(87)

jammer.play_progression(intro, pattern="hihat", instrument='none', bass_line='none')
jammer.play_progression(progr1, pattern="standard", instrument='none', bass_line='pop', repetitions=4, text="(intro)")
jammer.play_progression(progr1, pattern="standard", instrument='none', bass_line='pop', repetitions=4, text="(verse1)")
jammer.play_progression(progr1, pattern="standard", instrument='none', bass_line='pop', repetitions=4, text="(verse2)")
jammer.play_progression(prog2, pattern="standard", instrument='none', bass_line='simple', repetitions=4, text="(chorus)")
    
jammer.close()
