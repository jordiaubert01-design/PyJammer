import PyJammer as pj

jammer = pj.PyJammer()
jammer.set_bpm(140)
jammer.Volume_Bass = 40

p1 = "Dm|Dm|Dm|Dm."
p2 = "Dm|C,Bb|A|A."
p3a = "F|F|C|C|Bb|Bb|Dm|Dm,Bb|C|C"
p3b = "F|F|C|C|Bb|Bb|Dm|Dm,Bb|C|C,Bb|C|C"
p4 = "Dm|Bb|C|C"


jammer.play_progression(".", pattern="hihat")
#Intro
jammer.play_progression(p1, bass_line="half", repetitions = 2)
#verse 1 
jammer.play_progression(p2, repetitions=2, bass_line="half")
jammer.play_progression(p3a, repetitions=1, bass_line="half")
#verse 2 
jammer.play_progression(p2, repetitions=2, bass_line="half")
jammer.play_progression(p3b, repetitions=1, bass_line="half")
#riff
jammer.play_progression(p4, repetitions=2, bass_line="half")
#verses 3 & 4
jammer.play_progression(p2, repetitions=2, bass_line="half")
jammer.play_progression(p3b, repetitions=1, bass_line="half")
#riff
jammer.play_progression(p4, bass_line="half", repetitions=2)

jammer.set_bpm(100)
jammer.play_progression(p4, pattern="none", bass_line="half", repetitions=2)
jammer.set_bpm(110)
jammer.play_progression(p4, pattern="hihat", bass_line="half", repetitions=2)
jammer.set_bpm(120)
jammer.play_progression(p4, pattern="hihat", bass_line="half", repetitions=2)
jammer.set_bpm(130)
jammer.play_progression(p4, pattern="standard", bass_line="half", repetitions=4)
jammer.set_bpm(140)
jammer.play_progression(p4, pattern="standard", bass_line="half", repetitions=4)

jammer.close()
