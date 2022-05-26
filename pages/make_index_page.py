from page_maker import Page, Line, Color

p = Page(100)

# Draw EMFFAX logo
line = Line()
line.start_bg(Color.BLUE)
line.add_text(" " * 37)
line.start_bg(Color.BLACK)
p.set_line(2, line)
p.set_line(8, line)

line = Line()
line.start_bg(Color.YELLOW)
line.add_block("""
............xxxxxxxxx.............xxxxxx.............xxxxxxxxxxxxxxxxxxx
............xxxxxxxxx.............xxxxxx.............xxxxxxxxxxxxxxxxxxx
......xxxx..xxxxxxxxxxxxxx..xxxx..xxxxxxxxxx...xxx...xxxxxxxxxxxxxxxxxxx
""", Color.BLUE, None)
line.start_bg(Color.BLACK)
p.set_line(3, line)

line = Line()
line.start_bg(Color.YELLOW)
line.add_block("""
......xxxx..x............x..xxxx..x........x..xxxxx..x..................
......xx....x............x..xx....x........x..xx..x..x..................
......xxxx..x..xx....xx..x..xxxx..x..xxxx..x..xxxxx..x..xx.xx...........
""", Color.BLUE, None)
line.start_bg(Color.BLACK)
p.set_line(4, line)

line = Line()
line.start_bg(Color.YELLOW)
line.add_block("""
......xx....x..xxx..xxx..x..xx....x..xxxx..x..xxxxx..x..xx.xx...........
......xxxx..x..xxxxxxxx..x..xx....x..xx....x..xx..x..x..xx.xx...........
......xxxx..x..xx.xx.xx..x..xx....x..xxxx..x..xx..x..x...xxx............
""", Color.BLUE, None)
line.start_bg(Color.BLACK)
p.set_line(5, line)

line = Line()
line.start_bg(Color.YELLOW)
line.add_block("""
............x..xx....xx..x........x..xx....x.........x..xx.xx...........
............x..xx....xx..x........x..xx....x.........x..xx.xx...........
............x..xx....xx..x........x..xx....x.........x..xx.xx...........
""", Color.BLUE, None)
line.start_bg(Color.BLACK)
p.set_line(6, line)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
.............xxxxxxxxxxxx..........xxxxxxxx...........xxxxxxxxxxxxxxxxxx
.........xxxxxxxxxxxxxxxx......xxxxxxxxxxxx.......xxxxxxxxxxxxxxxxxxxxxx
.........xxxxxxxxxxxxxxxx......xxxxxxxxxxxx.......xxxxxxxxxxxxxxxxxxxxxx
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.set_line(7, line)

# List pages
index = [
    ("NEWS", 101),
    ("ABOUT EMFFAX", 114),
    ("_EMFFAX", 120),
    ("@EMFFAX", 121),
    ("HOLIDAYS", 400),
    ("BLUE PETER", 525),
    ("LOTTERY", 555),
    ("EMF SCHEDULE", 600),
    ("NOW & NEXT", 606),
]

for n, (i, j) in enumerate(zip(index[::2], index[1::2])):
    line = Line()
    line.start_fg(Color.YELLOW)
    line.add_text((i[0] + " " * 14)[:14])
    line.start_fg(Color.WHITE)
    line.add_text(f"{i[1]}")
    line.add_text(" ")
    line.start_fg(Color.YELLOW)
    line.add_text((j[0] + " " * 14)[:14])
    line.start_fg(Color.WHITE)
    line.add_text(f"{j[1]}")
    p.set_line(10 + n, line)

p.write()
