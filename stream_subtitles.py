import asyncio
import websockets
from pyfax import Page, Line, Color

lines = ["[awaiting subtitles]"]


async def hello():
    global lines
    async with websockets.connect("wss://stagetext.emfcamp.app/socket/a", ssl=True) as w:
        line = await w.recv()
    print(line)
    words = line.split()
    for w in words:
        if len(lines) == 0:
            lines.append(w)
        if len(lines[-1]) + 1 + len(w) < 38:
            lines[-1] += " " + w
        else:
            lines.append(w)
            lines = lines[-10:]

    write_subtitles()


def write_subtitles():
    try:
        p = Page(888)
        p.set_tagline(None)

        for i, j in enumerate(lines[::-1]):
            line = Line()
            line.start_fg(Color.DEFAULT)
            line.add_text(j)
            p.lines[22-i] = line

        p.write_direct(overwrite=True)
    except:  # noqa: E722
        pass


write_subtitles()
while True:
    asyncio.get_event_loop().run_until_complete(hello())
    print("updated")
