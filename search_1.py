
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    findflg = "False"
    for sourceName in source:
        if sourceName == word:
            print("{}が見つかりした".format(word))
            findflg = "Ture"
    if findflg == "False":
        print("{}が見つかりません".format(word))

if __name__ == "__main__":
    search()
