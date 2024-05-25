from pyfax import Page, Line, Color

p = Page(113)

line = Line()
line.start_double_size()
line.add_text("About")
line.start_fg(Color.YELLOW)
line.add_text("EMFFAX")
p.set_line(2, line)

n = p.add_wrapped_text(
    4,
    "EMFFAX is a text-based information service inspired by "
    "CEEFAX (see page 115). EMFFAX was created by "
    "Matthew Scroggs (@mscroggs).")
n = p.add_wrapped_text(
    n + 1,
    "EMFFAX uses vbit2 to encode teletext files into this "
    "television's video input.")
n = p.add_wrapped_text(
    n + 1,
    "The Python code that generates these pages can be found on "
    "GitHub at github.com/mscroggs/emffax")

p.write()

p = Page(114)

line = Line()
line.start_double_size()
line.add_text("About")
line.start_fg(Color.YELLOW)
line.add_text("CEEFAX")
p.set_line(2, line)

n = p.add_wrapped_text(
    4,
    "CEEFAX was a text-based information service provided by the BBC. "
    "The service ran from 1974-2012 and could be accessed by pressing "
    "the teletext button on any suitable TV.")

n = p.add_wrapped_text(
    n + 1,
    "As well as being available at any time via the teletext button, "
    "pages from CEEFAX were broadcast overnight on BBC One and BBC Two. "
    "In 1997, BBC One started broadcasting rolling news instead of CEEFAX "
    "pages. BBC Two continued to broadcast pages from CEEFAX until 2012.")

p.write()

p = Page(115)

line = Line()
n = p.add_wrapped_text(
    2,
    "EMFFAX's source code is available at "
    "https://github.com/mscroggs/emffax")

p.add_block(n + 1, """
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xx.......xxx.x..x.xxx.xx.......xx
xx.xxxxx.x.x.xx...x.xx.x.xxxxx.xx
xx.x...x.xxxxx..x.xx...x.x...x.xx
xx.x...x.x...x.x..x..x.x.x...x.xx
xx.x...x.xx.xxxxx.xxxx.x.x...x.xx
xx.xxxxx.x..x..xxx..x.xx.xxxxx.xx
xx.......x.x.x.x.x.x.x.x.......xx
xxxxxxxxxxx...xx.x.xx..xxxxxxxxxx
xx.....x....x.xxx....x..x.x.x.xxx
xxx.x.x.x.xx.x....xx....x...x.xxx
xx..x..x.xxx.xx...x.x.xxx.x..xxxx
xxx....xxxxxxx..xx....x.....xx.xx
xxx.xx.x.xx..x.x..x.xx.....xxxxxx
xx.x.xxxx.xxxxxxxx.xxx..xxx.xxxxx
xx.xxxx..x..x..xx.x.x.xxxxx....xx
xx..xx..xx.xx.xx.x.x...x...xx..xx
xxx.xx.x......xxx.x.xx.xx.xxxxxxx
xx.x.xxxx.x..x...x.xx..xx...x..xx
xx.xx.x..xx.xxx...x.x.xxxxx...xxx
xx.xx.x.x..xxx..xx.x.......xx..xx
xx.xx.xx..x..x.x....xx.......xxxx
xxxxxxxxxx.xxxxxx..xx..xxx.xx.xxx
xx.......x.x...xxxx.x..x.x.xx.xxx
xx.xxxxx.xx.x.xx.x.xxx.xxx.x...xx
xx.x...x.x....xxx....x.....x...xx
xx.x...x.x.xxx.....xxx..x.xxxxxxx
xx.x...x.x...xx...x...x...xx..xxx
xx.xxxxx.x.xxx..xx...x..xxx..x.xx
xx.......x...x.x....x....x...xxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
""", Color.WHITE)

p.write()
