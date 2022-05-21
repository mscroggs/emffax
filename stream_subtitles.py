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
    return out


words1 = []
words2 = []
while True:
    words2 += fake_stream()[::-1]
    while sum([len(i) + 1 for i in words2]) >= 38:
        words1.append(words2[0])
        words2 = words2[1:]
    while sum([len(i) + 1 for i in words1]) >= 38:
        words1 = words1[1:]

    print(" ".join(words1))
    print(" ".join(words2))

    p = Page(888)
    p.set_tagline(None)

    line = Line()
    line.start_bg(Color.DEFAULT)
    line.add_text(" ".join(words1[::-1]))
    p.lines[21] = line

    line = Line()
    line.start_bg(Color.DEFAULT)
    line.add_text(" ".join(words2[::-1]))
    p.lines[22] = line

    p.write_direct(overwrite=True)

    sleep(1)
