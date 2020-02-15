#!/home/prilog/.pyenv/versions/3.6.9/bin/python
# -*- coding: utf-8 -*-

# キャラクターレベル 2020/01/17現在
LEVEL = 154

# キャラクター名一覧(mask)
characters_name_mask = [
    "アオイ",
    "アオイ(編入生)",
    "アカリ",
    "アキノ",
    "アヤネ",
    "アヤネ(クリスマス)",
    "アユミ",
    "アリサ",
    "アン",
    "アンナ",
    "イオ",
    "イオ(☆6以降)",
    "イオ(サマー)",
    "イリヤ",
    "イリヤ(クリスマス)",
    "エミリア",
    "エリコ",
    "エリコ(バレンタイン)",
    "カオリ",
    "カオリ(サマー)",
    "カスミ",
    "カスミ(マジカル)",
    "カヤ",
    "キャル",
    "キャル(☆6以降)",
    "キャル(サマー)",
    "キャル(ニューイヤー)",
    "キョウカ",
    "キョウカ(ハロウィン)",
    "クウカ",
    "クウカ(オーエド)",
    "クリスティーナ",
    "クリスティーナ(クリスマス)",
    "クルミ",
    "クルミ(クリスマス)",
    "グレア",
    "クロエ",
    "コッコロ",
    "コッコロ(☆6以降)",
    "コッコロ(サマー)",
    "コッコロ(ニューイヤー)",
    "サレン",
    "サレン(サマー)",
    "ジータ",
    "シオリ",
    "シオリ(マジカル)",
    "シズル",
    "シズル(バレンタイン)",
    "シノブ",
    "シノブ(ハロウィン)",
    "ジュン",
    "スズナ",
    "スズナ(サマー)",
    "スズメ",
    "スズメ(サマー)",
    "スズメ(ニューイヤー)",
    "タマキ",
    "タマキ(サマー)",
    "チカ",
    "チカ(クリスマス)",
    "ツムギ",
    "トモ",
    "ナナカ",
    "ニノン",
    "ニノン(オーエド)",
    "ネネカ",
    "ノゾミ",
    "ノゾミ(クリスマス)",
    "ハツネ",
    "ヒヨリ",
    "ヒヨリ(ニューイヤー)",
    "ペコリーヌ",
    "ペコリーヌ(☆6以降)",
    "ペコリーヌ(サマー)",
    "ペコリーヌ(プリンセス)",
    "マコト",
    "マコト(サマー)",
    "マツリ",
    "マヒル",
    "マホ",
    "マホ(☆6以降)",
    "マホ(サマー)",
    "ミサキ",
    "ミサキ(ハロウィン)",
    "ミサト",
    "ミソギ",
    "ミソギ(ハロウィン)",
    "ミツキ",
    "ミフユ",
    "ミフユ(サマー)",
    "ミミ",
    "ミミ(ハロウィン)",
    "ミヤコ",
    "ミヤコ(ハロウィン)",
    "ムイミ",
    "モニカ",
    "ユイ",
    "ユイ(ニューイヤー)",
    "ユカリ",
    "ユカリ(☆6以降)",
    "ユキ",
    "ヨリ",
    "ラム",
    "リノ",
    "リノ(☆6以降)",
    "リマ",
    "リマ(☆6以降)",
    "リン",
    "ルゥ",
    "ルカ",
    "ルナ",
    "レイ",
    "レイ(ニューイヤー)",
    "レム",
]

