import numpy as np

from src.objective import objective


class HillClimber:
    """
    山登り法によって目的関数を最小化するクラス
    """

    def __init__(self, config):
        """
        コンストラクタ

        config には，config.json から読み込んだ実験条件が入る
        """

        self.seed = config["seed"]
        self.max_iterations = config["max_iterations"]
        self.initial_x = config["initial_x"]
        self.initial_y = config["initial_y"]
        self.step_size = config["step_size"]
        self.n_neighbors = config["n_neighbors"]

        # 乱数生成器を作成する
        self.rng = np.random.default_rng(self.seed)

        # 現在の位置を初期位置に設定する
        self.current_x = self.initial_x
        self.current_y = self.initial_y
        self.current_value = objective(self.current_x, self.current_y)

        # 実験結果を保存するリスト
        self.history = []

    def generate_neighbor(self):
        """
        現在の位置の近くに，新しい候補点を1つ作成するメソッド
        """

        new_x = self.current_x + self.rng.uniform(-self.step_size, self.step_size)
        new_y = self.current_y + self.rng.uniform(-self.step_size, self.step_size)

        return new_x, new_y

    def record_history(self, iteration, moved):
        """
        現在の探索状態を記録するメソッド
        """

        self.history.append({
            "iteration": iteration,
            "x": self.current_x,
            "y": self.current_y,
            "value": self.current_value,
            "moved": moved
        })

    def step(self):
        """
        山登り法の1回分の処理を行うメソッド
        """

        # 現在の位置を，その時点での最良候補としておく
        best_x = self.current_x
        best_y = self.current_y
        best_value = self.current_value

        # 現在の位置の周辺に候補点を作成する
        for _ in range(self.n_neighbors):
            candidate_x, candidate_y = self.generate_neighbor()
            candidate_value = objective(candidate_x, candidate_y)

            # より良い候補が見つかった場合，最良候補を更新する
            if candidate_value < best_value:
                best_x = candidate_x
                best_y = candidate_y
                best_value = candidate_value

        # 改善する候補が見つかった場合だけ移動する
        if best_value < self.current_value:
            self.current_x = best_x
            self.current_y = best_y
            self.current_value = best_value
            moved = True
        else:
            moved = False

        return moved

    def run(self):
        """
        山登り法を実行するメソッド
        """

        # 初期状態を記録する
        self.record_history(iteration=0, moved=True)

        # 指定された回数だけ探索を行う
        for iteration in range(1, self.max_iterations + 1):
            moved = self.step()
            self.record_history(iteration, moved)

        return self.history