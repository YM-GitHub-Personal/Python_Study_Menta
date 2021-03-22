
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
import csv
### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    # csvファイルを指定
    csvFile = 'C:\Virsual Studio Code\MyPython\GitHub_DownLoad\study-01-search-main\search.csv'

    # チェックフラグ
    cheFlg = 0
    # csvファイルオープン
    with open(csvFile, mode = 'r') as r:
        reader = csv.reader(r)
        for row in reader:
            if word == row:
                cheFlg = cheFlg + 1
                print("{}が見つかりました".format(word))
        
        if cheFlg == 0:
            print("{}は見つかりませんでした。".format(word))
            print("{}を追加します".format(word))
            with open(csvFile, mode = 'a') as w:
                writer = csv.DictWriter(w,['no','name'])
                d = {'no':reader.line_num -1, 'name':word}
                writer.writerow(d) 

if __name__ == "__main__":
    search()
