#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import String


class WeatherForecastNode(Node):
    def __init__(self):
        super().__init__('weather_forecast')

        # パブリッシャー
        self.weather_pub = self.create_publisher(String, 'weather_forecast', 10)

        # タイマー
        self.timer = self.create_timer(1.0, self.publish_forecast)

        # OpenWeatherMap APIキーと都市名
        self.api_key = "3d30831cdb2eefd3dcb465577309f7d5"
        self.city = "Tokyo,JP"

    def get_weather_data(self):
        """OpenWeatherMap APIから天気データを取得"""
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric&lang=ja"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']  # 天気
            temperature = data['main']['temp']  # 気温
            humidity = data['main']['humidity']  # 湿度
            return weather, temperature, humidity
        else:
            self.get_logger().warn(f"天気データの取得に失敗しました: {response.status_code}")
            return "不明", 0.0, 0.0

    def publish_forecast(self):
        """フォーマットされた天気情報をパブリッシュ"""
        weather, temperature, humidity = self.get_weather_data()

        # フォーマットされた文字列を作成
        forecast_message = f"天気: {weather}, 気温: {temperature:.2f}°C, 湿度: {humidity:.2f}%"

        # ログに表示（確認用）
        # self.get_logger().info(f"weather: {forecast_message}")

        # パブリッシュ
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

