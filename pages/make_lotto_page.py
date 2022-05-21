from page_maker import Page, Line, Color
from datetime import datetime
from tools.url_helpers import load_csv

p = Page(555)

line = Line()
line.start_double_size()
line.add_text("National Lottery Results")
p.set_line(2, line)

data = load_csv("https://www.national-lottery.co.uk/results/lotto/draw-history/csv")
res = data[1]
date = datetime.strptime(res[0], "%d-%b-%Y")
numbers = sorted([int(i) for i in res[1:7]])
bonus = res[7]
set_of_balls = res[8]
machine = res[9]

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text(date.strftime("%a %-d %b"))
p.set_line(4, line)

line = Line()
line.start_double_size()
for i, j in enumerate(numbers):
    line.start_fg([Color.BLUE, Color.YELLOW][i % 2])
    line.add_text(f"{j}")
line.start_fg(Color.RED)
line.add_text(f"{bonus}")
p.set_line(6, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text(machine)
p.set_line(8, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text(f"Set of balls number {set_of_balls}")
p.set_line(9, line)

p.write()
