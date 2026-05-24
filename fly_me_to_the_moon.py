import PyJammer as bb

intro = "_"
progression1 = "Am7|Dm7|G7|Cmaj7|Fmaj7|Bm7|E7|Am7"
progression2 = "Dm7|G7|Em7|A7|Dm7|G7|Cmaj7|E7"
ending = "_"

jammer = bb.PyJammer()
jammer.set_bpm(120)

jammer.play_progression(intro, pattern="swing", instrument='piano', bass_line='none', arpeggio=False, silence_drums=False)

for i in range(2):
    jammer.play_progression(progression1, pattern="swing", instrument='piano', bass_line='blues', arpeggio=False)
    jammer.play_progression(progression2, pattern="swing", instrument='organ', bass_line='blues', arpeggio=False)

jammer.play_progression(ending, pattern="swing", instrument='guitar', bass_line='none', arpeggio=False, silence_drums=False)

jammer.close()
