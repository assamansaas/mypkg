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

    return launch.LaunchDescription([talker, listener])

