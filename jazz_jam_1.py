import PyJammer as bb

intro = "Cmaj7|Am7|Fmaj7|G7"
progression = "Cmaj7|Am7|Fmaj7|G7"
ending = "Cmaj7|Fmaj7|Cmaj7"

jammer = bb.PyJammer()
jammer.set_bpm(110)

jammer.play_progression(intro, pattern="swing", instrument='piano', bass_line='none', arpeggio=True, silence_drums=True)

for i in range(20):
    jammer.play_progression(progression, pattern="swing", instrument='piano', bass_line='blues', arpeggio=False)

jammer.play_progression(ending, pattern="swing", instrument='piano', bass_line='none', arpeggio=True, silence_drums=True)

jammer.close()
