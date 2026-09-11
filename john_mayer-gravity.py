import PyJammer as pj

jammer = pj.PyJammer()

intro= "G|C"
pat1 = "G|C|G|C|Am|D7"
pat2 = "Gm,Ebmaj7|D7,."

ending="_"

jammer.set_bpm(62)
jammer.Volume_Inst = 20
#jammer.Volume_Bass = 100

jammer.start_visualizer()

jammer.play_progression(".", pattern="ballad", instrument = "", bass_line='')
jammer.play_progression(intro, pattern="ballad", instrument = "organ", bass_line='blues12')

for i in range(4):
    jammer.play_progression(pat1, pattern="ballad", instrument = "organ", bass_line='blues12')
    jammer.play_progression(pat2, pattern="ballad", instrument = "organ", bass_line='blues12')

jammer.close()
