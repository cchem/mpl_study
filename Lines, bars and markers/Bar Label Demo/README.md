# Bar Label Demo

積み上げ棒グラフを作成するax.barについて学んだ。

## ポイント

---

plt.subplotの引数は必須ではない。

```python
plt.subplot()
```

のように、引数なしで実行すると1,1のグラフが作成される。

---

bar_labelを実行すると棒グラフ上に数値を表示できる。  
その際、積み上げ棒グラフの特定の部分の数値のみを表示したいときは

```python
ax.bar_label(bar_object, label_type='center')
```

積み上げた全体の数値を表示したいときは、

```python
ax.bar_label(bar_object, label_type='edge')
```

とする。(edgeはデフォルト値なので省略可)

---

横向き棒グラフを利用するときはy軸の値の小さい方からリストが並べられるため、  
直感的にわかりやすい「上から下にリストが並ぶ」ということにならない。  
この対応として、

```python
ax.invert_yaxis()
```

を使う。

---
ax.bar_labelの仕様として、labelを与えなかった場合は棒グラフの値を読んでよしなにラベルが付与される。
label引数にテキストを与えると、そのテキストを使ってラベルが描画される。
```python
ax.bar_label(bar_object, label=['hoge' for _ in range(n)])
```

---

## Picture

<p align="center">
  <img src="main.png" alt="main.png">
</p>

<p align="center">
  <img src="main2.png" alt="main2.png">
</p>

<p align="center">
  <img src="main3.png" alt="main3.png">
</p>

# URL
[https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html](https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html)
