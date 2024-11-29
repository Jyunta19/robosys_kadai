#!/usr/bin/env python3
# Copyright (c) 2024 Jyunta Suzuki

import sys
import re
from collections import Counter

def main():
    input_text = sys.stdin.read().strip()
    if not input_text:
        print("No input provided.")
        return

    # 単語のカウント
    words = re.findall(r'\b[a-zA-Z]+\b', input_text.lower())  # 英単語を小文字化
    word_counts = Counter(words)

    # 頻度順に出力
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_counts:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
