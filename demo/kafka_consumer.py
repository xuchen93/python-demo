import json

from kafka import KafkaConsumer

from util import log_util

log = log_util.get_log(__name__)


def consumer_demo():
	consumer = KafkaConsumer(
		'kafka_demo',
		bootstrap_servers='124.220.50.39:9092',
		group_id='test'
	)
	for message in consumer:
		log.info("receive, key: {}, value: {}".format(
			json.loads(message.key.decode()),
			json.loads(message.value.decode())
		)
		)


if __name__ == '__main__':
	consumer_demo()
