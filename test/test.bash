#!/bin/bash
# SPDX-FileCopyrightText: 2024 Masahiro Yasui
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

if [ -d "$dir/ros2_ws" ]; then
    cd "$dir/ros2_ws"
else
    echo "Error: $dir/ros2_ws not found."
    exit 1
fi

colcon build || { echo "Error: Build failed."; exit 1; }

source install/setup.bash || { echo "Error: Could not source ROS 2 setup."; exit 1; }

log_file="/tmp/omikuji_test.log"
> "$log_file"

timeout 10 ros2 launch mypkg talk_listen.launch.py > "$log_file"

echo "Checking for omikuji results in logs..."
if grep -Eq '大吉|中吉|小吉|吉|末吉|凶' "$log_file"; then
    echo "Omikuji test passed: Found omikuji results in logs."
    grep -E '大吉|中吉|小吉|吉|末吉|凶' "$log_file"
else
    echo "Omikuji test failed: No omikuji results found in logs."
fi

