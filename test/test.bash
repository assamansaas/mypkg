#!/bin/bash
# SPDX-FileCopyrightText: 2025 Masahiro Yasui
# SPDX-License-Identifier: BSD-3-Clause

# 引数で指定されたディレクトリに移動
dir=~
[ "$1" != "" ] && dir="$1"

# ROS 2 ワークスペースに移動してビルド
cd $dir/mypkg/ros2_ws
colcon build
source $dir/.bashrc

# 天気予報ノードを 10 秒間実行してログを保存
timeout 30 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

# ログファイルを確認
cat /tmp/mypkg.log |
grep weather:


