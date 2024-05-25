from pyfax import Page, Color, Line
import pytrains
import config


class Station:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.page = None

    def make_page(self):
        p = Page(self.page)
        line = Line()
        line.start_double_size()
        line.add_text("Trains:")
        line.start_fg(Color.YELLOW)
        line.add_text(self.name)
        p.set_line(2, line)

        station = pytrains.Station(self.code)

        line_n = 5
        first = True

        for service in station.services:
            line = Line()
            line.start_fg(Color.YELLOW)
            line.add_text(service.expectedDepartureTime.strftime("%H:%M"))
            line.start_fg(Color.DEFAULT)
            line.add_text((service.destination + " " * 25)[:25])
            line.start_fg(Color.CYAN)
            line.add_text("-" if service.platform is None else service.platform[:5])
            p.set_line(line_n, line)
            line_n += 1

            if first:
                first = False
                line_n = p.add_wrapped_text(line_n, "Calling at: " + ", ".join(
                    [destination.name for destination in service.callingPoints]))
                line_n += 1

            if line_n > 20:
                break

        p.write()


trains = [
    Station(n, c)
    for n, c in [
        ("Ledbury", "LED"),
        ("Euston", "EUS"),
        ("Paddington", "PAD"),
        ("Waterloo", "WAT"),
        ("Banbury", "BAN"),
        ("Birmingham New St", "BHM"),
        ("Durham", "DHM"),
        ("Edinburgh", "EDB"),
        ("King's Cross", "KGX"),
        ("King's Lynn", "KLN"),
        ("Manchester Picc", "MAN"),
        ("Oxford", "OXF"),
        ("Reading", "RDG"),
        ("Stratford-upon-Avon", "SAV"),
    ]
]

trains.sort(key=lambda s: s.name)
for i, t in enumerate(trains):
    t.page = 408 + i
    t.make_page()

p = Page(407)

line = Line()
line.add_text(" " * 31)
line.start_bg(Color.RED)
line.add_block("""
............
...xx.......
....xx......
""", Color.WHITE, None)
p.set_line(1, line)

line = Line()
line.start_fg(Color.CYAN)
line.add_text("Trains")
line.add_text(" " * 24)
line.start_bg(Color.RED)
line.add_block("""
xxxxxxxxx...
...xx.......
..xx........
""", Color.WHITE, None)
p.set_line(2, line)

line = Line()
line.add_text(" " * 31)
line.start_bg(Color.RED)
line.add_block("""
xxxxxxxxx...
..xx........
...xx.......
""", Color.WHITE, None)
p.set_line(3, line)

for i, t in enumerate(trains):
    line = Line()
    line.start_fg(Color.YELLOW)
    line.add_text((t.name + " " * 23)[:23])
    line.start_fg(Color.DEFAULT)
    line.add_text(f"{t.page}")
    if i == 0:
        line.add_text(" " * 3)
        line.add_block(
            "xxxxxxxxxxxxxxxx\n................\n................",
            Color.RED, None)
    p.set_line(4 + i, line)

p.write()