# キャラクター名一覧
characters_name = [
    "アオイ",
    "アオイ(編入生)",
    "アカリ",
    "アキノ",
    "アヤネ",
    "アヤネ(クリスマス)",
    "アユミ",
    "アリサ",
    "アン",
    "アンナ",
    "イオ",
    "イオ",      # ☆6以降
    "イオ(サマー)",
    "イリヤ",
    "イリヤ(クリスマス)",
    "エミリア",
    "エリコ",
    "エリコ(バレンタイン)",
    "カオリ",
    "カオリ(サマー)",
    "カスミ",
    "カスミ(マジカル)",
    "カヤ",
    "キャル",
    "キャル",      # ☆6以降
    "キャル(サマー)",
    "キャル(ニューイヤー)",
    "キョウカ",
    "キョウカ(ハロウィン)",
    "クウカ",
    "クウカ(オーエド)",
    "クリスティーナ",
    "クリスティーナ(クリスマス)",
    "クルミ",
    "クルミ(クリスマス)",
    "グレア",
    "クロエ",
    "コッコロ",
    "コッコロ",      # ☆6以降
    "コッコロ(サマー)",
    "コッコロ(ニューイヤー)",
    "サレン",
    "サレン(サマー)",
    "ジータ",
    "シオリ",
    "シオリ(マジカル)",
    "シズル",
    "シズル(バレンタイン)",
    "シノブ",
    "シノブ(ハロウィン)",
    "ジュン",
    "スズナ",
    "スズナ(サマー)",
    "スズメ",
    "スズメ(サマー)",
    "スズメ(ニューイヤー)",
    "タマキ",
    "タマキ(サマー)",
    "チカ",
    "チカ(クリスマス)",
    "ツムギ",
    "トモ",
    "ナナカ",
    "ニノン",
    "ニノン(オーエド)",
    "ネネカ",
    "ノゾミ",
    "ノゾミ(クリスマス)",
    "ハツネ",
    "ヒヨリ",
    "ヒヨリ(ニューイヤー)",
    "ペコリーヌ",
    "ペコリーヌ",      # ☆6以降
    "ペコリーヌ(サマー)",
    "ペコリーヌ(プリンセス)",
    "マコト",
    "マコト(サマー)",
    "マツリ",
    "マヒル",
    "マホ",
    "マホ",      # ☆6以降
    "マホ(サマー)",
    "ミサキ",
    "ミサキ(ハロウィン)",
    "ミサト",
    "ミソギ",
    "ミソギ(ハロウィン)",
    "ミツキ",
    "ミフユ",
    "ミフユ(サマー)",
    "ミミ",
    "ミミ(ハロウィン)",
    "ミヤコ",
    "ミヤコ(ハロウィン)",
    "ムイミ",
    "モニカ",
    "ユイ",
    "ユイ(ニューイヤー)",
    "ユカリ",
    "ユカリ",      # ☆6以降
    "ユキ",
    "ヨリ",
    "ラム",
    "リノ",
    "リノ",      # ☆6以降
    "リマ",
    "リマ",      # ☆6以降
    "リン",
    "ルゥ",
    "ルカ",
    "ルナ",
    "レイ",
    "レイ(ニューイヤー)",
    "レム",
]

# 攻撃属性
PHYSICAL = 0
MAGICAL = 1
PHYSICAL_AND_MAGICAL = 2
EMPTY = 3

# テーブル格納位置
UB = 0
UB_ALTER = 1
S1 = 2
S1_ALTER = 3
S2 = 4
S2_ALTER = 5

