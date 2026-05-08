# Optimization Project Practice

## 概要
本プロジェクトでは、山登り法（Hill Climbing）を用いて2次元関数の最適化を行う。  
異なる初期位置から探索を開始し、各ステップにおける位置や目的関数の値を記録する。  
記録したデータはCSVファイルとして保存し、その収束の様子をグラフとして可視化することで、初期条件の違いによる影響を比較する。

---

## 実行方法

### 山登り法の実行
以下のコマンドを実行することで、異なる初期位置から最適化を行う。

```bash
python3 scripts/run.py settings/config_start_left_top.json
python3 scripts/run.py settings/config_start_right_bottom.json
実行後、results/ フォルダに以下のCSVファイルが生成される。

 start_left_top.csv
 start_right_bottom.csv

これらのCSVファイルには、各反復（iteration）ごとの位置（x, y）や目的関数の値（value）、移動の有無（moved）が記録されている。
以下のコマンドで、実験結果をグラフとして表示・保存する。
python3 scripts/visualize.py
実行後、以下の画像ファイルが生成される。

 results/convergence.png

このグラフでは、横軸を反復回数（iteration）、縦軸を目的関数値（value）とし、
2つの異なる初期位置からの探索結果を同一グラフ上に表示する。
これにより、収束の速さや最終的な値の違いを比較できる。
run.py

設定ファイル（JSON）を読み込み、山登り法による最適化を実行する。
現在位置の周囲に複数の候補点を生成し、その中で最も目的関数値が良い点へ移動する処理を繰り返す。
各ステップの結果はCSVファイルとして保存される。

visualize.py

CSVファイルを読み込み、探索の進行に伴う目的関数値の変化をグラフとして描画する。
2つの異なる初期条件の結果を同一グラフ上に表示し、収束の様子を比較する。