import config
import curses
import locale
import os
from time import sleep

with open(os.path.join(os.path.expanduser('~'), ".EMFFAX_running"), "w") as f:
    f.write("YES")

locale.setlocale(locale.LC_ALL, "")

scr = curses.initscr()

curses.start_color()
curses.use_default_colors()
curses.noecho()
curses.cbreak()
old = curses.curs_set(0)

scr.keypad(1)
scr.refresh()

pos = [0, 0]
dir = [1, 1]

text = f"Press {config.teletext_button} to open EMFFAX"

try:
    while True:
        rows, cols = scr.getmaxyx()
        pos[0] += dir[0]
        pos[1] += dir[1]
        if pos[1] + len(text) >= cols:
            pos[1] = cols - len(text) - 1
            dir[1] = -1
        if pos[1] < 0:
            pos[1] = 1
            dir[1] = 1
        if pos[0] >= rows:
            pos[0] = rows - 2
            dir[0] = -1
        if pos[0] < 0:
            pos[0] = 1
            dir[0] = 1

        scr.clear()
        scr.addstr(*pos, text)
        scr.refresh()

        sleep(0.5)

except BaseException:
    pass

curses.nocbreak()
curses.curs_set(old)
scr.keypad(0)
curses.echo()
curses.endwin()

with open(os.path.join(os.path.expanduser('~'), ".EMFFAX_running"), "w") as f:
    f.write("NO")
