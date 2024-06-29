from std_msgs.msg import Int32
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

import socket

kraken_settings = {
  'topics': [
    {
      'topic_name': '/topic1',
      'msg_type': Int32
    },
    {
      'topic_name': '/topic2',
      'msg_type': Float32
    },
    {
      'topic_name': '/cmd_vel',
      'msg_type': Twist 
    }
  ],
  # `meta` can send various information of the robot as meta data to kraken
  'meta': {
    'robot_name': 'kraken_ros2',
    'host': socket.gethostname()
  },
}