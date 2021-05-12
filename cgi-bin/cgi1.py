#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
form = cgi.FieldStorage() # cgiオブジェクト作成
v1 = form.getfirst('value1') # nameがvalue1の値を取得
v2 = form.getfirst('mise') # nameがvalue2の値を取得
#入力値が数字ならその積を返す関数
def times(a, b):
    try:
        a=int(a)
        b=int(b)
        return str(a*b)
    except ValueError:
        return('数値じゃないので計算できません(>_<)')

file = None
files = None
a = 0
b = 0
try:
    file = open( str(v2)+".txt","r")
    files = file.readline().split("@")
    a = files[0]
    b = v2
except IOError:
    a = 1
finally:
    if(file):
        file.close()

# ブラウザに戻すHTMLのデータ
print("Content-Type: text/html")
print()
htmlText = '''
<!DOCTYPE html>
<html>
    <head><meta charset="utf-8" />
    <link rel="stylesheet" href="../html/she.css">
    <script src="../html/jab.js"></script>
    </head>
<body>
    <div class="ttle">四高祭をスムーズに！</div>
    <p>店番号：%s</p>
    <p>現在は整理番号&nbsp; %s　番の方がご利用中です<br/></p>
    <hr/>
</body>
</html>
'''%(b,a) # 入力値の積を%sの箇所に埋める
print( htmlText.encode("utf-8", 'ignore').decode('utf-8') )
