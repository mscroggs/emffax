import json
import requests
import feedparser


def load_rss(url):
    return feedparser.parse(url)


def load_json(url, headers={}, cookies={}):
    feed = load(url, headers, cookies)
    return json.loads(feed)


def load_csv(url, headers={}, cookies={}):
    feed = load(url, headers, cookies)
    return [i.split(",") for i in feed.split("\n")]


def load(url, headers={}, cookies={}):
    headers["User-Agent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/50.0.2661.102 Safari/537.36")
    out = requests.get(url, headers=headers, cookies=cookies).text
    try:
        return out.decode('utf-8')
    except:  # noqa: E722
        return out
