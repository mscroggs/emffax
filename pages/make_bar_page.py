from pyfax import Page, Line, Color
# from pyfax.tools.url_helpers import load_json
from datetime import datetime

# sessions = load_json("https://bar.emf.camp/api/sessions.json")
# on_tap = load_json("https://bar.emf.camp/api/on-tap.json")

sessions = {"sessions": []}
on_tap = {}

open = False
now = datetime.now()
for s in sessions["sessions"]:
    start = datetime.strptime(s["opening_time"], "%Y-%m-%dT%H:%M:%S")
    end = datetime.strptime(s["closing_time"], "%Y-%m-%dT%H:%M:%S")
    if start < now < end:
        open = True
        break

p = Page(150)

line = Line()
line.start_double_size()
line.add_text("The robot arms  ")
if open:
    line.start_fg(Color.GREEN)
    line.add_text("OPEN")
else:
    line.start_fg(Color.RED)
    line.add_text("CLOSED")
p.set_line(2, line)

line_n = 5
for i, data in on_tap.items():
    line = Line()
    line.start_fg(Color.YELLOW)
    line.add_text(i[0].upper() + i[1:])
    p.set_line(line_n, line)
    line_n += 1

    for item in data:
        line = Line()
        line.start_fg(Color.DEFAULT)
        line.add_text((item["fullname"] + " " * 30)[:30])
        line.start_fg(Color.CYAN)
        line.add_text("GBP" + item["price"])
        p.set_line(line_n, line)
        line_n += 1

p.write()
