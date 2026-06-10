import PyJammer as pj

jammer = pj.PyJammer()
jammer.set_bpm(140)
jammer.Volume_Bass = 60
jammer.Volume_Inst = 40

p1 = "A,B|C#m"
p2 = "A,B|G#m."
ch1 = "A|A|E|E"
ch2 = "A|A|C#m|G#m|F#m|Am|C#m|C#m."
br1 = "E|E|B|B|G#m|G#m|F#m|F#m"

jammer.play_progression(".", pattern="hihat")

#intro
jammer.play_progression(p1, bass_line="simple", instrument="piano", repetitions = 3, text="(intro)")
jammer.play_progression(p2, bass_line="simple", instrument="piano",                  text="(intro)")

#Verse1
jammer.play_progression(p1, bass_line="simple", instrument="piano", text="Lady Writer on the TV")
jammer.play_progression(p1, bass_line="simple", instrument="piano", text="Talking about virgin mary")
jammer.play_progression(p1, bass_line="simple", instrument="piano", text="The way he used to look")
jammer.play_progression(p2, bass_line="simple", instrument="piano", text="And I kno he never read a book")
jammer.play_progression(p1, bass_line="simple", instrument="piano", repetitions = 3)
jammer.play_progression(p2, bass_line="simple", instrument="piano", text="(verse1)")
#chorus
jammer.play_progression(ch1, bass_line="simple", instrument="piano", text="Just the way that her hair fell down around her face")
jammer.play_progression(ch2, bass_line="simple", instrument="piano", text="Then I recall my fall from grace, Another time, another place")

#Verse2
jammer.play_progression(p1, bass_line="simple", instrument="piano", repetitions = 3)
jammer.play_progression(p2, bass_line="simple", instrument="piano", text="(verse2)")
jammer.play_progression(p1, bass_line="simple", instrument="piano", repetitions = 3)
jammer.play_progression(p2, bass_line="simple", instrument="piano", text="(verse2)")
#chorus
jammer.play_progression(ch1, bass_line="simple", instrument="piano")
jammer.play_progression(ch2, bass_line="simple", instrument="piano")

#bridge
jammer.play_progression(br1, bass_line="simple", instrument="piano", repetitions = 3)

#solo
jammer.play_progression(p1, bass_line="simple", instrument="piano", repetitions = 3, text="(solo)")
jammer.play_progression(p2, bass_line="simple", instrument="piano", text="(solo)")
#chorus
jammer.play_progression(ch1, bass_line="simple", instrument="piano")
jammer.play_progression(ch2, bass_line="simple", instrument="piano")

#Verse3
jammer.play_progression(p1, bass_line="simple", instrument="piano", repetitions = 3)
jammer.play_progression(p2, bass_line="simple", instrument="piano", text="(verse3)")
jammer.play_progression(p1, bass_line="simple", instrument="piano", repetitions = 3)
jammer.play_progression(p2, bass_line="simple", instrument="piano", text="(verse3)")

#Outtro
jammer.play_progression(p1, bass_line="simple", instrument="piano", repetitions = 3, text="(outtro)")
jammer.play_progression(p2, bass_line="simple", instrument="piano", text="(outtro)")
jammer.play_progression(p1, bass_line="simple", instrument="piano", repetitions = 3, text="(outtro)")
jammer.play_progression(p2, bass_line="simple", instrument="piano", text="(outtro)")

jammer.close()
