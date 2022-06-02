import config
import os
from enum import Enum

BCHARS = {
    "      ": " ", "x     ": "!", " x    ": "\"", "xx    ": "#", "  x   ": "$",
    "x x   ": "%", " xx   ": "&", "xxx   ": "'", "   x  ": "(", "x  x  ": ")",
    " x x  ": "*", "xx x  ": "+", "  xx  ": ",", "x xx  ": "-", " xxx  ": ".",
    "xxxx  ": "/", "    x ": "0", "x   x ": "1", " x  x ": "2", "xx  x ": "3",
    "  x x ": "4", "x x x ": "5", " xx x ": "6", "xxx x ": "7", "   xx ": "8",
    "x  xx ": "9", " x xx ": ":", "xx xx ": ";",  "  xxx ": "<", "x xxx ": "=",
    " xxxx ": ">", "xxxxx ": "?", "     x": "`", "x    x": "a", " x   x": "b",
    "xx   x": "c", "  x  x": "d", "x x  x": "e", " xx  x": "f", "xxx  x": "g",
    "   x x": "h", "x  x x": "i", " x x x": "j", "xx x x": "k", "  xx x": "l",
    "x xx x": "m", " xxx x": "n", "xxxx x": "o", "    xx": "p", "x   xx": "q",
    " x  xx": "r", "xx  xx": "s", "  x xx": "t", "x x xx": "u", " xx xx": "v",
    "xxx xx": "w", "   xxx": "x", "x  xxx": "y", " x xxx": "z", "xx xxx": "{",
    "  xxxx": "|", "x xxxx": "}", " xxxxx": "~", "xxxxxx": "\x7f",
}


class Color(Enum):
    DEFAULT = 0
    WHITE = 1
    RED = 2
    GREEN = 3
    BLUE = 4
    CYAN = 5
    MAGENTA = 6
    YELLOW = 7
    BLACK = 8


COLCHARS = {
    Color.DEFAULT: "G",
    Color.WHITE: "G",
    Color.RED: "A",
    Color.GREEN: "B",
    Color.BLUE: "D",
    Color.CYAN: "F",
    Color.MAGENTA: "E",
    Color.YELLOW: "C",
}

BLOCKCOLCHARS = {
    Color.DEFAULT: "W",
    Color.WHITE: "W",
    Color.RED: "Q",
    Color.GREEN: "R",
    Color.BLUE: "T",
    Color.CYAN: "V",
    Color.MAGENTA: "U",
    Color.YELLOW: "S",
}


class Page:
    def __init__(self, page_number):
        assert 100 <= page_number < 900
        self.description = None
        self.page_number = page_number
        self.subpage = 1
        self.ps = 8010
        self.lines = {i: None for i in range(1, 26)}
        self.tagline = "EMFFAX: The world at your fingertips"

    def write(self, overwrite=False):
        assert self.page_number != 888
        if not overwrite:
            if os.path.isfile(f"{config.build_dir}/P{self.page_number}.tti"):
                raise RuntimeError(f"Duplicate page: {self.page_number}")
        with open(f"{config.build_dir}/P{self.page_number}.tti", "w") as f:
            f.write(self.to_tti())

    def write_direct(self, overwrite=False):
        if not overwrite:
            if os.path.isfile(f"{config.output_dir}/P{self.page_number}.tti"):
                raise RuntimeError(f"Duplicate page: {self.page_number}")
        with open(f"{config.output_dir}/P{self.page_number}.tti", "w") as f:
            f.write(self.to_tti())

    def to_tti(self):
        if self.tagline is not None:
            tagline = " " * ((35 - len(self.tagline)) // 2) + self.tagline
            tagline += " " * (36 - len(tagline))
            line = Line()
            line.start_bg(Color.BLUE)
            line.start_fg(Color.YELLOW)
            line.add_text(tagline)
            line.start_bg(Color.BLACK)
            self.lines[22] = line

        assert self.page_number is not None
        padded_subpage = f"000{self.subpage}"[-2:]
        out = ""
        out += f"DE,{self.description}\n"
        out += f"PS,{self.ps}\n"
        out += f"PN,{self.page_number}{padded_subpage}\n"
        out += f"SC,00{padded_subpage}\n"
        for i, j in self.lines.items():
            if j is not None:
                out += f"OL,{i},{j}\n"

        return out

    def set_line(self, number, line):
        assert number in self.lines
        # Save space for tagline
        assert number not in [21, 22, 23]
        self.lines[number] = line

    def set_tagline(self, tagline):
        assert tagline is None or len(tagline) <= 36
        self.tagline = tagline

    def add_wrapped_text(self, number, text, double=False, color=Color.DEFAULT):
        words = text.split()
        words = [i if len(i) < 35 else i[:5] + "..." + i[-5:] for i in words]

        if len(words) == 0:
            return number

        line = Line()
        if double:
            line.start_double_size()
            if color != Color.DEFAULT:
                line.start_fg(color)
        else:
            line.start_fg(color)
        while True:
            if len(line) + len(words[0]) + 1 >= 40:
                self.set_line(number, line)
                line = Line()
                if double:
                    line.start_double_size()
                    if color != Color.DEFAULT:
                        line.start_fg(color)
                    number += 2
                else:
                    line.start_fg(color)
                    number += 1
                if number > 20:
                    return number
            if len(line) == 1:
                line.add_text(words[0])
            else:
                line.add_text(" " + words[0])
            words = words[1:]
            if len(words) == 0:
                self.set_line(number, line)
                if double:
                    return number + 2
                else:
                    return number + 1

    def add_block(self, number, block, color, bg=None, indent=0, color_after=Color.WHITE):
        blocks = block.strip("\n").split("\n")
        assert len(blocks) % 3 == 0
        for i in range(0, len(blocks), 3):
            line = Line()
            if bg is not None:
                line.start_bg(bg)
            if indent > 0:
                line.add_text(" " * indent)
            print("\n".join(blocks[i:i+3]), color, color_after)
            line.add_block("\n".join(blocks[i:i+3]), color, color_after)
            self.set_line(number, line)
            number += 1
        return number


class Line:
    def __init__(self):
        self.chars = []

    def __str__(self):
        if len(self.chars) > 40:
            print(f"line is too long ({len(self.chars)} characters, max 40):")
            print(''.join(self.chars))
        assert len(self.chars) <= 40
        return "".join(self.chars)

    def __len__(self):
        return len(self.chars)

    def start_double_size(self):
        self.chars.append("\x1bM")

    def end_double_size(self):
        self.chars.append("\x1bL")

    def start_flashing(self):
        self.chars.append("\x1bH")

    def end_flashing(self):
        self.chars.append("\x1bI")

    def start_fg(self, color, block=False):
        if block:
            self.chars.append("\x1b" + BLOCKCOLCHARS[color])
        else:
            self.chars.append("\x1b" + COLCHARS[color])

    def add_text(self, text):
        self.chars += [i for i in text]

    def add_block(self, block, color, color_after=Color.WHITE):
        block = block.replace(".",    " ")
        blocks = block.strip("\n").split("\n")
        text = ""
        for char in zip(*[b[j::2] for b in blocks for j in range(2)]):
            text += BCHARS["".join(char)]
        self.start_fg(color, True)
        self.add_text(text)
        if color_after is not None:
            self.start_fg(color_after)

    def start_bg(self, color):
        if color in [Color.BLACK, Color.DEFAULT]:
            self.chars.append("\x1b\\")
        else:
            self.start_fg(color)
            self.chars.append("\x1b]")
