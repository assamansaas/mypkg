#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Masahiro Yasui
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class OmikujiPublisher(Node):
    def __init__(self):
        super().__init__('omikuji_publisher')
        self.publisher_ = self.create_publisher(String, '/omikuji', 10)
        self.timer = self.create_timer(1.0, self.publish_omikuji)  # 1秒ごとに結果を送信
        
        # おみくじの結果のリスト（大吉、中吉、小吉、凶、大凶）
        self.omikuji_results = [
            "大吉", "中吉", "小吉", "吉", "末吉", "凶", "大凶"
        ]
        
        # 各項目の結果（待ち人、失せ物、旅行、恋愛）
        self.omikuji_items = {
            "待ち人": [
                "来るべし", "来ないかもしれない", "遅れてくる", "全く来ない"
            ],
            "失せ物": [
                "見つかるだろう", "見つかりにくいが、もう少し探すと見つかる",
                "あきらめない方が良い", "しばらく見つからないかもしれない"
            ],
            "旅行": [
                "良い旅行ができる", "計画通りに行かないかもしれない", 
                "楽しい旅行になる", "慎重に計画を練ると良い"
            ],
            "恋愛": [
                "順調に進展する", "気になる人から連絡が来る",
                "少し時間がかかるかもしれない", "慎重に進めると良い"
            ]
        }

    def publish_omikuji(self):
        # 大吉～大凶をランダムに選択
        omikuji_result = random.choice(self.omikuji_results)
        
        # 結果を組み立てる
        result = f"{omikuji_result}\n"
        for item, options in self.omikuji_items.items():
            result += f"{item}: {random.choice(options)}\n"
        
        # メッセージを送信
        msg = String()
        msg.data = result
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published Omikuji:\n{result}")


def main(args=None):
    rclpy.init(args=args)
    omikuji_publisher = OmikujiPublisher()
    rclpy.spin(omikuji_publisher)
    omikuji_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

