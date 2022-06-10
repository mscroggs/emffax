from pyfax import Page, Line, Color

p = Page(400)


p.add_block(1, """
........................................................................
........................................................................
xxxxxxxxxxxxxxxxxxxx.......xxxxxxxx......xxxxxxxx.......................
xxxxxxxxxxxxxxx....x.........x....x........x....x.......................
xxxxxxxxxxxxxxx..xxx.xxxxxxx.x..xxx.xxxxxx.x..x.x.xxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx...xx.x..x..x.x...xx.x....x.x....x.x..x..xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx..xxx.x.....x.x..xxx.x..xxx.x..x.x.x..x..xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx....x.x.x.x.x.x..xxx.x...xx.x..x.x.xx...xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx.x.xxx.x.xxxxxx.x..xxx.xxxxxx.x..x..xxxxxxxxxxxxxxxx
.....................x.xxx.x........x..xxx........x..x..xxxxxxxxxxxxxxxx
...................xxxxxxxxx......xxxxxxxx......xxxxxxxxxxxxxxxxxxxxxxxx
........................................................................
""", Color.YELLOW, bg=Color.BLUE)

p.add_block(5, """
........................................................................
xxxxxxx.xxxxxxx.xxxxxxx.xxxxxx.xxxxxxx.xxxxxxx.xxxxxxx.xxxxxxx..........
x..x..x.x.....x.x..xxxx.x....x.x....xx.x.....x.x..x..x.x.....x..........
""", Color.WHITE, bg=Color.BLUE)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
x..x..x.x..x..x.x..xxxx.xx..xx.x..x..x.x..x..x.x..x..x.x..xxxx
x.....x.x..x..x.x..xxxx.xx..xx.x..x..x.x.....x.x.....x.x.....x
x..x..x.x..x..x.x..xxxx.xx..xx.x..x..x.x..x..x.xxxx..x.xxxx..x
""", Color.WHITE, None)
line.add_block("""
xxxxxxxx
xxxxxxxx
xxxxxxx.
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.set_line(6, line)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
x..x..x.x.....x.x.....x.x....x.x....xx.x..x..x.x.....x.x.....x
xxxxxxx.xxxxxxx.xxxxxxx.xxxxxx.xxxxxxx.xxxxxxx.xxxxxxx.xxxxxxx
..............................................................
""", Color.WHITE, None)
line.add_block("""
xxxxxxx.
xxxxxx..
xxxxxx..
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.set_line(7, line)

line = Line()
line.start_bg(Color.BLUE)
line.start_fg(Color.CYAN)
line.add_text(" " * 26)
line.add_block("""
..xxxxxxxxxxxxx...
....xxxxxxxxx.....
......xxxxx.......
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.set_line(8, line)

line = Line()
line.start_bg(Color.BLUE)
line.start_fg(Color.CYAN)
line.add_text(" " * 26)
line.add_block("""
..x.....x.....x...
..................
........x.........
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.set_line(9, line)

line = Line()
line.start_bg(Color.BLUE)
line.start_fg(Color.CYAN)
line.add_text(" " * 26)
line.add_block("""
x...............x.
........x.........
..................
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.set_line(10, line)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
........................
...xxxxxxx..............
..xx..x..xxx............
""", Color.GREEN, None)
line.start_fg(Color.YELLOW)
line.add_text("USA")
line.start_fg(Color.GREEN)
line.add_text("Los Angeles")
line.start_fg(Color.CYAN)
line.add_text("....401")
line.start_bg(Color.BLACK)
p.set_line(11, line)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
.xx.......xxx...........
......xxx...xx.....xx...
...xxxxxxxx.xxx...xxxx..
""", Color.GREEN, None)
line.start_fg(Color.YELLOW)
line.add_text("ENGLAND")
line.start_fg(Color.GREEN)
line.add_text("Ledbury")
line.start_fg(Color.CYAN)
line.add_text("....402")
line.start_bg(Color.BLACK)
p.set_line(12, line)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
..xxxxxxxxx..xxxxxxxx...
xxx.xx.xx.xxxxxxxxxx....
x.x.x.........xxxx.xxxx.
""", Color.GREEN, None)
line.start_fg(Color.YELLOW)
line.add_text("MALAYSIA")
line.start_fg(Color.GREEN)
line.add_text("Langkawi")
line.start_fg(Color.CYAN)
line.add_text("..403")
line.start_bg(Color.BLACK)
p.set_line(13, line)

line = Line()
line.start_bg(Color.BLUE)
line.start_fg(Color.CYAN)
line.add_block("""
.........x
........xx
........xx
""", Color.RED, None)
line.add_block("""
..xx..xxx.
.xxxx..xxx
..xx...xx.
""", Color.GREEN, None)
line.start_fg(Color.YELLOW)
line.add_text("N'LANDS")
line.start_fg(Color.GREEN)
line.add_text("Zeewolde")
line.start_fg(Color.CYAN)
line.add_text("...404")
line.start_bg(Color.BLACK)
p.set_line(14, line)

