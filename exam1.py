

### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# # 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# ### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

# inメソッドでsourceの中にwordが無いかどうか確認
    if word in source:
#wordを{}の中に書き込むと同時にprintさせる
        print("{}が見つかりました".format(word))

#sourceに無い場合の処理。sourceに無かったことと、appendでリストに追加処理。
    else:
        print("{}は見つかりませんでした".format(word))
        source.append(word)
    
if __name__ == "__main__":
    search()



import csv
#ファイルの読み込み
# csvファイルがあるパスを指定
csv_path="C:/Users/Yoshi/project/source.csv"

# csvファイルを開くとともに、encodeエラーを防止。変数fに代入
with open(csv_path,encoding="utf-8") as f :

# csvリーダで代数fで開く
    csv.reader(f)

# fに格納されているオブジェクトを１つずつ取り出してprint
    for row in csv.reader(f):
        print(row)

# ファイルの書き込み
# 書き込みたいcsvファイルパスおよびファイル名を指定
csv_path="C:/Users/Yoshi/project/source_write.csv"
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

#パス名を指定して開く。文字化け防止。fとして保存
with open(csv_path,mode="w",encoding="utf=8") as f:
#fをwrite目的で開き、要素ごとに,で区切る。
    f.write(','.join(source))
