from enum import Enum

BCHARS = {
    "      ": " ",
    "x     ": "!",
    " x    ": "\"",
    "xx    ": "#",
    "  x   ": "$",
    "x x   ": "%",
    " xx   ": "&",
    "xxx   ": "'",
    "   x  ": "(",
    "x  x  ": ")",
    " x x  ": "*",
    "xx x  ": "+",
    "  xx  ": ",",
    "x xx  ": "-",
    " xxx  ": ".",
    "xxxx  ": "/",
    "    x ": "0",
    "x   x ": "1",
    " x  x ": "2",
    "xx  x ": "3",
    "  x x ": "4",
    "x x x ": "5",
    " xx x ": "6",
    "xxx x ": "7",
    "   xx ": "8",
    "x  xx ": "9",
    " x xx ": ":",
    "xx xx ": ";",
    "  xxx ": "<",
    "x xxx ": "=",
    " xxxx ": ">",
    "xxxxx ": "?",
    "     x": "`",
    "x    x": "a",
    " x   x": "b",
    "xx   x": "c",
    "  x  x": "d",
    "x x  x": "e",
    " xx  x": "f",
    "xxx  x": "g",
    "   x x": "h",
    "x  x x": "i",
    " x x x": "j",
    "xx x x": "k",
    "  xx x": "l",
    "x xx x": "m",
    " xxx x": "n",
    "xxxx x": "o",
    "    xx": "p",
    "x   xx": "q",
    " x  xx": "r",
    "xx  xx": "s",
    "  x xx": "t",
    "x x xx": "u",
    " xx xx": "v",
    "xxx xx": "w",
    "   xxx": "x",
    "x  xxx": "y",
    " x xxx": "z",
    "xx xxx": "{",
    "  xxxx": "|",
    "x xxxx": "}",
    " xxxxx": "~",
    "xxxxxx": "\x7f",
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
    Color.BLUE: "C",
    Color.CYAN: "D",
    Color.MAGENTA: "E",
    Color.YELLOW: "F",
}

BLOCKCOLCHARS = {
    Color.DEFAULT: "W",
    Color.WHITE: "G",
    Color.RED: "Q",
    Color.GREEN: "R",
    Color.BLUE: "S",
    Color.CYAN: "T",
    Color.MAGENTA: "U",
    Color.YELLOW: "V",
}


class Page:
    def __init__(self, page_number):
        self.description = None
        self.page_number = page_number
        self.subpage = 1
        self.ps = 8010
        self.lines = {i: None for i in range(1, 26)}

    def to_tti(self):
        assert self.page_number is not None
        padded_page = f"000{self.page_number}"[-3:]
        padded_subpage = f"000{self.subpage}"[-2:]
        out = ""
        out += f"DE,{self.description}\n"
        out += f"PS,{self.ps}\n"
        out += f"PN,{padded_page}{padded_subpage}\n"
        out += f"SC,00{padded_subpage}\n"
        for i, j in self.lines.items():
            if j is not None:
                out += f"OL,{i},{j}\n"

        return out

    def set_line(self, number, line):
        assert number in self.lines
        self.lines[number] = line


class Line:
    def __init__(self):
        self.chars = []

    def __str__(self):
        assert len(self.chars) <= 40
        return "".join(self.chars)

    def set_color(self, color, block=False):
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
        self.set_color(color, True)
        self.add_text(text)
        if color_after is not None:
            self.set_color(color_after)

    def start_bg(self, color):
        if color == Color.BLACK:
            self.chars.append("\x1b\\")
        else:
            self.set_color(color)
            self.chars.append("\x1b]")
