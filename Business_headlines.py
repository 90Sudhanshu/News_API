import requests
import streamlit as st
import send_email


api_key = "15d1007f03544568b67c443eea982b35"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-24&sortBy=publishedAt&apiKey=15d1007f03544568b67c443eea982b35"

req = requests.get(url)
content = req.json()
print(content["articles"])

col1,col2 = st.columns(2)

for index, article in enumerate(content["articles"]):
    print(f'{index} {article["title"]}')
    print(article["description"])
    # print(article["urlToImage"])

    if index % 2 == 0:
        column = col1
    else:
        column = col2

    column.header(index+1)
    column.header(article["title"])
    column.subheader(article["description"])
    # column.image(article['urlToImage'])

body = ""

for article in content["articles"]:

        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode('utf-8')
send_email.send_mail(message= body)
