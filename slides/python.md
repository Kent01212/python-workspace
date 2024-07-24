---
marp: true
theme: gaia
paginate: true
backgroundColor: #fff
backgroundImage: url('slides/images/5397806.svg')
size: "16:9"

<!-- style -->
<style>
# div.mermaid { all: unset; }
</style>

---

# Python セミナー

神戸電子専門学校 佐藤大輔

---

# Python 使ってますか?

* 2年生でちょこっとだけ触ったPython
* あれでは全然使い物にならない
* 実際の仕事でも使うことあるぞ
* ということでもう少しPythonを学びましょう

---

# 目次(2日分/6時間)

* タプルについて

---

# タプル(Tuple)

* 複数のデータを保持するデータ型
* リストになんとなく似てる
* 静的扱いで不変です

---

# タプル(Tuple)
## tuple/01.py

```Python
tuple = (0,1,2)
print(type(tuple))
```

---

# タプル(Tuple)
## tuple/02.py

```Python
print(tuple[0]) # リスト同様0〜のアクセス
```
普通?に添字アクセスできる

---

# タプル(Tuple)
## tuple/03.py

ただし書き込みはできない

```Python
# 値の書き換え(NG)
tuple[0] = 100
```

微妙な抜け穴はあるけどね

---

# タプル(Tuple)
## tuple/04.py

```Python
print(f"before: {tuple}")
tuple[1].append(100)
print(f"after : {tuple}")
```

タプル内要素にリストがあると、リストの中は可変だったりする

---

# タプル(Tuple)
## tuple/05.py

タプルを利用した多値取得

```Python
# タプルの中身を取り出す
(a, b, c) = tuple
print(c) # -> 2

# いらない所はアンダースコアで受け取ると良い
(a, _, _) = tuple
print(a) # -> 0
```

---

# タプル(Tuple)
## 関数の戻り値とタプル(tuple/06.py)

タプルを用いて多値返却が行われている

```Python
def multi_return():
    return 0, 1, 2

x = multi_return()
print(type(x))  # tuple
print(x)        # (0, 1, 2)
```
* 受け側が単一変数 → タプルのまま受け取る
* 受け側が複数変数 → タプルの要素をそれぞれ受け取る
    * タプルの要素数と合わないとエラーです

---

# タプル(Tuple)
## リストとの違い

* タプルは静的(immutable)、リストは動的(mutable)
    * 前述の例外はあるけどね
* 静的(不変)かつ順序を持つため、同じ値でも順序が違えば別物
    * ここは`set`の問題
* リストに比べると静的なため速い
    * リストは書き換えのためのコストが発生する

---

# Pythonオブジェクト

* Pythonは全てがオブジェクト
* 全ての変数の値はオブジェクトです
    * Python3での話
* 変数はオブジェクトへの参照を持っている
    * そのため、変数の値を変えると参照先のオブジェクトが変わる
    * 組み込み型には同じ値なら同じIDになるものもある
* IDは`id()`で取得可能

---

# Pythonオブジェクト
## IDを見てみる(obj/01.ipynb)

※ サンプルはJupyter Notebookで実行

```Python
# 変数が持つのはオブジェクトのIDです
x = 1
id(x)
```

---

# Pythonオブジェクト
## IDを見てみる(obj/01.ipynb)

あとから同じ値を代入した場合、既存のオブジェクトIDが渡されます

```Python
x = 1
y = 2
print(f"x: {id(x)}, y: {id(y)}") # id(x) != id(y)
y = 1 # 変更するとIDが変わります
print(f"x: {id(x)}, y: {id(y)}") # id(x) == id(y)
```

---

# Pythonオブジェクト
# 同値性の比較(obj/01.ipynb)

各オブジェクトは同値性を比較するためのハッシュ値を持つ
