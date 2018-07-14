
# coding: utf-8

# In[2]:


# マーチンゲール 法


def martingale(target_list_ninki,nanban,losing_streak,total_bet, bet, list_empty, bet_list, initial_bet,target_list_return,race_count,profit,revenue_win,profit_list,stop_losing):
    print("stop_losing",stop_losing)


    race_count=0
    # 過去12レースの結果を仮にサンプルとして、リスト化




    for i in target_list_ninki:
        race_count += 1
        print(race_count,"レース目")

        if i != nanban:

            losing_streak += 1
            print(losing_streak,"連敗")
            total_bet += bet
            print(total_bet,"円損失中")

            if losing_streak == stop_losing:
                print("損切確定！ベット金額を初回額にリセット。")
                print("連敗数もリセット！")
                bet_list.append(total_bet)
                total_bet = 0
                losing_streak = 0
                bet = initial_bet

            else:
                bet = bet*2
                print("ベット金額",bet,"円")



        else:
            print("的中！！！")
            list_empty.append(losing_streak)
            print("連敗数",losing_streak)
            losing_streak = 0

            total_bet += bet
            print("損失累積額",total_bet,"円")
            print(target_list_return)
            print(race_count)
            print("単勝オッズ:",target_list_return[race_count - 1]/100,"倍","×","ベット金額:",bet,"円")

            revenue_win = target_list_return[race_count-1]*bet/100
            print(revenue_win)
            profit = revenue_win -total_bet
            profit_list.append(profit)

            print("的中時利益:",profit)

            bet_list.append(total_bet)

            total_bet = 0
            bet = initial_bet
            print("リセット")

    print(list_empty)
    mx = max(list_empty)
    print("最大連敗数",mx)
    print(bet_list)
    mx_loss =max(bet_list)
    print("最大損失額",mx_loss,"円")

    print("的中時利益：",profit_list)
    print("的中時利益合計:",sum(profit_list))

    print("ベット金額合計:",sum(bet_list))

    return total_bet
    #martingale()


# #
