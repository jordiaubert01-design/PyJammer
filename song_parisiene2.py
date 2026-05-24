import PyJammer as bb


jammer = bb.PyJammer()
jammer.set_bpm(70)
jammer.set_instrument("piano")

print("Starting Jam: Parisienne Walkways by Gary Moore ")

intro="Am|_"
pr1 = "Am|Dm|G|Cmaj7|F|Gm|E|A"
ending="_"

jammer.play_progression(intro, silence_drums=False, instrument="piano")
jammer.play_progression(pr1, silence_drums=False, bass_line='ballad')
jammer.play_progression(pr1, silence_drums=False, bass_line='ballad')
#end
jammer.play_progression(ending, silence_drums=False)

