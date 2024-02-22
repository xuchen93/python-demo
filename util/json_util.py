import json

import orjson

from util import log_util


def to_json(o, beauty=False):
	return orjson.dumps(o, option=(orjson.OPT_INDENT_2 if beauty else 0) | orjson.OPT_OMIT_MICROSECONDS).decode()


def to_obj(json_str: str, beauty=False):
	return json.loads(json_str)


def to_pretty_json(o):
	return to_json(o, True)


def log_json(obj):
	log_util.info(to_json(obj))


def log_pretty_json(obj):
	log_util.info(to_pretty_json(obj))


def is_json(content: str):
	try:
		json.loads(content)
	except ValueError as e:
		return False
	return True
