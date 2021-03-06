
# Written by Jeff Hickson (rvbcaboose@gmail.com).
# This file is part of Flinx, a Python web-framework.

# Flinx is free software, and comes with no warranty.
# It is licenced under the GNU GLP v3.
# The full terms of this are available in the LICENCE file,
# in the root of the project, at <http://www.gnu.org/licenses/>,
# or at <https://github.com/Tillwoofie/Flinx/blob/master/LICENCE>

# implements a quick test for the redis sysmodule

import time  # for some performance tests.
import random


def main(environ, parsedUrl, config, sys_mods):
    if "redis-cache" not in sys_mods:
        stderr_log("Redis could not be loaded, can't run module redis-test")
        return "Cannot test, requires redis-cache module."
    r = sys_mods['redis-cache'].get_existing_connection()

    data = ""
    LIST_SIZE = int(get_url_arg("size", parsedUrl, 100))
    words = generate_words_list(LIST_SIZE)
    success, w_ins, w_get, w_del = test_list_redis(r, words)

    if success:
        data += "Words Test Success! Size = {} \n".format(LIST_SIZE)
    else:
        data += "Words Test Failure :( Size = {} \n".format(LIST_SIZE)
    data += ret_r_timing(w_ins, w_get, w_del)
    del(words)  # prevent too much memory from being used.

    nums = generate_number_list(LIST_SIZE)
    success, n_ins, n_get, n_del = test_list_redis(r, nums)

    if success:
        data += "Words Test Success! Size = {} \n".format(LIST_SIZE)
    else:
        data += "Words Test Failure :( Size = {} \n".format(LIST_SIZE)
    data += ret_r_timing(w_ins, w_get, w_del)
    del(nums)  # prevent too much memory from being used.

    return data


def generate_words_list(length):
    words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # using a dictionary isn't nessecary, but simple for avoiding duplicates.
    word_list = {}
    x = 0
    while True:
        word = ''.join(random.choice(words) for _ in range(3))
        word_list[word] = x
        x += 1
        if len(word_list) >= length:
            break
    return word_list.keys()


def generate_number_list(length):
    numlist = [x for x in range(length)]
    return numlist


def test_list_redis(r_conn, iterable):
    # set test
    start = time.time()
    for x in iterable:
        r_conn.set(x, x)
    end = time.time()
    insert_time = end - start

    good = True
    start = time.time()
    for x in iterable:
        q = r_conn.get(x)
        if q != str(x):
            good = False
    end = time.time()
    get_time = end - start

    start = time.time()
    for x in iterable:
        r_conn.delete(x)
    end = time.time()
    del_time = end - start

    return (good, insert_time, get_time, del_time)


def ret_r_timing(ins, get, delete):
    s = "Insert: {} Get: {} Delete: {}\n".format(ins, get, delete)
    return s


def stderr_log(msg):
    import sys
    sys.stderr.write("INFO_LOG: {}\n".format(msg))


def get_url_arg(arg, env, default=None):
    if env.env["PARSED_QUERY"] is not None:
        return env.env["PARSED_QUERY"].get(arg, default)
    else:
        return default
