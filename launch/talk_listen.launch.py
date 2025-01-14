# SPDX-FileCopyrightText: 2025 Masahiro Yasui
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    weather = launch_ros.actions.Node(
        package='mypkg',
        executable='weather',
        )
    listener = launch_ros.actions.Node(
            package='mypkg',
            executable='listener',
            output='screen'
            )

    return launch.LaunchDescription([weather, listener])

