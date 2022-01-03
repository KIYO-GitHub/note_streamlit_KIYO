import streamlit as st
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import mplfinance as mpf
import japanize_matplotlib


def app():
    with st.echo():
        st.title('App2：Pythonでやってみた２:株価取得/可視化')
        st.markdown('[KIYOのnote記事リンク](https://note.com/kiyo_ai_note/n/n84ed4055f5ad)')
        
    st.markdown('***') #マークダウン記法での区切り線    
    with st.echo():
        @st.cache
        def getstockprice(stockcode):
            return pdr.data.DataReader(stockcode, 'stooq')
        
        stocknum = st.text_input('株価取得：銘柄コードを4桁を入力してください。(初期値：7203(Toyota))', value='7203')
        df = getstockprice(f'{stocknum}.jp')
        st.dataframe(df)
        
    st.markdown('***') #マークダウン記法での区切り線    
    with st.echo():
        japanize_matplotlib.japanize() 
        st.line_chart(df['Close'])
        
        df_sorted = df.sort_index() #Dateが降順のため昇順に修正
        fig, ax = plt.subplots()
        df['Close'].plot(label='東京機械製作所')
        df['Close'].rolling(5).mean().plot(label='5日移動平均', linestyle='dashed')
        df['Close'].rolling(25).mean().plot(label='25日移動平均', linestyle='dashed')
        df['Close'].rolling(75).mean().plot(label='75日移動平均', linestyle='dashed')
        plt.legend()
        plt.grid()
        st.pyplot(fig)
        
    st.markdown('***') #マークダウン記法での区切り線    
    with st.echo():
        st.set_option('deprecation.showPyplotGlobalUse', False) #pyplotのグローバル変数を使用しない
        df_sorted = df.sort_index() #Dateが降順のため昇順に修正
        fig = mpf.plot(df_sorted ,type='candle', figratio=(10,5), mav=(5, 25, 75), volume=True, style='yahoo') #Volume=TrueはVolumeカラムが必須
        st.pyplot(fig)