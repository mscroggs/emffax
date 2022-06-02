from page_maker import Page, Line, Color
from tools.url_helpers import load_json

scores = load_json(
    "https://raw.githubusercontent.com/mscroggs/"
    "emf-2022-mathsteroids-scores/main/scores.json")

p = Page(140)

line = Line()
line.start_fg(Color.YELLOW)
line.start_double_size()
line.add_text("Mathsteroids High Scores")
p.set_line(2, line)

line_n = 5
for name, game in [
    ("Sphere", "scores-sphere"),
    ("Torus", "scores-torus"),
    ("Flat cylinder", "scores-flatcylinder"),
    ("Flat Mobius strip", "scores-flatmobius"),
    ("Flat torus", "scores-flattorus"),
    ("Flat Klein bottle", "scores-flatKlein"),
    ("Flat real projective plane", "scores-flatreal-pp"),
    ("Elliptical pool table", "scores-pool"),
]:
    line = Line()
    line.start_fg(Color.CYAN)
    line.add_text(name)
    p.set_line(line_n, line)
    line_n += 1

    line = Line()
    line.start_fg(Color.DEFAULT)
    if game in scores:
        line.add_text(f"{scores[game][0][1].upper()} {scores[game][0][0]}")
    else:
        line.add_text("(no high score yet)")
    p.set_line(line_n, line)
    line_n += 1

p.write()
