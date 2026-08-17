import PyJammer as pj

# Song: Oasis - Don't Look Back in Anger

jammer = pj.PyJammer()
jammer.set_bpm(82)
#jammer.Volume_Bass = 60

intro = "C|F."
p1 = "C,G|Am,E|F,G|C,G"
p2 = "F,Fm|C|F,Fm|C|F,Fm|C"
p2b = "G|E|Am,G|F|G"

jammer.play_progression(".", pattern="hihat")
#Intro
jammer.play_progression(intro, bass_line="half", pattern="hihat", repetitions = 2, text="intro")
#verse1
jammer.play_progression(p1, bass_line="half", pattern="standard", repetitions = 2, text="verse 1")
jammer.play_progression(p2, bass_line="half", pattern="standard", repetitions = 1, text="verse 1")
jammer.play_progression(p2b, bass_line="half", pattern="standard", repetitions = 1, text="verse 1")
#Chorus
jammer.play_progression(p1, bass_line="double", pattern="standard", repetitions = 2, text="chorus")

#verse2
jammer.play_progression(p1, bass_line="half", pattern="standard", repetitions = 2, text="verse 1")
jammer.play_progression(p2, bass_line="half", pattern="standard", repetitions = 1, text="verse 1")
jammer.play_progression(p2b, bass_line="half", pattern="standard", repetitions = 1, text="verse 1")
#Chorus
jammer.play_progression(p1, bass_line="double", pattern="standard", repetitions = 2, text="chorus")

jammer.close()
