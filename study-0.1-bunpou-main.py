# Python基本構文の学習用
# この課題は初学者さん用に基礎文法の理解度チェックするためのものです。
# ある程度理解している方は飛ばしてもかまいません。

# １ 変数の使い方
# 変数を使って、「ねずこ」と「ぜんいつ」 は仲間ですとprint文を使って表示させてみよう
# なお、ねずこをname1、ぜんいつをname2として定義してください。
print("{}# １ 変数の使い方-----".format("\n"))
name1 = "ねずこ"
name2 = "ぜんいつ"
print("「{}」と「{}」は仲間です".format(name1,name2))



# ２ if文の使い方
# １のソースを改造して、name2が敵キャラの「むざん」だった場合に
# 仲間ではありませんと表示させてみよう。
print("{}# ２ if文の使い方-----".format("\n"))
if name2 == "むざん":
    print("仲間ではありません")
else:
    print("むざんは敵です。")



# ３ 配列の使い方
# 以下の配列に対して、キャラクター「ぜんいつ」を追加してみよう。 appendを使うことで追加できます。 
print("{}# ３ 配列の使い方-----".format("\n"))
name=["たんじろう","ぎゆう","ねずこ","むざん"]
print("追加前")
print(name)

print("追加後")
name.append("ぜんいつ")
print(name)



# ４ for文の使い方
# ３のソースコードで使用したnameのキャラクターをfor文を使って
# １行に１キャラクター表示してみよう
print("{}# ４ for文の使い方-----".format("\n"))
for rowname in name:
    print(rowname)



# ５　関数の使い方
# 関数を１つ作ってみましょう。
# 関数化したら、関数を呼び出して結果が表示されることを確認してみよう。
print("{}# ５　関数の使い方-----".format("\n"))

def kimetutai():
    muzan = "むざん"
    print(muzan +" は鬼滅隊ではありません")

kimetutai()



# ６ 引数を使う関数の使い方
# 以下のようにhikisuuの部分が引数です。引数は関数の外から変数を関数内に渡すことができます。\n このような引数を使う関数を作成してみよう。

# def test(hikisuu):

# 【仕様】
# 関数名：なんでも良い
# 引数：キャラクターの名前を格納する変数
# 関数で行う処理：キャラクターのリスト（３、４で使ったもの）の中に、
# 引数で入力されたキャラクター名が存在するか確認して結果をprint文で表示させる
# 例）引数が「ぎゆう」→nmaeにぎゆうが存在する→ぎゆうは含まれますと表示
print("{}# ６ 引数を使う関数の使い方-----".format("\n"))

def charNameCheck(hikisuu):
    checkFlg = "False"
    for checkName in name:
        if hikisuu == checkName:
            checkFlg = "Ture"
            print(hikisuu + " は含まれます")
    
    if checkFlg == "False":
        print(hikisuu + " は含まれません")

# 関数呼び出し
charName = "あああ"
charNameCheck(charName)