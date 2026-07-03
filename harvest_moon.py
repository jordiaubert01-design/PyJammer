import PyJammer as pj

jammer = pj.PyJammer()
jammer.set_bpm(120)
jammer.Volume_Bass = 60

p1 = "D|D|D|D"
p2 = "Em|Em|Em|Em|D|D|G|G|G|G"
p3 = "G|G|A7|A7|G|G|A7|A7"


jammer.play_progression(".", pattern="hihat")
#Intro
jammer.play_progression(p1, bass_line="country", repetitions = 1)
for i in range(4):
    #etrofa
    jammer.play_progression(p2, bass_line="country", repetitions = 1)
    jammer.play_progression(p1, bass_line="country", repetitions = 1)
    jammer.play_progression(p3, bass_line="country", repetitions = 1)
    jammer.play_progression(p1, bass_line="country", repetitions = 1)

jammer.play_progression(p1, bass_line="country", repetitions = 4)

jammer.close()
