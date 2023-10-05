import streamlit as st

with st.form(key="profile_form"):
    #テキストボックス
    name = st.text_input("名前")
    address = st.text_input("住所")

    #セレクトボックス
    age_category = st.radio(
        '年齢層',
        ('子供（18歳未満）','大人（18歳以上')
    )

    hobby = st.multiselect(
        '趣味',
        ('スポーツ','読書','プログラミング','アニメ')
    )

    #ボタン
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")
    if submit_btn:
        st.text(f"ようこそ{name}さん.{address}へ送付しました")
        st.text(f'{age_category}')
        st.text(f'{", ".join(hobby)}')

