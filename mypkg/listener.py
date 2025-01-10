import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32

class WeatherSubscriber(Node):
    def __init__(self):
        super().__init__('weather_subscriber')

        # 3つのトピックをサブスクライブ
        self.weather_subscription = self.create_subscription(
            String,
            'weather_condition',
            self.weather_callback,
            10
        )
        self.temperature_subscription = self.create_subscription(
            Float32,
            'temperature_forecast',
            self.temperature_callback,
            10
        )
        self.humidity_subscription = self.create_subscription(
            Float32,
            'humidity_forecast',
            self.humidity_callback,
            10
        )

    def weather_callback(self, msg):
        self.get_logger().info(f'Weather Condition: {msg.data}')

    def temperature_callback(self, msg):
        self.get_logger().info(f'Temperature: {msg.data:.2f}°C')

    def humidity_callback(self, msg):
        self.get_logger().info(f'Humidity: {msg.data:.2f}%')

def main(args=None):
    rclpy.init(args=args)
    node = WeatherSubscriber()
    rclpy.spin(node)

if __name__ == '__main__':
    main()

