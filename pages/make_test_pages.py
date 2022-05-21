from page_maker import Page, Line, Color

p = Page(899)

line = Line()
line.start_double_size()
line.add_text("Test_page")
p.set_line(2, line)

line = Line()
line.add_text("Foreground colours:")
line.start_fg(Color.RED)
line.add_text("red")
line.start_fg(Color.GREEN)
line.add_text("green")
line.start_fg(Color.BLUE)
line.add_text("blue")

p.write()
