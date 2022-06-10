from pyfax import Page, Line, Color
from pyfax.tools.url_helpers import load_json

data = load_json("https://emffilms.org/api/2022/schedule")

films = {"Thursday": [], "Friday": [], "Saturday": [], "Sunday": []}

for film in data["films"]:
    films[film["showing"]["day"]].append(film)

for i, (day, films) in enumerate(films.items()):
    p = Page(619 + i)
    line = Line()
    line.start_double_size()
    line.add_text(f"{day} films")
    p.set_line(2, line)
    n = 5
    for film in films:
        line = Line()
        line.start_fg(Color.CYAN)
        line.add_text(film['showing']['text'].split(' ')[-1])
        line.start_fg(Color.DEFAULT)
        line.add_text(f"{film['title'][:22]} ({film['year']})")
        c = film['certificate']
        if c in ["U", "Uc"]:
            line.start_fg(Color.GREEN)
        elif c == "PG":
            line.start_fg(Color.YELLOW)
        elif c in ["12", "12A"]:
            line.start_fg(Color.MAGENTA)
        elif c == "15":
            line.start_fg(Color.RED)
        elif c == "18":
            line.start_fg(Color.CYAN)
        elif c == "Unrated":
            line.start_fg(Color.DEFAULT)
        else:
            raise ValueError(f"Unknown certificate: {c}")
        line.add_text(c[:3])
        p.set_line(n, line)
        n += 1

        n = p.add_wrapped_text(n, film['precis']['oneLine'])
        n += 1
    p.write()
