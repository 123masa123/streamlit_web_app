import streamlit as st
from PIL import Image

st.title("サブーアプリ")
st.caption("これはさぶーの動画用のテストアプリです")

    #画像
image = Image.open("./data/FireShot Capture 005 - 東三河 デジタル イノベーターズ 2023 参加申込みフォーム - forms.office.com.png")
st.image(image,width=200)