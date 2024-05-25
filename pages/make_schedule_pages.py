from pyfax import Page, Line, Color
from pyfax.tools.url_helpers import load_json
from datetime import datetime

data = load_json("https://www.emfcamp.org/api/villages")

perpage = 17
page_n = 200 + len(data) // perpage

workshop_villages = {
    "Drop-In Workshops": 0,
    "Nottingham Hackspace": 1,
    "Milliways": 2,
    "Furry High Commssion": 3,
    "Field-FX": 4,
    "Maths Village": 5,
    "Hardware Hacking Area": 6,
}
workshop_pages = []

for i in range(len(data) // perpage):
    p = Page(200 + i)
    line = Line()
    line.start_double_size()
    line.add_text("Villages")
    line.start_fg(Color.YELLOW)
    line.add_text(f"{i + 1}/{len(data) // perpage}")
    p.set_line(2, line)

    for j in range(perpage):
        line = Line()
        line.start_fg(Color.DEFAULT)
        v = perpage * i + j
        line.add_text((data[v]["name"] + " " * 20)[:20])
        line.start_fg(Color.YELLOW)
        line.add_text(f"{page_n}")
        p.set_line(3 + j, line)
        sub_p = Page(page_n)
        line = Line()
        line.start_double_size()
        line.add_text(data[v]["name"])
        sub_p.set_line(2, line)

        line = Line()
        line.start_fg(Color.MAGENTA)
        if data[v]['location'] is not None:
            line.add_text(f"{data[v]['location']['coordinates'][0]},"
                          f"{data[v]['location']['coordinates'][1]}")
        sub_p.set_line(4, line)

        if data[v]["name"] in workshop_villages:
            n = workshop_villages[data[v]["name"]]
            workshop_pages.append((n, data[v]["name"], page_n))
            line = Line()
            line.start_fg(Color.DEFAULT)
            line.add_text(f"Workshop {n} ")
            line.start_fg(Color.YELLOW)
            line.add_text(f"{780 + 3 * n - 2}")
            sub_p.set_line(5, line)
            sub_p.add_wrapped_text(7, data[v]["description"])
        else:
            sub_p.add_wrapped_text(6, data[v]["description"])

        sub_p.write()

        page_n += 1
        if page_n == 888:
            page_n += 1

    p.write()


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


data = load_json("https://www.emfcamp.org/schedule/2024.json")
stages = ["Stage A", "Stage B", "Stage C"]
now = datetime.now()

workshop_pages.sort(key=lambda x: x[0])

daily = {stage: {"Fri": [], "Sat": [], "Sun": []}
         for stage in stages + [f"Workshop {i[0]}" for i in workshop_pages]}

upcoming = {}
for item in data:
    c = Content(item, None)
    if c.end > now:
        if c.venue not in upcoming:
            upcoming[c.venue] = []
        upcoming[c.venue].append(c)
    if c.venue in daily and c.start.strftime("%a") in daily[c.venue]:
        daily[c.venue][c.start.strftime("%a")].append(c)

page_n = 630
for day in ["Fri", "Sat", "Sun"]:
    for stage in stages:
        daily[stage][day].sort(key=lambda item: item.start)
        for c in daily[stage][day]:
            c.page = page_n
            c.make_page()
            page_n += 1

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
index.append(("Workshops", 780))
index.append(("Now & Next", 606))
index.append(("Thursday films", 619))
index.append(("Friday films", 620))
index.append(("Saturday films", 621))
index.append(("Sunday films", 622))
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

# Workshops
today_n = ["Fri", "Sat", "Sun"].index(now.strftime("%a"))

index = []
pn = 0
for venue, v_name, v_page in workshop_pages:
    for day in ["Friday", "Saturday", "Sunday"]:
        short_day = day[:3]

        index.append((f"Workshop {venue} {day}",
                      501 + pn + i + today_n))

        p = Page(501 + pn)
        line = Line()
        line.start_fg(Color.YELLOW)
        line.start_double_size()
        line.add_text(f"Workshop {venue} {day}")
        p.set_line(2, line)

        line = Line()
        line.start_fg(Color.DEFAULT)
        line.add_text((v_name + " " * 30)[:30])
        line.start_fg(Color.CYAN)
        line.add_text(f"{v_page}")
        p.set_line(4, line)

        line_n = 5

        for item in daily[f"Workshop {venue}"][short_day][:17]:
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

p = Page(500)
line = Line()
line.start_fg(Color.MAGENTA)
line.start_double_size()
line.add_text("Workshops")
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
