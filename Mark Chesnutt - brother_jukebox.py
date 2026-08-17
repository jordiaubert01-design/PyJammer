import PyJammer as bb

intro = "_"
c1 = "D|D,G|D|D|D|Bm|A|A7"
c2 = "D|D7|G|G|D|A|D|D"
v1 = "D|G|D|D|D|G|D|D"
v2 = "G|A|Bm|Bm|D|A|D|D"

jammer = bb.PyJammer()
jammer.set_bpm(140)
jammer.Volume_Inst = 40

jammer.play_progression(intro, pattern="hihat", instrument='guitar', bass_line='none', arpeggio=False)

#chorus
jammer.play_progression(c1, pattern="standard", instrument='piano', bass_line='country')
jammer.play_progression(c2, pattern="standard", instrument='piano', bass_line='country')

for i in range(4):
    #verse
    jammer.play_progression(v1, pattern="hihat", instrument='piano', bass_line='country')
    jammer.play_progression(v2, pattern="hihat", instrument='piano', bass_line='country')
    #chorus
    jammer.play_progression(c1, pattern="standard", instrument='piano', bass_line='country')
    jammer.play_progression(c2, pattern="standard", instrument='piano', bass_line='country')

jammer.close()
