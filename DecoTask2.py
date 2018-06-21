import functools

def once(func):
	@functools.wraps(func)
	def inner(*args, **kwargs):
		if not inner.called:
			inner.result = func(*args, **kwargs)
			inner.called = True

		return inner.result

	inner.called = False
	return inner


@once
def init():
	print('Calculated')
	return 5 + 2


print(init())
print(init())