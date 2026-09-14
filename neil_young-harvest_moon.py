import PyJammer as pj

lyrics = """Come a little bit closer
Hear what I have to say
Just like children sleepin'
We could dream this night away

But there's a full moon risin'
Let's go dancing in the light
We know where the music's playin'
Let's go out and feel the night

Because I'm still in love with you
I want to see you dance again
Because I'm still in love with you
On this harvest moon

When we were strangers
I watched you from afar
When we were lovers
I loved you with all my heart
But now it's gettin' late
And the moon is climbin' high
I want to celebrate
See it shining in your eye
Because I'm still in love with you
I want to see you dance again
Because I'm still in love with you
On this harvest moon"""
print(lyrics)

harvest_moon = [
    ("D|D|D|D",   "..."),
    ("Em|Em|Em",   "Come a little bit closer"),
    ("Em|D|D|D|D", "Hear what I have to say"),
    ("G|G|G",   "Just like children sleepin"),
    ("G|D|D|D|D", "We could dream this night away"),
    ("G|G|G",      "But there's a full moon risin'"),
    ("G|D|D|D|D",  "Let's go dancing in the light"),
    ("G|G|G",      "We know where the music's playin'"),
    ("G|D|D|D|D",  "Let's go out and feel the night"),

    ("G|G",    "Because I'm still in love with you"),
    ("A7|A7",      "I want to see you dance again"),
    ("G|G",        "Because I'm still in love with you"),
    ("A7|A7",       "On this harvest moon"),
    ("D|D|D|D",   "..."),

    ("Em|Em|Em",   "When we were strangers"),
    ("Em|D|D|D|D", "I watched you from afar"),
    ("G|G|G",   "When we were lovers"),
    ("G|D|D|D|D", "I loved you with all my heart"),
    ("G|G|G",      "But now it's gettin' late"),
    ("G|D|D|D|D",  "And the moon is climbin' high"),
    ("G|G|G",      "I want to celebrate"),
    ("G|D|D|D|D",  "See it shining in your eye"),

    ("G|G","Because I'm still in love with you"),
    ("A7|A7","I want to see you dance again"),
    ("G|G","Because I'm still in love with you"),
    ("A7|A7","On this harvest moon"),
    ("D|D|D|D", ""),
    ("D|D|D|D", ""),
    
    ("","")
]

jammer = pj.PyJammer()
jammer.set_bpm(120)
jammer.Volume_Bass = 60

jammer.play_progression(".", pattern="hihat")

for chords, lyrics in harvest_moon:
    jammer.play_progression(chords, pattern="standard", instrument = "piano", bass_line='country', text=lyrics)

jammer.close()
