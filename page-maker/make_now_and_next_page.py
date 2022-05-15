from page import Page, Line, Color
from url_helpers import load_json

data = load_json("https://www.emfcamp.org/schedule/2018.json")

p = Page(606)

line = Line()
line.add_text("Coming soon")
p.set_line(2, line)

with open("../P606.tti", "w") as f:
    f.write(p.to_tti())
