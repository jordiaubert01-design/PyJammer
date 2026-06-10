import PyJammer as bb

jammer = bb.PyJammer()

intro="_|_"
comu = "Cmaj7|Cmaj7|E7|E7|A7|A7|Dm7|Dm7"
estrofa1 = "E7|E7|Am7|Am7|D7|D7|Dm|G7"
estrofa2 = "F|Fm7|Cmaj7|A7|Dm7|G7|Cmaj7|."

ending="_"

jammer.set_bpm(140)

jammer.play_progression(intro, pattern="swing", bass_line='blues')
for i in range (3):
    jammer.play_progression(comu, pattern="swing", bass_line='blues')
    jammer.play_progression(estrofa1, pattern="swing", bass_line='blues')
    jammer.play_progression(comu, pattern="swing", bass_line='blues')
    jammer.play_progression(estrofa2, pattern="swing", bass_line='blues')

jammer.play_progression(ending, pattern="swing", bass_line='blues')

jammer.close()
 