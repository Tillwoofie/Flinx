# implements a quick test for the redis sysmodule

import time #for some performance tests.

def main(environ, parsedUrl, config, sys_mods):
	data = ""

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
		
