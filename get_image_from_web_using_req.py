# import requests
#
# url = "https://images.pexels.com/photos/14730090/pexels-photo-14730090.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
#
# response = requests.get(url)
# content = response.content
#
# with open('image.jpeg', 'wb') as file:
#     file.write(content)

import streamlit as st

import requests

# api_key = "lnpKN2BsBrmoZylVblf0bczl4IWaL7efjeKJrisQ"

url = "https://api.nasa.gov/planetary/apod?api_key=lnpKN2BsBrmoZylVblf0bczl4IWaL7efjeKJrisQ"


response = requests.get(url)
content = response.json()
print(content)

st.header(content['title'])


image_url = content['url']
request = requests.get(image_url)
pic = request.content
with open('image.jpg', 'wb') as file:
    file.write(pic)


st.image('image.jpg')

st.write(content['explanation'])

