import sklearn
import urllib3
from bs4.element import Comment
import urllib.request
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import requests
import threading

ThreadCount = 10


def TF_IDF_Func():
    with open('Dataset/text.txt', 'r') as content_file:
        corpus = content_file.readlines()
    """print(sklearn.feature_extraction.text.CountVectorizer(words_of_sent, encoding='utf-8', lowercase='True',
                                                          preprocessor=None, ngram_range=(1, 2), stop_words='english'))"""
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    X = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(X.toarray())



def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body, filename):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    output = ''
    with open("Dataset/text.txt", "w", encoding="utf-8")as file:
        for t in visible_texts:
            t = t.lower()
            # t = re.sub('[^a-zİıŞşÇçÜüĞğÖö]+', ' ', t)
            output += '{}'.format(t)
            file.write(t + "\n")
    file.close()
    words_of_sent = nltk.word_tokenize(output)
    file1 = open(filename, "w", encoding="ISO-8859-9")

    # tempwords = words_of_sent
    """all_stop = all_stop_words()
    for word in words_of_sent:
        if word not in all_stop and len(word) > 1:
            tempwords.append(word)

    tempwords = lemmatizing(tempwords)"""
    for word in words_of_sent:
        file1.write(word + ' ')
    file1.close()

    # TF_IDF_Func()


def url2text(url, filename):
    try:
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        urllib3.disable_warnings()
        retVal = requests.get(url, verify=False, timeout=3)
        if retVal.status_code == 200:
            print(url)
            html = urllib.request.urlopen(req).read()
            text_from_html(html, filename)
    except:
        return



def URL_Extract():
    df = pd.read_csv("Filtered.csv")
    saved_url = df['url']
    saved_category = df['main_category']

    index = 0
    with open("INFO.txt", "w", encoding="utf-8") as file:
        while index < (saved_url.__len__()):
            if saved_category[index] != 'Not_working':
                file.write(saved_category[index] + ' ' + saved_url[index] + '\n')
            index += 1
    file.close()


def URL_Contents(number):
    with open("INFO.txt", "r", encoding="utf-8")as file:
        content = file.read()
        content = content.split()
    file.close()

    number *= 2

    while number < len(content) / 2:
        if content[number] == 'Adult':
            filename = "URL/Adult/" + content[number + 1] + ".txt"
            content[number + 1] = "http://www." + content[number + 1]
            url2text(content[number + 1], filename)
            number += (ThreadCount * 2)
        elif content[number] == "Bandwidth":
            filename = "URL/Bandwidth/" + content[number + 1] + ".txt"
            content[number + 1] = "http://www." + content[number + 1]
            url2text(content[number + 1], filename)
            number += (ThreadCount * 2)
        elif content[number] == "Business":
            filename = "URL/Business/" + content[number + 1] + ".txt"
            content[number + 1] = "http://www." + content[number + 1]
            url2text(content[number + 1], filename)
            number += (ThreadCount * 2)
        elif content[number] == "Personal":
            filename = "URL/Personal/" + content[number + 1] + ".txt"
            content[number + 1] = "http://www." + content[number + 1]
            url2text(content[number + 1], filename)
            number += (ThreadCount * 2)
        else:
            number += (ThreadCount * 2)


URL_Extract()
# URL_Contents()

thread_list = []
for i in range(ThreadCount):
    thread = threading.Thread(target=URL_Contents, args=(i,))
    thread_list.append(thread)
    thread.start()



"""def URL_Contents(number):
    with open("INFO.txt", "r", encoding="utf-8")as file:
        content = file.read()
        content = content.split()
    file.close()

    number *= 2
    cats = set('Adult', 'Bandwidth', 'Business', 'Personal')

    while i < len(content) / 2:
        cat = columns[i]
        if cat in cats:
            domain = columns[i+1]
            txt_file = "URL/{}/{}.txt".format(cat, domain)
            url = "http://www." + domain
            url2text(url, txt_file)
            i += (ThreadCount * 2)"""