from page_maker import Page, Line, Color
from tools.url_helpers import load_rss

index = Page(101)
line = Line()
line.start_double_size()
line.add_text("News index")
index.set_line(2, line)

for i, (feed, title, tagline) in enumerate([
    ("http://feeds.bbci.co.uk/news/rss.xml?edition=uk", "Top Stories", "From BBC News"),
    ("http://feeds.bbci.co.uk/news/technology/rss.xml?edition=uk", "Technology", "From BBC News"),
    ("http://feeds.bbci.co.uk/news/business/rss.xml?edition=uk", "Business", "From BBC News"),
    ("http://www.ledburyreporter.co.uk/news/rss/", "Local News", "From Ledbury Reporter"),
    ("http://feeds.bbci.co.uk/news/science_and_environment/rss.xml?edition=uk",
     "Science", "From BBC News"),
    ("http://feeds.bbci.co.uk/news/politics/rss.xml?edition=uk", "Politics", "From BBC News"),
    ("http://feeds.bbci.co.uk/news/education/rss.xml?edition=uk", "Education", "From BBC News"),
    ("https://www.theguardian.com/uk/rss", "The Guardian", None),
    ("http://www.independent.co.uk/news/rss", "The Independent", None),
    ("http://www.telegraph.co.uk/newsfeed/rss/news_breaking.xml", "The Telegraph", None),
    ("http://blog.emfcamp.org/rss", "emfcamp.org", None),
    ("http://www.metoffice.gov.uk/public/data/PWSCache/WarningsRSS/Region/UK",
     "Weather warnings", "From the Met Office"),
    ("http://www.dailymail.co.uk/tvshowbiz/index.rss", "Showbiz", "From The Daily Mail"),
]):

    line = Line()
    line.start_fg(Color.DEFAULT)
    line.add_text((title + " " * 30)[:30])
    line.start_fg(Color.YELLOW)
    line.add_text(f"{102 + i}")
    index.set_line(4 + i, line)

    p = Page(102 + i)
    if tagline is not None:
        p.set_tagline(tagline)
    line = Line()
    line.start_double_size()
    line.add_text(title)
    p.set_line(2, line)

    data = load_rss(feed)

    line_n = 5
    gap = 2
    title = data["entries"]
    for item in data["entries"]:
        line = Line()
        if line_n == 5:
            line.start_double_size()
        title = item["title"][:37]
        while line_n <= 20 and len(title) > 0:
            line.add_text(title[:37])
            title = title[37:]
            p.set_line(line_n, line)
            line_n += gap
        line_n += gap + 1
        gap = 1
        if line_n > 20:
            break

    p.write()

index.write()
