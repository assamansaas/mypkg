#!/bin/bash
# SPDX-FileCopyrightText: 2024 Masahiro Yasui
# SPDX-License-Identifier: BSD-3-Clause

dir=~/mypkg
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws" || { echo "Error: Directory $dir/ros2_ws not found."; exit 1; }

colcon build || { echo "Error: Build failed."; exit 1; }

source install/setup.bash

log_file="/tmp/omikuji_test.log"
timeout 10 ros2 run mypkg omikuji > "$log_file"

if grep -Eq '大吉|中吉|小吉|吉|末吉|凶' "$log_file"; then
    grep -E '大吉|中吉|小吉|吉|末吉|凶' "$log_file"
else
    echo "No omikuji results found in logs."
fi


