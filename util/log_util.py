import logging

import colorlog


def get_log(name=__name__, fmt_string='%(log_color)s %(asctime)s | %(threadName)s | %(module)s.%(funcName)s():%(lineno)d | %(message)s') -> logging.Logger:
	log = logging.getLogger(name)
	if name == __name__:
		fmt_string = '%(log_color)s %(asctime)s | %(threadName)s | %(message)s'
	log.setLevel(logging.DEBUG)
	__handler = logging.StreamHandler()
	__handler.setLevel(logging.DEBUG)
	log_colors = {
		'DEBUG': 'white',
		'INFO': 'green',
		'WARNING': 'yellow',
		'ERROR': 'red',
		'CRITICAL': 'purple'
	}
	fmt = colorlog.ColoredFormatter(fmt_string, log_colors=log_colors)
	__handler.setFormatter(fmt)
	log.addHandler(__handler)
	return log


__log = get_log()


def debug(obj, *args, **kwargs):
	__log.debug(obj, *args, **kwargs)


def info(obj, *args, **kwargs):
	__log.info(obj, *args, **kwargs)


def warning(obj, *args, **kwargs):
	__log.warning(obj, *args, **kwargs)


def error(obj, *args, **kwargs):
	__log.error(obj, *args, **kwargs)
