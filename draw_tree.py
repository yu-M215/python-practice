#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# turtleの機能を読み込む
from turtle import *

# 木を描く関数
def tree(length):
    if length > 5:
        forward(length)
        right(20)
        tree(length-15)
        left(40)
        tree(length-15)
        right(20)
        backward(length)

# カーソルの色を緑色にする
color("green")

# 左に90度回転させて上を向かせる
left(90)

# 下に下げる
backward(150)

# 定義した木を描く関数を呼び出す
tree(120)

# 描画終了後の入力待ち
input('type to exit')
