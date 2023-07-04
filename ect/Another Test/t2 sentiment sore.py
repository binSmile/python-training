
def getSentimentScore(topic):
    import urllib.request
    contents = urllib.request.urlopen("https://en.wikipedia.org/w/api.php?action=parse&prop=text&format=json&page=%s" % topic).read()
    import  json
    import re
    page = json.loads(contents)
    html_text = page["parse"]["text"]["*"]
    plain_text = re.sub('<[^<]+?>', '', html_text).lower()
    edge = -1 #plain_text.find('\nreferences[edit]\n')
    words = re.findall(r'[a-zA-Z]+(?:-[a-zA-Z]+)*', plain_text[:edge])
    word_counts = {
        "worst": words.count("worst"),
        "bad": words.count("bad"),
        "good": words.count("good"),
        "best": words.count("best"),
    }
    sentiment_score = (-3) * word_counts["worst"] - word_counts["bad"] + word_counts["good"] + 3 * word_counts["best"]
    return sentiment_score

if __name__ == '__main__':
    topic = 'pizza'

    result = getSentimentScore(topic)

    print(str(result))