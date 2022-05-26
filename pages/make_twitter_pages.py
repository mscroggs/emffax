from page_maker import Page, Line, Color
import twitter
import config

if config.twitter_access_key is None:
    tweets = []
else:
    t = twitter.Twitter(auth=twitter.OAuth(
        config.twitter_access_key,
        config.twitter_access_secret,
        config.twitter_consumer_key,
        config.twitter_consumer_secret))

    tweets = [i for i in t.search.tweets(q="#emfcamp")["statuses"]
              if not i["text"].startswith("RT @")]

t_n = 0
p_n = 120

b1 = """
.x.x..xxx..x.x..xxx.xxx..xx...x.x..xxx..
xxxxx.x...xxxxx.x...x...x..x.xxxxx.x..x.
.x.x..xx..x.x.x.xx..x...xxxx.x.x.x.xxx..
"""
b2 = """
xxxxx.x...x...x.x...x...x..x.x...x.x....
.x.x..xxx.x...x.x...xxx.x..x.x...x.x....
........................................
"""
for i in range(10):
    p = Page(p_n)

    line = Line()
    line.add_block(b1, Color.CYAN, None)
    p.set_line(2, line)

    line = Line()
    line.add_block(b2, Color.CYAN, None)
    line.start_fg(Color.CYAN)
    line.add_text(f"{i + 1}/10")
    p.set_line(3, line)

    line_n = 4

    while line_n <= 20 and t_n < len(tweets):
        line = Line()
        line.start_fg(Color.CYAN)
        line.add_text("@" + tweets[t_n]["user"]["screen_name"])
        p.set_line(line_n, line)
        line_n += 1
        if line_n <= 20:
            line_n = p.add_wrapped_text(
                line_n, tweets[t_n]["text"].replace("_", "-").replace("#", "_"))
            line_n += 1
        t_n += 1

    p.write()
    p_n += 1

if config.twitter_access_key is None:
    tweets = []
else:
    tweets = t.statuses.user_timeline(screen_name="emfcamp")

t_n = 0
p_n = 130

b1 = """
.xxxx..xxx..x.x..xxx.xxx..xx...x.x..xxx..
x....x.x...xxxxx.x...x...x..x.xxxxx.x..x.
x.xx.x.xx..x.x.x.xx..x...xxxx.x.x.x.xxx..
"""
b2 = """
x.xx.x.x...x...x.x...x...x..x.x...x.x....
x..xx..xxx.x...x.x...xxx.x..x.x...x.x....
.x.......................................
"""
for i in range(10):
    p = Page(p_n)

    line = Line()
    line.add_block(b1, Color.CYAN, None)
    p.set_line(2, line)

    line = Line()
    line.add_block(b2, Color.CYAN, None)
    p.set_line(3, line)

    line_n = 4

    t_n = 0

    while line_n <= 20 and t_n < len(tweets):
        line_n = p.add_wrapped_text(
            line_n, tweets[t_n]["text"].replace("_", "-").replace("#", "_"))
        line_n += 1
        t_n += 1

    p.write()
    p_n += 1
