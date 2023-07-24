import requests
import streamlit as st
import send_email

from send_email import send_mail

# to get api key we need to login to newsapi

topic = "tesla"
api_key = "15d1007f03544568b67c443eea982b35"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}" \
      "&from=2023-05-24" \
      "&sortBy=publishedAt" \
      f"&apiKey={api_key}"

req = requests.get(url)
content = req.json()
print(content)
print(content["articles"])

col1,col2 = st.columns(2)


for index, article in enumerate(content["articles"])[:20]:
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
    if article["title"] is not None:
        body = "Subject: Tesla News" + "\n"\
               + body + article["title"] + "\n"\
               + article["description"]\
               + article["url"] + "\n"\
               + 2*"\n"


body = body.encode('utf-8')

send_email.send_mail(message= body)



