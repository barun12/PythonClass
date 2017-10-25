import thread
import time

def print_numbers(delay_sec, start, end, thread_name):
    start_time = time.time()
    for i in range(start, end+1):
        print "{}: {}".format(thread_name, i)
        time.sleep(delay_sec)
    end_time = time.time()
    print "Total time for {}: {}".format(thread_name, int(end_time - start_time))

try:
    thread.start_new_thread(print_numbers, (1, 1, 5, "t1"))
    thread.start_new_thread(print_numbers, (1, 6, 10, "t2"))
except Exception:
    pass


while True:
    pass

