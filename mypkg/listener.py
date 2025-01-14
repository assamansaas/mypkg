#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Masahiro Yasui
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class WeatherSubscriberNode(Node):
    def __init__(self):
        super().__init__('weather_subscriber')

        #サブスクライバの作成
        self.weather_sub = self.create_subscription(
            String,
            'weather_forecast',
            self.callback,
            10
        )

    def callback(self, msg):
        # 受信したメッセージをログに表示
        self.get_logger().info(f"{msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = WeatherSubscriberNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

