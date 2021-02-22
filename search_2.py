
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
        print("{}が見つかりませんでした".format(word))
        print("{}を追加します".format(word))

        # wordを検索ソースに追加
        source.append(word)

        # 追加した検索ソースの一覧を出力
        print("{}を追加した検索ソースの一覧を出力します".format(word))
        for newsource in source:
            print(newsource)


if __name__ == "__main__":
    search()
