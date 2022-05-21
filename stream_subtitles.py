import lorem
import random
from time import sleep
from page_maker import Page, Line, Color

next = []


def fake_stream():
    global next
    if len(next) == 0:
        next = lorem.sentence().split()

    n = random.randrange(1, 4)
    out = next[:n]
    next = next[n:]
    return " ".join(out)


lines = []
words1 = []
words2 = []
while True:
    words = fake_stream()
    if len(lines[-1]) + 1 + len(words) < 38:
        lines[-1] += words
    else:
        lines.append(words)
        lines = [-5:]

    p = Page(888)
    p.set_tagline(None)

    for i, j in enumerate(lines[::-1]):
        line = Line()
        line.start_fg(Color.DEFAULT)
        line.add_text(j)
        p.lines[22-i] = line

    p.write_direct(overwrite=True)

    sleep(1)
