import PyJammer as bb

jammer = bb.PyJammer()

print("Song sung blue, by Neil Young")
jammer.set_bpm(105)
jammer.set_transpose(0)
jammer.play_progression("_", pattern="hihat", instrument='none', bass_line='none', arpeggio=False, silence_drums=False)
prog1 = "C|C|G|G|G|G|C|C"
prog2 = "C7|C7|C7|F|F|G|G|C|G"
for i in range(3):
    jammer.play_progression(prog1, pattern="standard", instrument='piano', bass_line='country', arpeggio=False)
    jammer.play_progression(prog2, pattern="standard", instrument='piano', bass_line='country', arpeggio=False)

jammer.close()
