import PyJammer as bb

print("Starting Jam: Parisienne Walkways by Gary Moore ")

jammer = bb.PyJammer()
jammer.set_bpm(80)
jammer.Volume_Bass = 40

#start
jammer.play_progression("Am|_", silence_drums=False, instrument="piano")
#main progression x 3 times
pr1="Dm|G|Cmaj7|F|Bb|E|Am|_"
jammer.play_progression(pr1, silence_drums=False, instrument="piano", bass_line="ballad", repetitions=8)
#end
jammer.play_progression("_", silence_drums=False)

