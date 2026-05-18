import PyJammer as bb

intro = "_"
progression = "Am7|Am7|Am7|Am7|Dm7|Dm7|Am7|Am7|Em7|Dm7|Am7|E7."
ending = "_|Am7"

jammer = bb.PyJammer()
jammer.set_bpm(115)

jammer.play_progression(intro, pattern="", instrument='piano', bass_line='none', arpeggio=True, silence_drums=False)

for i in range(20):
    jammer.play_progression(progression, pattern="swing", instrument='piano', bass_line='blues', arpeggio=False)

jammer.play_progression(ending, pattern="swing", instrument='piano', bass_line='none', arpeggio=True, silence_drums=True)

jammer.close()
