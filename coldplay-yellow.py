import PyJammer as pj

jammer = pj.PyJammer()
jammer.set_bpm(85)
jammer.Volume_Bass = 60

p1 = "B|B|F#|F#|E|E"
p11 = "B|B"
p2 = "E|B,F#"
jammer.play_progression(".", pattern="hihat")
#Intro
jammer.play_progression(p1+"|"+p11, bass_line="double", pattern="standard", repetitions = 1, text="intro")
#verses
for i in range(2):
    jammer.play_progression(p1, bass_line="double", pattern="bass", repetitions = 2, text="look at the stars, look how they shine for you...")
    jammer.play_progression(p11, bass_line="double", pattern="bass", repetitions = 1)
    jammer.play_progression(p2, bass_line="double", pattern="bass", repetitions = 3, text="your skin, oh yeah, your skin, and bones...")
    jammer.play_progression("E", bass_line="double", pattern="bass", repetitions = 2, text="...and it was all yellow")
    jammer.play_progression(p1+"|"+p11, bass_line="double", pattern="bass", repetitions = 1)

jammer.close()
