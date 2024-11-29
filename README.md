# robosys_kadai
ロボットシステム学課題用リポジトリ

## 概要
- このプロジェクトは、英語の文章を入力として、各単語の出現頻度を解析し、結果を標準出力に表示するコマンドを実装しています。

- 主な機能は、入力された英語文章から単語を分離し、頻度順に出力することです。

## インストール方法
以下の手順でプロジェクトをインストールしてください。

1. リポジトリをクローンします。
```git clone https://github.com/Jyunta19/robosys_kadai.git```

2. リポジトリディレクトリに移動します。
```cd robosys_kadai```

3. このプロジェクトはPython環境で動作します。

## 使い方
1. コマンドを実行するには、英語のテキストを標準入力で渡してください。
```echo "This is a sample text. This text is only a sample." | python3 word_freq.py```

2. 出力例  
this: 2  
is: 2  
a: 2  
sample: 2  
text: 2  
only: 1

## テスト
1. 以下のコマンドで、動作確認用のテストを実行できます。
```python3 test_word_freq.py```

2. すべてのテストに合格した場合、All tests passed! と表示されます。

## 必要なソフトウェア
- Python
 - テスト済みバージョン: 3.7~3.10

## テスト環境
- Ubuntu 20.04 LTS

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

- © 2024 Jyunta Suzuki
