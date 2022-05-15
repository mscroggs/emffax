from page import Page, Line, Color

p = Page(100)

l = Line()
l.start_bg(Color.BLUE)
p.set_line(2, l)
p.set_line(8, l)

l = Line()
l.start_bg(Color.YELLOW)
l.add_block("""
............xxxxxxxxx.............xxxxxx.............xxxxxxxxxxxxxxxxxxx
............xxxxxxxxx.............xxxxxx.............xxxxxxxxxxxxxxxxxxx
......xxxx..xxxxxxxxxxxxxx..xxxx..xxxxxxxxxx...xxx...xxxxxxxxxxxxxxxxxxx
""", Color.BLUE, None)
l.start_bg(Color.BLACK)
p.set_line(3, l)

l = Line()
l.start_bg(Color.YELLOW)
l.add_block("""
......xxxx..x............x..xxxx..x........x..xxxxx..x..................
......xx....x............x..xx....x........x..xx..x..x..................
......xxxx..x..xx....xx..x..xxxx..x..xxxx..x..xxxxx..x..xx.xx...........
""", Color.BLUE, None)
l.start_bg(Color.BLACK)
p.set_line(4, l)

l = Line()
l.start_bg(Color.YELLOW)
l.add_block("""
......xx....x..xxx..xxx..x..xx....x..xxxx..x..xxxxx..x..xx.xx...........
......xxxx..x..xxxxxxxx..x..xx....x..xx....x..xx..x..x..xx.xx...........
......xxxx..x..xx.xx.xx..x..xx....x..xxxx..x..xx..x..x...xxx............
""", Color.BLUE, None)
l.start_bg(Color.BLACK)
p.set_line(5, l)

l = Line()
l.start_bg(Color.YELLOW)
l.add_block("""
............x..xx....xx..x........x..xx....x.........x..xx.xx...........
............x..xx....xx..x........x..xx....x.........x..xx.xx...........
............x..xx....xx..x........x..xx....x.........x..xx.xx...........
""", Color.BLUE, None)
l.start_bg(Color.BLACK)
p.set_line(6, l)

l = Line()
l.start_bg(Color.BLUE)
l.add_block("""
.............xxxxxxxxxxxx..........xxxxxxxx...........xxxxxxxxxxxxxxxxxx
.........xxxxxxxxxxxxxxxx......xxxxxxxxxxxx.......xxxxxxxxxxxxxxxxxxxxxx
.........xxxxxxxxxxxxxxxx......xxxxxxxxxxxx.......xxxxxxxxxxxxxxxxxxxxxx
""", Color.YELLOW, None)
l.start_bg(Color.BLACK)
p.set_line(7, l)

with open("../P100.tti", "w") as f:
    f.write(p.to_tti())
