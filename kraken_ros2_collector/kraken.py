import os
import logging
import asyncio
import grpc
from kraken_ros2_collector import kraken_pb2
from kraken_ros2_collector import kraken_pb2_grpc

async def send(payload):
    async with grpc.aio.insecure_channel(os.getenv('KRAKENC_BROKER_HOST')) as channel:
        stub = kraken_pb2_grpc.KrakenMessageStub(channel)
        response = await stub.Send(kraken_pb2.KrakenMessageRequest(kind="ros2", provider="ros2", payload=payload))
    logging.info("Kraken client received: status_code=%d" % response.status)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(send("{\"message\":\"Hello World\"}"))
