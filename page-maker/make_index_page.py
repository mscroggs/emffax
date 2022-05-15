from page import Page, Line, Color

p = Page(100)

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

line = Line()
line.set_color(Color.RED)
line.add_text("Red")
line.set_color(Color.GREEN)
line.add_text("Green")
line.set_color(Color.BLUE)
line.add_text("Blue")
line.set_color(Color.CYAN)
line.add_text("Cyan")
line.set_color(Color.MAGENTA)
line.add_text("Magenta")
line.set_color(Color.YELLOW)
line.add_text("Yellow")
p.set_line(9, line)

line = Line()
line.add_text("Red: ")
line.add_block("""
.xx...
x.xx.x
.x.xx.
""", Color.RED)
line.add_text("Green: ")
line.add_block("""
.xx...
x.xx.x
.x.xx.
""", Color.GREEN)
line.add_text("Blue: ")
line.add_block("""
.xx...
x.xx.x
.x.xx.
""", Color.BLUE)
p.set_line(10, line)

line = Line()
line.add_text("Cyan: ")
line.add_block("""
.xx...
x.xx.x
.x.xx.
""", Color.CYAN)
line.add_text("Magenta: ")
line.add_block("""
.xx...
x.xx.x
.x.xx.
""", Color.MAGENTA)
line.add_text("Yellow: ")
line.add_block("""
.xx...
x.xx.x
.x.xx.
""", Color.YELLOW)
p.set_line(11, line)

with open("../P100.tti", "w") as f:
    f.write(p.to_tti())
