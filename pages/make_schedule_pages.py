from page_maker import Page, Line, Color
from tools.url_helpers import load_json
from datetime import datetime


class Content:
    def __init__(self, data, page):
        self.data = data
        self.page = page
        self.start = datetime.strptime(data["start_date"], "%Y-%m-%d %H:%M:%S")
        self.end = datetime.strptime(data["end_date"], "%Y-%m-%d %H:%M:%S")
        self.venue = data["venue"]

    def make_page(self):
        assert self.page is not None
        p = Page(self.page)
        line_n = p.add_wrapped_text(2, self.data["title"], double=True)

        line = Line()
        line.start_fg(Color.YELLOW)
        line.add_text(self.data["speaker"][:38])
        p.set_line(line_n, line)
        line_n += 1

        line = Line()
        line.start_fg(Color.YELLOW)
        line.add_text(self.start.strftime("%a %H:%M"))
        line.add_text("-")
        line.add_text(self.end.strftime("%H:%M"))
        p.set_line(line_n, line)
        line_n += 1

        line = Line()
        line.start_fg(Color.YELLOW)
        line.add_text(self.data["venue"][:22])
        p.set_line(line_n, line)
        line_n += 1

        if self.data["description"] is not None:
            p.add_wrapped_text(line_n + 1, self.data["description"])
        p.write()


# TODO: update to 2022
data = load_json("https://www.emfcamp.org/schedule/2018.json")
stages = ["Stage A", "Stage B", "Stage C"]
now = datetime.now()

# Date in past to test. TODO: remove this
now = datetime(2018, 9, 2, 11, 32, 10, 3)


daily = {stage: {"Fri": [], "Sat": [], "Sun": []}
         for stage in stages}

upcoming = {}
page_n = 630
for item in data:
    if item["venue"] in stages:
        c = Content(item, page_n)
        c.make_page()
        page_n += 1
    else:
        c = Content(item, None)
    if c.end > now:
        if c.venue not in upcoming:
            upcoming[c.venue] = []
        upcoming[c.venue].append(c)
    if c.venue in daily:
        daily[c.venue][c.start.strftime("%a")].append(c)

# Now and next page
p = Page(606)
line = Line()
line.start_fg(Color.YELLOW)
line.start_double_size()
line.add_text("Now and Next")
p.set_line(2, line)

line_n = 5
for venue in stages:
    if venue in upcoming:
        line = Line()
        line.start_fg(Color.YELLOW)
        line.add_text(venue)
        p.set_line(line_n, line)
        line_n += 1

        upcoming[venue] = sorted(upcoming[venue], key=lambda item: item.start)
        for i, item in enumerate(upcoming[venue][:2]):
            line = Line()
            line.start_fg(Color.CYAN)
            line.add_text(item.start.strftime("%a %H:%M"))
            line.add_text("-")
            line.add_text(item.end.strftime("%H:%M"))
            line.start_fg(Color.DEFAULT)
            if item.page is None:
                line.add_text(item.data["title"][:23])
            else:
                line.add_text((item.data["title"] + " " * 19)[:19])
                line.start_fg(Color.YELLOW)
                line.add_text(f"{item.page}")
            p.set_line(line_n, line)
            line_n += 1
        line_n += 1

p.write()

# Pages for each stage
index = []
index.append(("Now & Next", 606))
pn = 0
for day in ["Friday", "Saturday", "Sunday"]:
    for venue in stages:
        short_day = day[:3]

        index.append((f"{venue} {day}", 610 + pn))

        p = Page(610 + pn)
        line = Line()
        line.start_fg(Color.YELLOW)
        line.start_double_size()
        line.add_text(venue + " " + day)
        p.set_line(2, line)

        line_n = 4

        daily[venue][short_day].sort(key=lambda item: item.start)
        for item in daily[venue][short_day][:17]:
            line = Line()
            line.start_fg(Color.CYAN)
            line.add_text(item.start.strftime("%H:%M"))
            line.start_fg(Color.DEFAULT)
            if item.page is None:
                line.add_text(item.data["title"][:31])
            else:
                line.add_text((item.data["title"] + " " * 27)[:27])
                line.start_fg(Color.YELLOW)
                line.add_text(f"{item.page}")
            p.set_line(line_n, line)
            line_n += 1

        p.write()
        pn += 1

p = Page(600)
line = Line()
line.start_fg(Color.MAGENTA)
line.start_double_size()
line.add_text("EMF Schedule")
p.set_line(2, line)

index.sort(key=lambda i: i[1])

for i, (page, n) in enumerate(index):
    line = Line()
    line.start_fg(Color.YELLOW)
    line.add_text((page + " " * 20)[:20])
    line.start_fg(Color.DEFAULT)
    line.add_text(f"{n}")
    p.set_line(5 + i, line)

p.write()
