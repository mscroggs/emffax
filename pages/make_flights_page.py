import config
from tools.url_helpers import load_json
from page_maker import Page, Line, Color


if config.aviationstack_key is None:
    data = []
else:
    data = load_json("http://api.aviationstack.com/v1/flights?"
                     f"access_key={config.aviationstack_key}&limit=20&dep_iata=LHR")["data"]

p = Page(406)

line = Line()
line.start_double_size()
line.add_text("Departures from Heathrow")
p.set_line(2, line)

line_n = 5
for flight in data:
    line = Line()
    line.start_fg(Color.YELLOW)
    line.add_text(flight["flight"]["number"])
    line.start_fg(Color.DEFAULT)
    line.add_text((flight["arrival"]["airport"] + " " * 18)[:18])
    line.add_text(f" ({flight['arrival']['iata']})")
    line.start_fg(Color.YELLOW)
    line.add_text(":".join(
        flight["departure"]["estimated"].split("T")[1].split(":")[:2]))
    t = flight["departure"]["terminal"]
    if t is not None:
        line.start_fg(Color.RED)
        line.add_text(f"T{t}")
    p.set_line(line_n, line)
    line_n += 1
    if line_n > 20:
        break

p.write()
