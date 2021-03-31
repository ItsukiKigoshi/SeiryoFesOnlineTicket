path = r"db.txt"
obj = open(path ,mode = "r")
data = []
ordata = []

max_num = 12000

#利用状態 : [6:7]
#観劇状態 : [8:9]
#ユーザーネーム : [10:]   (正規表現)



#dbからの読み込み (dataのインデックス番号はチケットの識別番号に同じ)
for a in range(max_num + 1):
    ordata.append(obj.readline())
    data.append("")
    #ordataをlist型に変更してdataに格納
    data[a] = list(ordata[a])




#利用状態の更新
def ren_use(index , state):
    data[index][6:7] = state

#観劇状態の更新
def ren_view(index , state):
    data[index][8:9] = state

#名前の更新
def ren_name(index , name):
    data[index][10:] = name



print("--------------------------------------------------------------------------")




#メインルーチン
for k in range(10000000000):
    
    try:
        inn = input("識別番号 : ")
        inn = int(inn)
        print("")
        print("現在のデータ  : ","".join(data[inn]))
        print("")
    except Exception as e:
        print("有効な番号ではありません")
        print("")
        print("--------------------------------------------------------------------------")
        continue

    try:
        ch = input("変更 (利用 : 1 /  観劇 : 2  /  ユーザーネーム : 3)   /  キャンセル (4)  : ")
        ch = int(ch)
        print("")
        if ch == 1:
            print("")
            inf = input("変更後の利用情報 (y,n) :  ")
            ren_use(inn,inf)
            print("")
            print("ユーザー情報を書き換えました :  ","".join(data[inn]))
            obj = open(path ,mode = "w")
            print("")
        elif ch == 2:
            print("")
            inf = input("変更後の観劇情報 (y,n) :  ")
            ren_view(inn,inf)
            print("")
            print("ユーザー情報を書き換えました :  ","".join(data[inn]))
            obj = open(path ,mode = "w")
            print("")
        elif ch == 3:
            print("")
            inf = input("変更後の名前  :  ")
            inf = inf + "\n"
            ren_name(inn,inf)
            print("")
            print("ユーザー情報を書き換えました :  ","".join(data[inn]))
            obj = open(path ,mode = "w")
            print("")
        elif ch == 4:
            print("")
            obj = open(path,mode = "w")
        else:
            print("")
            obj = open(path,mode = "w")
    except Exception as e:
        print("有効な記述ではありません")
        print("")
        print("--------------------------------------------------------------------------")
        continue

    print("--------------------------------------------------------------------------")

    #db へ変更を保存
    s = ""
    for a in range(max_num + 1):
        s = s + "".join(data[a])
    obj.write(s)
    obj.close()
    

print("".join(data[0]))
