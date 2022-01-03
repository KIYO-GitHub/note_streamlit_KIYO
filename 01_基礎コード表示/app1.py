import streamlit as st
import pandas as pd

def app():
    with st.echo():
        st.title('タイトル基礎コード表示')
        st.write('app1.pyの内容を記載します。')
    
    
    st.markdown('***') #マークダウン記法での区切り線    
    with st.echo():
        st.markdown('''
        st.markdown("文字列")で文字列を表示できます。markdownでは数式やリンク等が簡単に作成できます。  
        $$\\frac{x-a}{b}$$
        ''')
        st.markdown('[KIYOのnoteリンク](https://note.com/kiyo_ai_note/magazines)')

    
    st.markdown('***') #マークダウン記法での区切り線 
    with st.echo():
        url = 'https://info.finance.yahoo.co.jp/ranking'
        df_stocktable = pd.read_html(url)[0] #yahoo証券のランキングを取得
        if st.checkbox('株価テーブル(動的)を表示します。'):
            st.dataframe(df_stocktable)
        if st.button('株価テーブル(静的)を表示します。'):
            st.table(df_stocktable)
            
    st.markdown('***') #マークダウン記法での区切り線 
    with st.echo():
        stockmarket = list(df_stocktable['市場'].value_counts().index) #yahoo証券ランキングリストから市場リストを作成
        st.selectbox('セレクトボックスで選択できます。', stockmarket)
        st.multiselect('複数の選択肢を選択できます。', stockmarket, default=stockmarket)


    st.markdown('***') #マークダウン記法での区切り線 
    with st.echo():
        imgfile = st.file_uploader('ここに画像ファイル(JPEG, PNG)をアップロードしてください。') #ファイルがないときはNoneが返る
        if imgfile != None: #そのままだとエラーになるためif分で処理
            st.image(imgfile, width=300) #imgfile=Noneだとエラーになる
            
        csv_financde = df_stocktable.to_csv().encode('utf-8')
        st.download_button(
            label='CSVダウンロード',
            data=csv_financde,
            file_name='Yahoo株価ランキング.csv',
            mime='text/csv'
        )
             