import PyJammer as bb

intro = "_|_"
p1 = "G,C|G|F|G"
p2 = "C|D|G,C|G."
p3 = "Bm|Em|Bm|Bm|G|Em|A7|D7"
jammer = bb.PyJammer()
jammer.set_bpm(140)

jammer.play_progression(intro, pattern="hihat", instrument='guitar', bass_line='none', arpeggio=False)
#verse 1
jammer.play_progression(p1, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=2)
jammer.play_progression(p2, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=1)
#verse 2
jammer.play_progression(p1, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=2)
jammer.play_progression(p2, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=1)
#bridge
jammer.play_progression(p3, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=1)
#verse 3
jammer.play_progression(p1, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=2)
jammer.play_progression(p1, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=2)
#solo
jammer.play_progression(p2, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=1)
jammer.play_progression(p1, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=2)
#bridge
jammer.play_progression(p3, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=1)
#ending
jammer.play_progression(p1, pattern="standard", instrument='electric_guitar', bass_line='simple', arpeggio=False, repetitions=4)

jammer.close()
