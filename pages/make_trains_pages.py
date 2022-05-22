from page_maker import Page, Color, Line
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

        if config.open_ldbws_key is None:
            line = Line()
            line.set_color(Color.RED)
            line.add_text("Need an OpenLDBWS key to load train data.")
            p.set_line(4, line)

            p.write()
            return

        from nrewebservices.ldbws import Session

        session = Session(
            "https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2016-02-16",
            config.open_ldbws_key)
        board = session.get_station_board_with_details(
            self.code, rows=14, include_departures=True, include_arrivals=False)

        line_n = 5
        first = True

        for service in board.train_services:
            line = Line()
            line.start_fg(Color.YELLOW)
            line.add_text(service.std)
            line.start_fg(Color.DEFAULT)
            line.add_text((service.destination + " " * 25)[:25])
            line.start_fg(Color.CYAN)
            line.add_text("-" if service.platform is None else service.platform[:5])
            p.set_line(line_n, line)
            line_n += 1

            if first:
                first = False
                line_n = p.add_wrapped_text(line_n, "Calling at: " + ", ".join(
                    [destination.location_name
                     for destination in service.subsequent_calling_points[0].calling_points]))
                line_n += 1

            if line_n > 20:
                break

        p.write()


trains = [
    Station(n, c)
    for n, c in [
        ("Ledbury", "LED"),
        ("Euston", "EUS"),
        ("King's Cross", "KGX"),
        ("St Pancras", "STP"),
        ("Marylebone", "MYB"),
        ("Paddington", "PAD"),
        ("Waterloo", "WAT"),
        ("Banbury", "BAN"),
        ("Basingstoke", "BSK"),
        ("Birmingham New St", "BHM"),
        ("Cambridge", "CBG"),
        ("Durham", "DHM"),
        ("Edinburgh", "EDB"),
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
