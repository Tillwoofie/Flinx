# implements a quick test for the redis sysmodule

import time #for some performance tests.
import random

def main(environ, parsedUrl, config, sys_mods):
	if not "redis-cache" in sys_mods:
		stderr_log("Redis could not be loaded, can't run module redis-test")
		return "Cannot test, requires redis-cache module."
	r = sys_mods['redis-cache'].get_existing_connection()
	
	data = ""

	words = generate_words_list(100)
	nums = generate_number_list(100)

	data += "Redis performance/functionality test\n"
		stderr_log("Redis could not be loaded, can't run module redis-test")
	start_time = time.time()
	for x in words:
		r.set(x, "1")
	words_insert = time.time()

	for x in nums:
		r.set(x, "num")
	nums_insert = time.time()

	words_pull = []
	for x in words:
		words_pull.append(r.get(x))
	if len(words_pull) == len(words):
		data += "words retreival good!\n"
	else:
		data += "WORDS NOT RETREIVED!\n"
	words_get = time.time()
	
	num_pull = []
	for x in nums:
		num_pull.append(r.get(x))
	if len(num_pull) == len(nums):
		data += "words retreival good!\n"
	else:
		data += "WORDS NOT RETREIVED!\n"
	nums_get = time.time()

	for x in words:
		r.delete(x)
	words_del = time.time()

	for x in nums:
		r.delete(x)
	nums_del = time.time()

	words_insert_time = words_insert - start_time
	nums_insert_time = nums_insert - words_insert
	words_ret_time = words_get - nums_insert
	nums_ret_time = nums_get - words_get
	words_del_time = words_del - nums_get
	nums_del_time = nums_del - words_del
	total_time = nums_del - start_time

	data += "words insert: %f \n" % (words_insert_time,)
	data += "nums insert: %f \n" % (nums_insert_time,)
	data += "words get: %f \n" % (words_ret_time,)
	data += "nums get: %f \n" % (nums_ret_time,)
	data += "words del: %f \n" % (words_del_time,)
	data += "nums del: %f \n" % (nums_del_time,)
	data += "total elapsed time: %f \n" % (total_time,)


	return data

def generate_words_list(length):
	words = ["tralala", "troll", "sillyness", "apple", "banana", "thing", "hello", "python"]
	word_list = {} #using a dictionary isn't nessecary, but simple for avoiding duplicates.
	x = 0
	while True:
		word = ''.join(random.choice(words) for _ in range(3))
		word_list[word] = x
		x += 1
		if len(word_list) >= length:
			break
	return word_list.keys()


def generate_number_list(length):
	numlist = [ x for x in range(length) ]
	return numlist
		

def test_list_redis(r_conn, iterable):
	#set test
	start = time.time()
	for x in iterable:
		r_conn.set(x, x)
	end = time.time()
	insert_time = end - start

	good = True
	start = time.time()
	for x in iterable:
		q = r_conn.get(x)
		if q != x:
			good = False
	end = time.time()
	get_time = end - start

	start = time.time()
	for x in iterable:
		r_conn.delete(x)
	end = time.time()
	del_time = end - start

	return (good, insert_time, get_time, del_time)


def stderr_log(msg):
	import sys
	sys.stderr.write("INFO_LOG: {}\n".format(msg))
