import json
import sys
from pathlib import Path

import pandas as pd

# プロジェクト直下のパスを取得する
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# src フォルダを読み込めるようにする
sys.path.append(str(PROJECT_ROOT))

from src.optimizer import HillClimber


def load_config(config_path):
    """
    JSON形式の設定ファイルを読み込む関数
    """

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    return config


def main():
    """
    最適化実験を実行するメイン処理
    """

    # 設定ファイルのパス
    config_path = PROJECT_ROOT / "settings" / "config.json"

    # 設定ファイルを読み込む
    config = load_config(config_path)

    # 山登り法のインスタンスを作成する
    optimizer = HillClimber(config)

    # 山登り法を実行する
    history = optimizer.run()

    # 実験結果をDataFrameに変換する
    df = pd.DataFrame(history)

    # 出力先フォルダ
    output_directory = PROJECT_ROOT / config["output_directory"]

    # 出力先フォルダが存在しない場合は作成する
    output_directory.mkdir(exist_ok=True)

    # 実験名を使ってCSVファイル名を作成する
    output_path = output_directory / f"{config['experiment_name']}.csv"

    # CSVファイルとして保存する
    df.to_csv(output_path, index=False)

    print("実験が完了しました．")
    print(f"結果を {output_path} に保存しました．")


if __name__ == "__main__":
    main()