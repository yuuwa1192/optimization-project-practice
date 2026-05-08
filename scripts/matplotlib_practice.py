import pandas as pd
import matplotlib.pyplot as plt

# CSV読み込み
df1 = pd.read_csv("results/start_left_top.csv")
df2 = pd.read_csv("results/start_right_bottom.csv")

# グラフ作成
plt.figure()

# 1本目
plt.plot(df1["iteration"], df1["value"], label="start_left_top", marker="o")

# 2本目
plt.plot(df2["iteration"], df2["value"], label="start_right_bottom", marker="s")

# ラベル（←ここ重要）
plt.xlabel("iteration", fontsize=14)
plt.ylabel("value", fontsize=14)

# タイトル
plt.title("Convergence of Hill Climbing", fontsize=16)

# 目盛りのサイズ
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# 凡例
plt.legend(fontsize=12)

# 保存
plt.savefig("results/convergence.png")

# 表示
plt.show()