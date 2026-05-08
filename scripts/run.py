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

    # 🔴 引数チェック（これが今回の重要修正）
    if len(sys.argv) < 2:
        print("設定ファイルを指定してください")
        print("例: python3 scripts/run.py settings/config_start_left_top.json")
        sys.exit()

    # 🔴 コマンドライン引数から設定ファイル取得
    config_path = PROJECT_ROOT / sys.argv[1]

    # 設定ファイルを読み込む
    config = load_config(config_path)

    # 山登り法のインスタンスを作成
    optimizer = HillClimber(config)

    # 実行
    history = optimizer.run()

    # DataFrameに変換
    df = pd.DataFrame(history)

    # 出力先フォルダ
    output_directory = PROJECT_ROOT / config["output_directory"]
    output_directory.mkdir(exist_ok=True)

    # 🔴 ファイル名はconfigごとに変わる（ここ重要）
    output_path = output_directory / f"{config['experiment_name']}.csv"

    # 保存
    df.to_csv(output_path, index=False)

    print("実験が完了しました．")
    print(f"結果を {output_path} に保存しました．")


if __name__ == "__main__":
    main()