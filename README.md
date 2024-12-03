# robosys_kadai
ロボットシステム学課題用リポジトリ

## 概要
- このプロジェクトは、英語の文章を入力として、各単語の出現頻度を解析し、結果を標準出力に表示するコマンドを実装しています。

- 主な機能は、入力された英語文章から単語を分離し、頻度順に出力することです。

## 使い方
1. リポジトリをクローンします。
```
git clone https://github.com/Jyunta19/robosys_kadai.git
```

2. リポジトリディレクトリに移動します。
```
cd robosys_kadai
```

3. 英語のテキストを入力し、 コマンドを実行します。
```
echo "This is a sample text. This text is only a sample." | ./word_freq
```

4. 以下が出力例です。  
```
this: 2  
is: 2  
a: 2  
sample: 2  
text: 2  
only: 1
```

## テスト
1. 以下のコマンドで、動作確認用のテストを実行できます。  
```
./test_word_freq
```

2. すべてのテストに合格した場合、All tests passed! と表示されます。

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7~3.10

## テスト環境
- Ubuntu 20.04 LTS

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

- このパッケージのコードの一部は，（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
  - https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024

- © 2024 Jyunta Suzuki
