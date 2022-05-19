from page_maker import Page, Line, Color
from tools.url_helpers import load_json
from datetime import datetime


class Content:
    def __init__(self, data, page):
        self.data = data
        self.page = page
        self.start = datetime.strptime(data["start_date"], "%Y-%m-%d %H:%M:%S")
        self.end = datetime.strptime(data["end_date"], "%Y-%m-%d %H:%M:%S")

    def make_page(self):
        p = Page(self.page)
        line = Line()
        line.start_double_size()
        line.add_text(self.data["title"][:38])
        p.set_line(2, line)

        line = Line()
        line.start_fg(Color.YELLOW)
        line.add_text(self.data["speaker"][:38])
        p.set_line(4, line)
        line = Line()
        line.start_fg(Color.YELLOW)
        line.add_text(self.start.strftime("%a %H:%M"))
        line.add_text("-")
        line.add_text(self.end.strftime("%H:%M"))
        line.add_text("  ")
        line.add_text(self.data["venue"][:22])
        p.set_line(5, line)

        if self.data["description"] is not None:
            p.add_wrapped_text(6, self.data["description"])
        p.write()


# TODO: update to 2022
data = load_json("https://www.emfcamp.org/schedule/2018.json")

now = datetime.now()
# Date in past to test. TODO: remove this
now = datetime(2018, 9, 2, 11, 32, 10, 3)

page_n = 630

upcoming = {}
for item in data:
    the_date = datetime.strptime(item["end_date"], "%Y-%m-%d %H:%M:%S")
    c = Content(item, page_n)
    c.make_page()
    page_n += 1
    if the_date > now:
        if item["venue"] not in upcoming:
            upcoming[item["venue"]] = []
        upcoming[item["venue"]].append(c)

# Now and next page
p = Page(606)
line = Line()
line.start_fg(Color.YELLOW)
line.start_double_size()
line.add_text("Now and Next")
p.set_line(2, line)

line_n = 5
for venue in ["Stage A", "Stage B", "Stage C"]:
    if venue in upcoming:
        line = Line()
        line.start_fg(Color.YELLOW)
        line.add_text(venue)
        p.set_line(line_n, line)
        line_n += 1

        village_events = sorted(upcoming[venue], key=lambda item: item.start)
        for i, item in enumerate(village_events[:2]):
            line = Line()
            line.start_fg(Color.CYAN)
            line.add_text(item.start.strftime("%a %H:%M"))
            line.add_text("-")
            line.add_text(item.end.strftime("%H:%M"))
            line.start_fg(Color.DEFAULT)
            line.add_text((item.data["title"] + " " * 19)[:19])
            line.start_fg(Color.YELLOW)
            line.add_text(f"{item.page}")
            p.set_line(line_n, line)
            line_n += 1
        line_n += 1

p.write()

# Pages for each stage
for i, venue in enumerate(["Stage A", "Stage B", "Stage C"]):
    p = Page(601 + i)
    line = Line()
    line.start_fg(Color.YELLOW)
    line.start_double_size()
    line.add_text(venue)
    p.set_line(2, line)

    line_n = 4

    for i, item in enumerate(village_events[:8]):
        line = Line()
        line.start_fg(Color.CYAN)
        line.add_text(item.start.strftime("%a %H:%M"))
        line.add_text("-")
        line.add_text(item.end.strftime("%H:%M"))
        line.start_fg(Color.DEFAULT)
        line.add_text(item.data["speaker"][:23])
        p.set_line(line_n, line)
        line_n += 1

        line = Line()
        line.start_fg(Color.DEFAULT)
        line.add_text((item.data["title"] + " " * 34)[:34])
        line.start_fg(Color.YELLOW)
        line.add_text(f"{item.page}")
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
line.add_text("606")
p.set_line(8, line)

p.write()
