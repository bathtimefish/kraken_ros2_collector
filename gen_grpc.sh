#!/bin/sh

python3 -m grpc_tools.protoc -I./kraken_ros2_collector/proto --python_out=./kraken_ros2_collector/ --pyi_out=./kraken_ros2_collector/ --grpc_python_out=./kraken_ros2_collector/ ./kraken_ros2_collector/proto/kraken.proto