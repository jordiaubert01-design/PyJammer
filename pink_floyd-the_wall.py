import PyJammer as bb

intro = "_|_"
progr1 = "Dm|Dm|Dm|Dm|Dm|Dm|Dm|Dm|G|G|Dm|Dm"
progr2 = "G|G|Dm|Dm|G|G|Dm|Dm|G|G|Dm|Dm"
progr3 = "G|G|Bb|Bb|C|C|Dm|Dm|_|_"

jammer = bb.PyJammer()
jammer.set_bpm(110)

jammer.play_progression(intro, pattern="disco", instrument='guitar', bass_line='none', arpeggio=False)
for i in range(1):
    jammer.play_progression(progr1, pattern="disco", instrument='guitar', bass_line='simple', arpeggio=False)
    jammer.play_progression(progr2, pattern="disco", instrument='guitar', bass_line='simple', arpeggio=False)
    jammer.play_progression(progr3, pattern="disco", instrument='guitar', bass_line='simple', arpeggio=False)
    
jammer.close()
