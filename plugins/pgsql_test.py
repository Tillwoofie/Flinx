
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
    if "pgsql" not in sys_mods:
        stderr_log("Postgres could not be loaded, can't run module pgsql")
        return "Cannot test, requires pgsql module."
    pg_conn = sys_mods['redis-cache'].get_existing_connection()
    pg_conn.autocommit = True  # better performance test for this.
    cur = pg_conn.cursor()

    test_table = "pgsql_test_23745"  # semi-random key mashing.

    # start test by ensuring clean slate.
    drop_if_exists(cur, test_table)

    data = ""
    LIST_SIZE = int(get_url_arg("size", parsedUrl, 100))
    words = generate_words_list(LIST_SIZE)

    timings = test_list_pgsql(cur, words)
    data += ret_r_timing(timings)

    # make sure we clean up.
    drop_if_exists(cur, test_table)
    cur.close()
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


def drop_if_exists(cur, table_name):
    # drops a table if it exists.
    if table_exists(cur, table_name):
        cur.execute("DROP TABLE %s;", (table_name,))


def table_exists(cur, table_name):
    # simply returns if a table exists or not.
    # Could likely code this better, but it's for a simple test.
    QUERY = "SELECT table_name FROM information_schema.tables WHERE"
    QUERY += " table_schema = 'public' AND table_name = %s;"
    cur.execute(QUERY, (table_name,))
    tables = cur.fetchall()
    if table_name in tables:
        return True
    return False


def create_test_table(cur, table_name):
    # creates the test table with the needed schema.
    QUERY = "CREATE TABLE {} (id serial PRIMARY KEY, test_str varchar);"
    cur.execute(QUERY, (table_name,))


def test_list_pgsql(cur, table_name, iterable):
    # set test
    start = time.time()
    QUERY = "INSERT INTO {} (test_str) VALUES (%s);".format(table_name)
    cur.executemany()
    end = time.time()
    insert_time = end - start

    good = True
    start = time.time()
    for x in iterable:
        QUERY = "SELECT test_str FROM %s WHERE test_str = %s;"
        cur.execute(QUERY, (table_name, x))
        # make sure we only get one result.
        res = cur.fetchall()
        if len(res) != 1:
            good = False
            continue
        else:
            q = res[0][0]  # should work?
        if str(q) != str(x):
            good = False
    end = time.time()
    get_time = end - start

    start = time.time()
    for x in iterable:
        cur.execute("DELETE FROM %s WHERE test_str = %s;", (table_name, x))
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
