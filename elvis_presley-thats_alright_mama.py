import PyJammer as bb

intro = "_"
c1 = "D|D,G|D|D|D|Bm|A|A7"
c2 = "D|D7|G|G|D|A|D|D"
v1 = "D|G|D|D|D|G|D|D"
v2 = "G|A|Bm|Bm|D|A|D|D"

jammer = bb.PyJammer()
jammer.set_bpm(250)
jammer.Volume_Inst = 40

#sjammer.play_progression("", pattern="hihat", instrument='guitar', bass_line='none', arpeggio=False, repetitions=4, text="intro")
jammer.play_progression("", pattern="standard", instrument='guitar', bass_line='none', arpeggio=False, repetitions=200, text="intro")

jammer.close()
