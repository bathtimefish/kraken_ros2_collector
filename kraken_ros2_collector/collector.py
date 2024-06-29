import rclpy
from rclpy.node import Node
import json
import asyncio
from rosidl_runtime_py.utilities import get_message
from rosidl_runtime_py.convert import message_to_ordereddict
from kraken_ros2_collector.settings import kraken_settings
from kraken_ros2_collector import kraken

def message_to_dict(msg):
    return message_to_ordereddict(msg)

def message_to_json(msg):
    msg_dict = message_to_dict(msg)
    return json.dumps(msg_dict)

class KrakenTopicCollector(Node):

    def __init__(self):
        super().__init__('kraken_topic_collector')

        self.kraken_meta = json.dumps(kraken_settings['meta'])

        # Create subscribers for each topic
        for setting in kraken_settings['topics']:
            s = self.create_subscription(
                setting['msg_type'],
                setting['topic_name'],
                self.collector_callback,
                10
            )
            setattr(self, setting['topic_name'], s)
            getattr(self, setting['topic_name'])  # prevent unused variable warning

    def collector_callback(self, msg):
        payload = self.create_kraken_payload(msg)
        self.get_logger().info('%s' % payload)
        asyncio.run(kraken.send(json.dumps(payload)))

    def create_kraken_payload(self, msg):
        msg_type = f'{type(msg).__module__}.{type(msg).__name__}'
        msg = message_to_json(msg)
        meta = self.kraken_meta
        return {
            'msg': msg,
            'msg_type': msg_type,
            'meta': meta
        }

def main(args=None):
    rclpy.init(args=args)

    subscriber = KrakenTopicCollector()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()