# UB属性テーブル　キャラクターの攻撃属性に一致させる
ub_type_table = [
    # アオイ
    PHYSICAL,
    # アオイ(編入生)
    PHYSICAL,
    # アカリ
    MAGICAL,
    # アキノ
    PHYSICAL,
    # アヤネ
    PHYSICAL,
    # アヤネ(クリスマス)
    PHYSICAL,
    # アユミ
    PHYSICAL,
    # アリサ
    PHYSICAL,
    # アン
    MAGICAL,
    # アンナ
    MAGICAL,
    # イオ
    MAGICAL,
    # イオ(☆6以降)
    MAGICAL,
    # イオ(サマー)
    MAGICAL,
    # イリヤ
    MAGICAL,
    # イリヤ(クリスマス)
    MAGICAL,
    # エミリア
    MAGICAL,
    # エリコ
    PHYSICAL,
    # エリコ(バレンタイン)
    PHYSICAL,
    # カオリ
    PHYSICAL,
    # カオリ(サマー)
    PHYSICAL,
    # カスミ
    MAGICAL,
    # カスミ(マジカル)
    MAGICAL,
    # カヤ
    PHYSICAL,
    # キャル
    MAGICAL,
    # キャル(☆6以降)
    MAGICAL,
    # キャル(サマー)
    MAGICAL,
    # キャル(ニューイヤー)
    MAGICAL,
    # キョウカ
    MAGICAL,
    # キョウカ(ハロウィン)
    MAGICAL,
    # クウカ
    PHYSICAL,
    # クウカ(オーエド)
    MAGICAL,
    # クリスティーナ
    PHYSICAL,
    # クリスティーナ(クリスマス)
    PHYSICAL,
    # クルミ
    PHYSICAL,
    # クルミ(クリスマス)
    PHYSICAL,
    # グレア
    MAGICAL,
    # クロエ
    PHYSICAL,
    # コッコロ
    PHYSICAL,
    # コッコロ(☆6以降)
    PHYSICAL,
    # コッコロ(サマー)
    PHYSICAL,
    # コッコロ(ニューイヤー)
    PHYSICAL,
    # サレン
    PHYSICAL,
    # サレン(サマー)
    PHYSICAL,
    # ジータ
    PHYSICAL,
    # シオリ
    PHYSICAL,
    # シオリ(マジカル)
    PHYSICAL,
    # シズル
    PHYSICAL,
    # シズル(バレンタイン)
    PHYSICAL,
    # シノブ
    PHYSICAL,
    # シノブ(ハロウィン)
    PHYSICAL,
    # ジュン
    PHYSICAL,
    # スズナ
    PHYSICAL,
    # スズナ(サマー)
    PHYSICAL,
    # スズメ
    MAGICAL,
    # スズメ(サマー)
    MAGICAL,
    # スズメ(ニューイヤー)
    MAGICAL,
    # タマキ
    PHYSICAL,
    # タマキ(サマー)
    PHYSICAL,
    # チカ
    MAGICAL,
    # チカ(クリスマス)
    MAGICAL,
    # ツムギ
    PHYSICAL,
    # トモ
    PHYSICAL,
    # ナナカ
    MAGICAL,
    # ニノン
    PHYSICAL,
    # ニノン(オーエド)
    PHYSICAL,
    # ネネカ
    MAGICAL,
    # ノゾミ
    PHYSICAL,
    # ノゾミ(クリスマス)
    PHYSICAL,
    # ハツネ
    MAGICAL,
    # ヒヨリ
    PHYSICAL,
    # ヒヨリ(ニューイヤー)
    PHYSICAL,
    # ペコリーヌ
    PHYSICAL,
    # ペコリーヌ(☆6以降)
    PHYSICAL,
    # ペコリーヌ(サマー)
    PHYSICAL,
    # ペコリーヌ(プリンセス)
    PHYSICAL,
    # マコト
    PHYSICAL,
    # マコト(サマー)
    PHYSICAL,
    # マツリ
    PHYSICAL,
    # マヒル
    PHYSICAL,
    # マホ
    MAGICAL,
    # マホ(☆6以降)
    MAGICAL,
    # マホ(サマー)
    MAGICAL,
    # ミサキ
    MAGICAL,
    # ミサキ(ハロウィン)
    MAGICAL,
    # ミサト
    MAGICAL,
    # ミソギ
    PHYSICAL,
    # ミソギ(ハロウィン)
    PHYSICAL,
    # ミツキ
    PHYSICAL,
    # ミフユ
    PHYSICAL,
    # ミフユ(サマー)
    PHYSICAL,
    # ミミ
    PHYSICAL,
    # ミミ(ハロウィン)
    PHYSICAL,
    # ミヤコ
    PHYSICAL,
    # ミヤコ(ハロウィン)
    PHYSICAL,
    # ムイミ
    PHYSICAL,
    # モニカ
    PHYSICAL,
    # ユイ
    MAGICAL,
    # ユイ(ニューイヤー)
    MAGICAL,
    # ユカリ
    PHYSICAL,
    # ユカリ(☆6以降)
    PHYSICAL,
    # ユキ
    MAGICAL,
    # ヨリ
    MAGICAL,
    # ラム
    MAGICAL,
    # リノ
    PHYSICAL,
    # リノ(☆6以降)
    PHYSICAL,
    # リマ
    PHYSICAL,
    # リマ(☆6以降)
    PHYSICAL,
    # リン
    PHYSICAL,
    # ルゥ
    MAGICAL,
    # ルカ
    PHYSICAL,
    # ルナ
    MAGICAL,
    # レイ
    PHYSICAL,
    # レイ(ニューイヤー)
    PHYSICAL,
    # レム
    PHYSICAL,
]
