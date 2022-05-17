from page_maker import Page, Line, Color
from tools.url_helpers import load_json
from datetime import datetime

# TODO: update to 2022
data = load_json("https://www.emfcamp.org/schedule/2018.json")

now = datetime.now()
# Date in past to test. TODO: remove this
now = datetime(2018, 9, 2, 11, 32, 10, 3)

venues = ["Stage A", "Stage B", "Stage C"]

events = {}
for item in data:
    the_date = datetime.strptime(item["end_date"], "%Y-%m-%d %H:%M:%S")
    if the_date > now:
        if item["venue"] not in events:
            events[item["venue"]] = []
        events[item["venue"]].append(item)


p = Page(606)
line = Line()
line.start_fg(Color.YELLOW)
line.start_double_size()
line.add_text("Now and Next")
p.set_line(2, line)

line_n = 5
for venue in venues:
    if venue in events:
        line = Line()
        line.start_fg(Color.YELLOW)
        line.add_text(venue)
        p.set_line(line_n, line)
        line_n += 1

        village_events = sorted(events[venue], key=lambda item: item["start_date"])
        for i, item in enumerate(village_events[:2]):
            line = Line()
            line.start_fg(Color.CYAN)
            line.add_text(item["start_date"].split()[1][:5])
            line.add_text("-")
            line.add_text(item["end_date"].split()[1][:5])
            line.start_fg(Color.DEFAULT)
            line.add_text(item["speaker"][:28])
            p.set_line(line_n, line)
            line_n += 1

            line = Line()
            line.start_fg(Color.DEFAULT)
            line.add_text(item["title"][:38])
            p.set_line(line_n, line)
            line_n += 1
        line_n += 1

p.write()

for i, venue in enumerate(["Stage A", "Stage B", "Stage C"]):
    p = Page(601 + i)
    line = Line()
    line.start_fg(Color.YELLOW)
    line.start_double_size()
    line.add_text(venue)
    p.set_line(2, line)

    line_n = 4

    village_events = sorted(events[venue], key=lambda item: item["start_date"])
    for i, item in enumerate(village_events[:9]):
        line = Line()
        line.start_fg(Color.CYAN)
        line.add_text(item["start_date"].split()[1][:5])
        line.add_text("-")
        line.add_text(item["end_date"].split()[1][:5])
        line.start_fg(Color.DEFAULT)
        line.add_text(item["speaker"][:27])
        p.set_line(line_n, line)
        line_n += 1

        line = Line()
        line.start_fg(Color.DEFAULT)
        line.add_text(item["title"][:38])
        p.set_line(line_n, line)
        line_n += 1

    p.write()

p = Page(600)
line = Line()
line.start_fg(Color.YELLOW)
line.start_double_size()
line.add_text("EMF Schedule")
p.set_line(2, line)

for i, venue in enumerate(["Stage A", "Stage B", "Stage C"]):
    line = Line()
    line.start_fg(Color.DEFAULT)
    line.add_text(venue + "      ")
    line.start_fg(Color.YELLOW)
    line.add_text(f"{601+i}")
    p.set_line(5 + i, line)

line = Line()
line.start_fg(Color.DEFAULT)
line.add_text("Now & Next   ")
line.start_fg(Color.YELLOW)
line.add_text(f"606")
p.set_line(8, line)

p.write()
