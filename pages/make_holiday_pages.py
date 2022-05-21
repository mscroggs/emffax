from page_maker import Page, Line, Color

p = Page(400)


line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
........................................................................
........................................................................
xxxxxxxxxxxxxxxxxxxx.......xxxxxxxx......xxxxxxxx.......................
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.set_line(2, line)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
xxxxxxxxxxxxxxx....x.........x....x........x....x.......................
xxxxxxxxxxxxxxx..xxx.xxxxxxx.x..xxx.xxxxxx.x..x.x.xxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx...xx.x..x..x.x...xx.x....x.x....x.x..x..xxxxxxxxxxxxxxxx
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.set_line(3, line)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
xxxxxxxxxxxxxxx..xxx.x.....x.x..xxx.x..xxx.x..x.x.x..x..xxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxx....x.x.x.x.x.x..xxx.x...xx.x..x.x.xx...xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxx.x.xxx.x.xxxxxx.x..xxx.xxxxxx.x..x..xxxxxxxxxxxxxxxx
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.set_line(4, line)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
.....................x.xxx.x........x..xxx........x..x..xxxxxxxxxxxxxxxx
...................xxxxxxxxx......xxxxxxxx......xxxxxxxxxxxxxxxxxxxxxxxx
........................................................................
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.set_line(5, line)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
........................................................................
xxxxxxx.xxxxxxx.xxxxxxx.xxxxxx.xxxxxxx.xxxxxxx.xxxxxxx.xxxxxxx..........
x..x..x.x.....x.x..xxxx.x....x.x....xx.x.....x.x..x..x.x.....x..........
""", Color.WHITE, None)
line.start_bg(Color.BLACK)
p.set_line(6, line)

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
p.set_line(7, line)

line = Line()
line.start_bg(Color.BLUE)
line.add_block("""
x..x..x.x.....x.x.....x.x....x.x....xx.x..x..x.x.....x.x.....x
xxxxxxx.xxxxxxx.xxxxxxx.xxxxxx.xxxxxxx.xxxxxxx.xxxxxxx.xxxxxxx
..............................................................
""", Color.WHITE, None)
p.set_line(8, line)
line.add_block("""
xxxxxxx.
xxxxxx..
xxxxxx..
""", Color.YELLOW, None)
line.start_bg(Color.BLACK)
p.write()
