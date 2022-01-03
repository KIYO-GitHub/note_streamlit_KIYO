import streamlit as st
import sys, os

#パッケージ(ライブラリ)のパス設定：相対参照で使用するためにパスを通す
sys.path.append(os.path.join(os.getcwd(),'01_基礎コード表示'))
sys.path.append(os.path.join(os.getcwd(),'02_株価取得アプリ'))


#各パッケージからモジュールをインポートする
import app1
import app2


# ページ一覧の設定：Streamlitのサイドバーに表示
PAGES = {
    "01_基礎コード表示": app1,
    "02_株価取得アプリ": app2,
}

#選択したページを開く処理：Streamlit main.appの動作設定
st.sidebar.title('アプリの選択')
selection = st.sidebar.radio("アプリ一覧", list(PAGES.keys()))
page = PAGES[selection]
page.app()