from page_maker import Page, Line, Color

p = Page(525)
p1 = Page(526)
p2 = Page(527)
p3 = Page(528)

logo = """
....................................................
........x........................x..................
.......xx......xx...............xx........x.........
.....xxxxx....xxx.............xxxxxx.....x.x........
...xxxxxxxx..xx.x...........xxxxxxxxx....x.x........
.....xx..xx.xx.xx..............xx..xx...xxx.........
....xx..xxx.x.xx..............xx..xxx...xxxxx.......
....xxxxxx.xxxxx..............xxxxxx.xxxxx......x...
..xxxxxxx..xxxx.xx.x..xxx...xxxxxx.....xx..xxx.xxx.x
...xxxxx..xxxx.xx.xx.xx.x....xxx..xxx.xxx.xx.x.xxxxx
...xx.xxx..xx.xx.xx.xx.xx...xx...xx.x.xx.xx.xx.x.xx.
...xx..xx.xx.xx.xx.xxxxx....xx.xxxxx.xx..xxxx.xx....
..xx...xx.xxxxxxxxxxxxxx...xx...xx..xxx.xxx..xx.....
..xx..xxx.xxxxxxxxx.xx.x...xx...xx.xxxxxxxxxxxx.....
.xxxxxxx.....xx.xx...xx...xx....xxxx.xxx.xxx.xx.....
.xxxxxx...................xx.....xx.................
xx..................................................
....................................................
"""

p.add_block(1, logo, Color.BLUE, bg=Color.WHITE, indent=3)
p1.add_block(1, logo, Color.BLUE, bg=Color.WHITE, indent=3)
p2.add_block(1, logo, Color.BLUE, bg=Color.WHITE, indent=3)
p3.add_block(1, logo, Color.BLUE, bg=Color.WHITE, indent=3)

line = Line()
line.start_double_size()
line.add_text("BUILD: Tracy Island    ")
line.start_fg(Color.YELLOW)
line.add_text("526")
p.set_line(8, line)

line = Line()
line.start_double_size()
line.add_text("Blue Peter Badges      ")
line.start_fg(Color.YELLOW)
line.add_text("527")
p.set_line(11, line)

line = Line()
line.start_double_size()
line.add_text("About the presenters   ")
line.start_fg(Color.YELLOW)
line.add_text("528")
p.set_line(14, line)

p.write()

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("BUILD: Tracy Island")
p1.set_line(7, line)

p1.add_wrapped_text(
    8,
    "MATERIALS: Grocery carton, Cereal pack cardboard, Newspapers, "
    "Kitchen foil, P.V.A. glue, Soap powder packet, Oblong cheese box, "
    "Paper bowl, Washing-up liquid bottle, Potato crisp tube, Small "
    "adhesive labels, Blue and grey pens, 75 mm flower pot saucer, "
    "Sandpaper, 2 medium and 1 small matchboxes, Sponge, Drinking "
    "straw, Corrugated paper, Brass paper fastener, Blue card, Pipe "
    "cleaners, Green and brown crepe paper, Green, brown and gray paint, "
    "Sawdust", color=Color.YELLOW)

p1.write()

line = Line()
line.start_double_size()
line.add_text("Badges")
p2.set_line(8, line)

line = Line()
line.start_fg(Color.BLUE)
line.add_text("Blue badges")
line.start_fg(Color.DEFAULT)
line.add_text("are awarded for sending in")
p2.set_line(10, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("interesting letters.")
line.start_fg(Color.GREEN)
line.add_text("Green badges")
line.start_fg(Color.DEFAULT)
line.add_text("are")
p2.set_line(11, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("awarded for caring about nature. Silver")
p2.set_line(12, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("badges are awarded to extra-special")
p2.set_line(13, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("blue badge holders.")
line.start_fg(Color.MAGENTA)
line.add_text("Purple badges")
line.start_fg(Color.DEFAULT)
line.add_text("are")
p2.set_line(14, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("awarded for joining the Blue Peter fan")
p2.set_line(15, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("club.")
line.start_fg(Color.CYAN)
line.add_text("Music badges")
line.start_fg(Color.DEFAULT)
line.add_text("were designed by Ed")
p2.set_line(16, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("Sheeran.")
line.start_fg(Color.CYAN)
line.add_text("Sport badges")
line.start_fg(Color.DEFAULT)
line.add_text("are awarded for")
p2.set_line(17, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("getting active.")
line.start_fg(Color.YELLOW)
line.add_text("Orange badges")
line.start_fg(Color.DEFAULT)
line.add_text("are")
p2.set_line(18, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("awarded to competition winners.")
line.start_fg(Color.YELLOW)
line.add_text("Gold")
p2.set_line(19, line)

line = Line()
line.start_fg(Color.YELLOW)
line.add_text("badges")
line.start_fg(Color.DEFAULT)
line.add_text("are very rare indeed.")
p2.set_line(20, line)

p2.write()

line = Line()
line.start_double_size()
line.add_text("Presenters")
p3.set_line(8, line)

n = p3.add_wrapped_text(
    10,
    "Konnie Huq was a Blue Peter presenter from 1997 to 2008. She has "
    "A-levels in chemistry, maths and physics.", color=Color.YELLOW)

n = p3.add_wrapped_text(
    n + 1,
    "Valerie Singleton was a Blue Peter presenter from 1962 to 1972. "
    "She is the daughter of an RAF wing commander.",
    color=Color.CYAN)

n = p3.add_wrapped_text(
    n + 1,
    "Richie Driss has been a Blue Peter presenter since 2019. He is "
    "a Manchester United fan.",
    color=Color.YELLOW)

p3.write()
