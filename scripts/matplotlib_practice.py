import matplotlib.pyplot as plt

# x軸
x = [0, 1, 2, 3, 4]

# データ2種類
y1 = [10, 8, 6, 5, 3]
y2 = [3, 4, 6, 8, 11]

# 1本目
plt.plot(x, y1, label="Data1", marker="o")

# 2本目
plt.plot(x, y2, label="Data2", marker="s")

# ラベル
plt.xlabel("x")
plt.ylabel("y")

# タイトル
plt.title("Two Lines Plot")

# 凡例（超重要）
plt.legend()

# 保存
plt.savefig("results/practice_plot.png")

# 表示
plt.show()