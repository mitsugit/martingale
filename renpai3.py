
# coding: utf-8

# In[23]:

def renpai3():

    import pandas as pd
    import openpyxl
    import xlsxwriter
    import numpy as np
    import datetime as dt

    #エクセルファイルの読み込み
    excel = pd.ExcelFile("new2.xlsx")
    #データフレーム 化
    df = excel.parse(sheet_name="matome")

    #着順が１着の行 を抽出し、そこから開催日、レース、人気の列のみを抽出
    new_df = df[(df['着順']==1)].loc[:, ["開催日","レース","人気","オッズ","単勝払戻"]]


    day = new_df['開催日']
    race = new_df['レース']



    #インデックスをリセットし、連番を振り直す
    #http://ailaby.com/reset_index/

    new_df = new_df.reset_index(drop = True)


    # In[28]:


    start_day = input("いつから？")
    start_race = int(input("何レースから？"))
    howmany_race = int(input("何レース分？"))

    #基準行となるレースのindex番号を取得
    start_index = new_df[(new_df["開催日"]== start_day) & (new_df["レース"]== start_race)].index[0]
    print(start_index)

    #最終行のindex番号を取得
    end_index = start_index+ howmany_race
    print(end_index)

    #基準行と最終行のindex番号から、データフレーム の選択範囲を決定し、新たなデータフレーム に代入
    target_dataframe = new_df.iloc[start_index:end_index , :]

    #新たなデータフレーム から.valuesでarrayに変換し、そのarrayをリストに変換する
    target_list_ninki = target_dataframe["人気"].values.tolist()
    target_list_return = target_dataframe["単勝払戻"].values.tolist()

    print(target_list_ninki)
    print(target_list_return)


    # In[29]:


    import math
    import decimal
    import numpy as np
    import importlib

    #past_race = [1,3,2,6,4,3,4,1,1,3,2,3]
    #past_race = target_list_ninki


    initial_bet = int(input("最初のベット金額を入力してください"))
    bet = initial_bet
    total_bet = 0
    bet_list =[]


    nanban = int(input("何番人気について調べますか"))
    stop_losing = int(input("何回連続で負けたらベット金額を初回金額にリセットしますか"))

    losing_streak = 0
    list_empty = []


    losing_total = 0

    losing_streak = 0

    list_empty = []

    curren_list = []

    initial_list = []

    profit_list = []

    race_count = 0
    profit = 0

    revenue_win = 0


    print("ベット方法を選択してください")

    selection = int(input("０：マーチンゲール , 1:逆マーチンゲール ,２：ピラミッド法,3:逆ピラミッド,4:ココモ法"))


    # マーチンゲール 関数の呼び出し

    if selection == 0:

        import martingale_m
        importlib.reload(martingale_m)

        martingale_m.martingale(target_list_ninki,nanban,losing_streak,total_bet, bet,list_empty, bet_list,initial_bet,target_list_return,race_count,profit,revenue_win,profit_list,stop_losing)

     #逆マーチンゲール 関数の呼び出し

    elif selection ==1:

        import re_martingale
        importlib.reload(re_martingale)

        re_martingale.re_martingale(past_race,nanban,losing_streak,total_bet, bet,list_empty, bet_list,initial_bet)

    #ピラミッド関数の呼び出し

    elif selection ==2:

        import pylamid
        importlib.reload(pylamid)

        pylamid.pylamid(past_race,nanban,losing_streak,total_bet, bet,list_empty, bet_list,initial_bet)

    #逆ピラミッド関数の呼び出し

    elif selection ==3:

        import re_pylamid
        importlib.reload(re_pylamid)

        re_pylamid.re_pylamid(past_race,nanban,losing_streak,total_bet, bet,list_empty, bet_list,initial_bet)

    #ココモ関数の呼び出し

    elif selection ==4:

        import cocomo
        importlib.reload(cocomo)

        cocomo.cocomo(past_race,nanban,losing_streak,total_bet, bet,list_empty, bet_list,initial_bet)


    #ウィナーズ投資法

    elif selection ==5:

        import winners
        importlib.reload(winners)

        winners.winners(past_race,nanban,losing_streak,total_bet, bet,list_empty, bet_list,initial_bet,betting_list,losing_total)

    elif selection == 6:

        import MonteCarlo
        importlib.reload(MonteCarlo)

        MonteCarlo.MonteCarlo_3(past_race,nanban,losing_streak,total_bet, bet,list_empty, bet_list,initial_bet,betting_list,losing_total,curren_list,initial_list)