line = Line()
line.start_bg(Color.BLUE)
line.start_fg(Color.CYAN)
line.add_block("""
.......xx.
.......xx.
......xxx.
""", Color.RED, None)
line.add_block("""
.xxx....x.
..x.....x.
xxx....x..
""", Color.GREEN, None)
line.start_fg(Color.YELLOW)
line.add_text("NORWAY")
line.start_fg(Color.GREEN)
line.add_text("Kautokeino")
line.start_fg(Color.CYAN)
line.add_text("..405")
line.start_bg(Color.BLACK)
p.set_line(15, line)

line = Line()
line.start_bg(Color.BLUE)
line.start_fg(Color.CYAN)
line.add_block("""
......xx
.....xxx
.....xxx
""", Color.RED, None)
line.add_block("""
...x
..xx
..x.
""", Color.GREEN, None)
line.add_text(" " * 28)
line.start_bg(Color.BLACK)
p.set_line(16, line)

line = Line()
line.start_bg(Color.YELLOW)
line.start_fg(Color.CYAN)
line.add_block("""
....xxxx
....xxx.
...xxxx.
""", Color.RED, None)
line.add_block("""
................xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
...................xxxxxxxxxxxxxxx.xxxxxxxxxx.xxxxxxxxxxxxxxx
.......................xxxxx.xxxxxxxx.xxxxxxxxxxxxxxxxxxxxx.x
""", Color.CYAN, None)
line.start_bg(Color.BLACK)
p.set_line(17, line)

line = Line()
line.start_bg(Color.YELLOW)
line.add_block("""
...xxxx.
...xxxx.
..xxxxx.
""", Color.RED, None)
line.add_block("""
..................
...xxxx..xxxxxx...
.....xxxxxxxx.....
""", Color.BLUE, None)
line.add_block("""
.......xxxxxxxxxxxxx.xxxxxxxxxxxxxxxxxxxxxx
..............xxxxxxxxxxxxxxxxxxxx.xxxxxxxx
.......................xxxxxxxxxxxxxxxxxxxx
""", Color.CYAN, None)
line.start_bg(Color.BLACK)
p.set_line(18, line)

line = Line()
line.start_bg(Color.YELLOW)
line.start_fg(Color.CYAN)
line.add_block("""
..xxxxxxxxxxxxxxxxxxxxxxx...
......xxxxxxxxx...xxxx.xxx..
.................xxxx...xxx.
""", Color.BLUE, None)
line.add_block("""
................................xxxxxxxxx
.........................................
.........................................
""", Color.CYAN, None)
line.start_bg(Color.BLACK)
p.set_line(19, line)

line = Line()
line.start_bg(Color.YELLOW)
line.start_fg(Color.CYAN)
line.add_text(" " * 24)
line.start_fg(Color.BLUE)
line.add_text("Trains")
line.start_fg(Color.RED)
line.add_text("407 ")
line.start_bg(Color.BLACK)
p.set_line(20, line)

line = Line()
line.add_block("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
............................................................................
............................................................................
""", Color.YELLOW, None)

p.lines[21] = line

p.write()

things_to_see = {
    "Los Angeles": [
        "Venice Beach", "Stroll along the stars in Hollywood",
        "Shop in style on Rodeo Drive", "Museum of Jurassic Technology",
        "Los Angeles County Museum of Art", "Griffith Observatory",
        "Disneyland", "The Broad Museum", "Watts Towers Arts Center",
        "Walt Disney Concert Hall", "Amoeba Music", "Cruise along Mulholland",
        "Japanese American National Museum", "Huntington Library"
    ],
    "Ledbury": ["Electromagnetic Field 2022"],
    "Langkawi": [
        "Walk on the beach", "Shopping (tax-free)", "Island hopping",
        "Jet-skiing"
    ],
    "Zeewolde": ["MCH2022"],
    "Kautokeino": [
        "RiddoDuottar Museum", "Juhls Silver Gallery", "Samiway",
        "Sokkiadventure", "Pikefossen", "Kautokeino Church", "Freeze"
    ],
    "Lower Brailes": [
        "Brailes church", "Mine Hill", "Brailes Hill", "Castle Hill",
        "Baldwin's", "Paddock Farm", "Playing Fields", "Fairfax Interiors"
    ]
}

for n, (location, things) in enumerate(things_to_see.items()):
    p = Page(401 + n)
    line = Line()
    line.start_double_size()
    line.add_text("Things to do in")
    line.start_fg(Color.CYAN)
    line.add_text(location)
    p.set_line(2, line)

    for i, j in enumerate(things):
        line = Line()
        line.start_fg([Color.YELLOW, Color.CYAN][i % 2])
        line.add_text(j)
        p.set_line(5 + i, line)

    p.write()
