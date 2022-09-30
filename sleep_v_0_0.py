import json
import time

# v_0_0
def sleep(sleep_time=False, sleep_to=False, start_time=False):
    if not start_time:
        start_time = time.time_ns()

    if sleep_time:
        # 从睡眠时间算醒来时间
        sleep_time *= 1000000000
        sleep_to = sleep_time + start_time
    elif not sleep_to:
        # 既没有睡眠时间，也没有醒来时间，直接退出
        return False
    else:
        sleep_to = sleep_to * 1000000000

    # 在当前时间小于目标时间时循环
    while time.time_ns() < sleep_to:
        pass
    return True
