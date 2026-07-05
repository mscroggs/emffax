from pyfax import Page, Line, Color
from datetime import datetime
from pyfax.tools.url_helpers import load_xml


def xml_children(element, tag):
    return [i for i in element if i.tag == tag]


def xml_child(element, tag):
    children = xml_children(element, tag)
    assert len(children) == 1
    return children[0]


p = Page(555)

line = Line()
line.start_double_size()
line.add_text("National Lottery Results")
p.set_line(2, line)

data = load_xml("https://www.national-lottery.co.uk/results/lotto/draw-history/xml")
game = xml_child(data, "game")
draw = xml_child(game, "draw")
date = datetime.strptime(xml_child(draw, "draw-date").text, "%Y-%m-%d")
balls = xml_children(game, "balls")
machines = xml_children(draw, "draw-machine")

round1 = [b.text for b in xml_children(balls[0], "ball")]
round1_bonus = xml_child(balls[0], "bonus-ball").text
round1_balls = xml_child(balls[0], "set").text
round1_machine = machines[0].text

round2 = [b.text for b in xml_children(balls[1], "ball")]
round2_bonus = xml_child(balls[1], "bonus-ball").text
round2_balls = xml_child(balls[1], "set").text
round2_machine = machines[1].text

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text(date.strftime("%a %-d %b"))
p.set_line(4, line)

line = Line()
line.start_double_size()
line.add_text("Round 1:")
for i, j in enumerate(round1_balls):
    line.start_fg([Color.CYAN, Color.YELLOW][i % 2])
    line.add_text(f"{j}")
line.start_fg(Color.RED)
line.add_text(f"{round1_bonus}")
p.set_line(6, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text(f"Machine: {round1_machine}")
p.set_line(9, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text(f"Set of balls number {round1_balls}")
p.set_line(10, line)

line = Line()
line.start_double_size()
line.add_text("Round 2:")
for i, j in enumerate(round2_balls):
    line.start_fg([Color.CYAN, Color.YELLOW][i % 2])
    line.add_text(f"{j}")
line.start_fg(Color.RED)
line.add_text(f"{round2_bonus}")
p.set_line(6, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text(f"Machine: {round2_machine}")
p.set_line(9, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text(f"Set of balls number {round2_balls}")
p.set_line(10, line)

p.write()
