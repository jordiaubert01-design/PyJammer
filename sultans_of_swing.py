import PyJammer as pj

jammer = pj.PyJammer()
jammer.set_bpm(135)
jammer.Volume_Bass = 40

p1 = "Dm|Dm|Dm|Dm."
p2 = "Dm|C,Bb|A|A."
p3 = "F|F|C|C|Bb|Bb|Dm|Dm,Bb|C|C"
p4 = "Dm|Bb|C.|C"

def verse():
    jammer.play_progression(p2, repetitions=2, bass_line="half")
    jammer.play_progression(p3, repetitions=1, bass_line="half")

jammer.play_progression(".", pattern="hihat")
#Intro
jammer.play_progression(p1, bass_line="half")
#verses 1 & 2
verse()
verse()
#riff
jammer.play_progression(p4, repetitions=2, bass_line="half")
#verses 3 & 4
verse()
verse()
#riff
jammer.play_progression(p4, repetitions=2, bass_line="half")

jammer.close()
