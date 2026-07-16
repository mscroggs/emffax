import re
from pyfax import Page, Line, Color
from pyfax.tools.url_helpers import load_rss


def strip_tags(text):
    return re.sub(r"\<[^\>]+\>", "", text)


index = Page(101)
line = Line()
line.start_double_size()
line.add_text("Headlines")
index.set_line(2, line)

emf = load_rss("http://blog.emfcamp.org/rss")["entries"]
ledbury = load_rss("http://www.ledburyreporter.co.uk/news/rss/")["entries"]

pages = []
for i in range(10):
    if i < len(emf):
        pages.append(emf[i])
    if i < len(ledbury):
        pages.append(ledbury[i])

for i, page in enumerate(pages):
    if i < 15:
        line = Line()
        line.add_text((page["title"][:34] + " " * 34)[:34] + " ")
        if i % 2 == 0:
            line.start_fg(Color.YELLOW)
        else:
            line.start_fg(Color.BLUE)
        line.add_text(str(101 + i))
        index.set_line(4 + i, line)

    p = Page(102 + i)
    line = Line()
    line.start_double_size()
    line.start_fg(Color.YELLOW)
    line_n = p.add_wrapped_text(5, page["title"], double=True)
    line_n = p.add_wrapped_text(line_n, strip_tags(page["content"][0]["value"]))
    p.write()

index.write()
