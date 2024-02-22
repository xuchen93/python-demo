import functools
import time

from requests.exceptions import ConnectionError

from util import log_util


def cost_time(f):
	@functools.wraps(f)
	def cost(*args, **kwargs):
		start = time.time_ns()
		__data = f(*args, **kwargs)
		end = time.time_ns()
		log_util.info("[%s]耗时：%s ms", f.__name__, (end - start) / 1000_000)
		return __data

	return cost


def request_retry(retry_count: int = 2, time_interval: int = 3, exceptions=(ConnectionError,)):
	def retry_decorator(f):
		@functools.wraps(f)
		def do_retry(*args, **kwargs):
			exc = None
			for i in range(retry_count):
				try:
					data = f(*args, **kwargs)
					return data
				except Exception as e:
					if any(isinstance(e, ex_type) for ex_type in exceptions):
						log_util.warning("[%s]捕捉到异常，进行重试。异常：%s", f.__name__, e.args)
						time.sleep(time_interval)
						exc = e
					else:
						raise e
			log_util.warning(str(f'[{f.__name__}]超过最大重试次数'))
			raise exc

		return do_retry

	return retry_decorator
