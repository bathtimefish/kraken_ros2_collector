# Kraken ROS2 Collector

Kraken is a highlevel IoT data routing service.

![logo](./kraken-logo-300.png)

Kraken ROS2 Collector acts as a ROS2 subscriber that can subscribe to multiple topics and send them to the [Kraken Broker](https://github.com/bathtimefish/kraken_broker_python).

# Getting started

```
cd ~/ros2_ws/src
git clone https://github.com/bathtimefish/kraken_ros2_collector
cd ../..
colcon build --packages-select kraken_ros2_collector
source install/setup.bash
ros2 run kraken_ros2_collector collector
```