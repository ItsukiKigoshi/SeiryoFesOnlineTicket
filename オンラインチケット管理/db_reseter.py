conf = input("データベースを初期化してもよろしいですか (y : はい)  : ")
if conf == "y":
    path = r"db.txt"
    obj = open(path ,mode = "w",encoding = "utf-8")
    #最大人数
    max_num = 12000


    #db へ変更を保存
    s = ""
    for a in range(max_num + 1):
        a = str(a)
        s = s + a.zfill(5) + "/n/n/\n"

    obj.write(s)
    obj.close()
