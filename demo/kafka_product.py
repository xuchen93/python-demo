import json
import traceback

from kafka import KafkaProducer
from kafka.errors import kafka_errors

from util import log_util

log = log_util.get_log(__name__)


def get_producer():
	# 假设生产的消息为键值对（不是一定要键值对），且序列化方式为json
	producer = KafkaProducer(
		bootstrap_servers=['124.220.50.39:9092'],
		key_serializer=lambda k: json.dumps(k).encode(),
		value_serializer=lambda v: json.dumps(v).encode())
	return producer


def producer_demo():
	producer = get_producer()
	# 发送三条消息
	for i in range(0, 3):
		future = producer.send(
			'kafka_demo',
			key='count_num',  # 同一个key值，会被送至同一个分区
			value=str(i),
			partition=0)
		log.info("send {}".format(str(i)))
		try:
			future.get(timeout=10)  # 监控是否发送成功
		except kafka_errors:  # 发送失败抛出kafka_errors
			traceback.format_exc()


def input_producer():
	producer = get_producer()
	while True:
		_value = input()
		if _value == 'bye':
			break
		future = producer.send(
			'kafka_demo',
			key='count_num',  # 同一个key值，会被送至同一个分区
			value=_value,
			partition=0)
		log.info("send {}".format(_value))
		try:
			future.get(timeout=10)  # 监控是否发送成功
		except kafka_errors:  # 发送失败抛出kafka_errors
			traceback.format_exc()


if __name__ == '__main__':
	# producer_demo()
	input_producer()
