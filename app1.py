import streamlit as st
from PIL import Image  # 画像を貼り付けるために必要

st.title('Daisukeアプリ')
st.caption('これはDaisukeのstreamlit学習用アプリです')
st.subheader('自己紹介')
st.text('九州工業大学に通っている竹内大輔です。\n'
        '趣味は料理です。よろしくお願いします。')
code = '''
import streamlit as st

st.title(Daisukeアプリ)
'''

st.code(code, language = 'Python')

# 画像
st.text('\n')
st.text('↓推しのペルセウス(モンスターストライクより)')
image = Image.open('ペルセウス4.png') # パス名(相対パス)
st.image(image, width = 700)

with st.form(key='profile'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')
    
    # セレクトボックス
    age_category = st.selectbox(  #st.radio でラジオボタンになる
        '年齢層', #ラベル
        ('未成年(18歳未満)', '大人(18歳以上)')
    )
    
    # 複数選択
    hobby = st.multiselect(
        '趣味',  #ラベル
        ('スポーツ', '読書', 'アニメ', '映画', '釣り', 'プログラミング', '料理')
    )

    # ボタン(ボタンが押されたタイミングでページがリロードされる)
    submit_btn = st.form_submit_button('送信')  #押されている:True, 押されていない:False
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:  # これで submit == Ture と同じ意味
        st.text(f'ようこそ、{name}さん！\n')
        st.text(f'あなたの住所は{address}なんだね、覚えたよ！')
        st.text(f'年齢層: {age_category}')
        st.text(f'趣味: {", ".join(hobby)}')