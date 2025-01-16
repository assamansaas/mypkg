#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Masahiro Yasui
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import String


class WeatherForecastNode(Node):
    def __init__(self):
        super().__init__('weather_forecast')

        self.weather_pub = self.create_publisher(String, 'weather_forecast', 10)

        self.timer = self.create_timer(1.0, self.publish_forecast)

        self.api_key = "3d30831cdb2eefd3dcb465577309f7d5"
        self.city = "Tokyo,JP"

    def get_weather_data(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric&lang=ja"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            return weather, temperature, humidity
        else:
            self.get_logger().warn(f"天気データの取得に失敗しました: {response.status_code}")
            return "不明", 0.0, 0.0

    def publish_forecast(self):
        weather, temperature, humidity = self.get_weather_data()

        forecast_message = f"weather: {weather}, temperature: {temperature:.2f}°C, humidity: {humidity:.2f}%"

        self.weather_pub.publish(String(data=forecast_message))


def main(args=None):
    rclpy.init(args=args)
    node = WeatherForecastNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

