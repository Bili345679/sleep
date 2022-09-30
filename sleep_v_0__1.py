import time

# v_0-1
def sleep(sleep_time=False, sleep_to=False, start_time=False):
    if not start_time:
        start_time = time.time()

    if sleep_to:
        sleep_time = sleep_to - start_time
    elif not sleep_time:
        return False

    time.sleep(sleep_time)

    return True
