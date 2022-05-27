# Test Sintesi Vocale
# Brain & Bytes

import pyttsx3
import feedparser

synthesizer = pyttsx3.init()

feed = feedparser.parse("https://www.ansa.it/sito/notizie/tecnologia/tecnologia_rss.xml")

feed_entries = feed.entries

for entry in feed.entries:

    article_title = entry.title
    article_link = entry.link
    article_published_at = entry.published # Unicode string
    article_published_at_parsed = entry.published_parsed # Time object
    content = entry.summary

    print ("{}".format(article_title))

    synthesizer.say(article_title)
    synthesizer.runAndWait()
    synthesizer.stop()
