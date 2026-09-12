import PyJammer as pj

gravity_john_mayer = [
    # Intro
    ("G|C|G|C", "(Intro)"),
    
    # Verse 1
    ("G|C", "Gravity is working against me"),
    ("G|C", "And gravity wants to bring me down"),
    
    # Chorus 1
    ("Am", "Oh, I'll never know what makes this man"),
    ("D7",  "with all the love that his heart can stand"),
    ("Gm,Ebmaj7|D7,.", "dream of ways to throw it all away"),
    
    # Verse 2
    ("G|C", "Oooh, Gravity is working against me"),
    ("G|C", "And gravity wants to bring me down"),
    
    # Verse 3
    ("Am", "Oooh, twice as much ain't twice as good"),
    ("D7", "And can't sustain like one half could"),
    ("Gm,Ebmaj7|D7,.", "It's wanting more that's gonna send me to my knees"),
    
    # Solo / Interlude
    ("G|C|G|C", "(Solo)"),
    
    # Chorus 2
    ("Am", "Oooh, twice as much ain't twice as good"),
    ("D7",  "And can't sustain like one half could"),
    ("Gm,Ebmaj7|D7,.", "It's wanting more that's gonna send me to my knees"),

    # Outro
    ("G|C", "Oh, gravity, stay the hell away from me"),
    ("G|C", "Oh, gravity has taken all I got"),
    ("G|C", "Now how can that be all?"),
    ("G|C", "Just keep me where the light is"),
    ("G|C", "(ending)")
]

jammer = pj.PyJammer()

ending="_"

jammer.set_bpm(62)
jammer.Volume_Inst = 20

jammer.start_visualizer()

for chords, lyrics in gravity_john_mayer:
    jammer.play_progression(chords, pattern="ballad", instrument = "organ", bass_line='blues12', text=lyrics)

jammer.close()
