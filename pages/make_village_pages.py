from page_maker import Page, Line, Color
from tools.url_helpers import load_json

data = load_json("https://www.emfcamp.org/api/villages")

perpage = 17

page_n = 800 + len(data) // perpage

for i in range(len(data) // perpage):
    p = Page(800 + i)
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

        sub_p.add_wrapped_text(6, data[v]["description"])

        sub_p.write()

        page_n += 1

p.write()
