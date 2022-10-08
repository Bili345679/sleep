import time

# v_0_4 采用 time.perf_counter() 精度更高，fall_sleep_pc 需用 time.perf_counter() 而非之前的time.time()
# 参数说明
# 带_pc为time.perf_counter(), 相对于time.time()更为精准
# 带_time为time.time()
# 优先级为
#   pc_ns > pc > time_ns > time
#   精准苏醒时间 > 精准入睡时间+睡眠保持时间 > 通用入睡时间+通用睡眠保持时间 > 通用苏醒时间
# 参数
#   sleep_time(_ns)   睡眠保持时间(_纳秒)
#   fall_sleep[_pc/_time](_ns)   入眠时间[精准/通用](_纳秒)
#   wake_up_pc[_pc/_time](_ns)   苏醒时间[精准/通用](_纳秒)
#   need_res    睡眠情况
def sleep(
    sleep_time=False,
    sleep_time_ns=False,
    fall_sleep_pc=False,
    fall_sleep_time=False,
    fall_sleep_pc_ns=False,
    fall_sleep_time_ns=False,
    wake_up_pc=False,
    wake_up_time=False,
    wake_up_pc_ns=False,
    wake_up_time_ns=False,
    need_res=False,
):
    fall_sleep = time.perf_counter_ns()
    if wake_up_pc_ns:
        # 精准苏醒纳秒时间
        pass
    elif wake_up_pc:
        # 精准苏醒时间
        wake_up_pc_ns = wake_up_pc * 1000000000
    elif sleep_time_ns or sleep_time:
        # 设定了睡眠保持时间
        if not sleep_time_ns:
            sleep_time_ns = sleep_time * 1000000000

        # 入睡时间
        if fall_sleep_pc_ns:
            # 精准入眠纳秒时间
            pass
        elif fall_sleep_pc:
            # 精准入眠纳秒时间
            fall_sleep = fall_sleep_pc * 1000000000
        elif fall_sleep_time_ns:
            # 通用入眠纳秒时间
            fall_sleep = fall_sleep_time_ns
        elif fall_sleep_time:
            # 通用入眠时间
            fall_sleep = fall_sleep_time * 1000000000

        # 苏醒时间
        wake_up_pc_ns = fall_sleep + sleep_time_ns
        fall_sleep_pc_ns = fall_sleep

    elif wake_up_time_ns:
        # 通用睡眠纳秒时间
        wake_up_pc_ns = wake_up_time_ns
    elif wake_up_time:
        # 通用睡眠时间
        wake_up_pc_ns = wake_up_time * 1000000000
    else:
        return False

    now_time_ns = time.perf_counter_ns()
    # 在当前时间小于目标时间时循环
    while now_time_ns < wake_up_pc_ns:
        now_time_ns = time.perf_counter_ns()
        pass

    if not need_res:
        return True
    else:
        res = {
            "sleep_time": sleep_time,
            "sleep_time_ns": sleep_time_ns,
            "fall_sleep_pc": fall_sleep_pc,
            "fall_sleep_time": fall_sleep_time,
            "fall_sleep_pc_ns": fall_sleep_pc_ns,
            "fall_sleep_time_ns": fall_sleep_time_ns,
            "wake_up_pc": wake_up_pc,
            "wake_up_time": wake_up_time,
            "wake_up_pc_ns": wake_up_pc_ns,
            "wake_up_time_ns": wake_up_time_ns,
            "real_wake_up": now_time_ns,
            "sleep_difference": now_time_ns - wake_up_pc_ns,
        }
        return res


# 上面的函数在判断过程中也会消耗一定时间，导致在要求极短睡眠时出错
# 上面的判断大约需要2000纳秒，如果要进行小于2000纳秒的睡眠，请采用后面的几个函数

# 精准睡眠
def sleep_pc(sleep_time=False, fall_sleep=False, wake_up=False):
    if not wake_up:
        if not fall_sleep:
            fall_sleep = time.perf_counter()
        if sleep_time:
            wake_up = fall_sleep + sleep_time
        else:
            return False
    while time.perf_counter() < wake_up:
        pass


# 精准睡眠(纳秒)
def sleep_pc_ns(sleep_time=False, fall_sleep=False, wake_up=False):
    if not wake_up:
        if not fall_sleep:
            fall_sleep = time.perf_counter_ns()
        if sleep_time:
            wake_up = fall_sleep + sleep_time
        else:
            return False
    while time.perf_counter_ns() < wake_up:
        pass


# 精准睡眠(最简)
def sleep_pc_easy(sleep_time):
    fall_sleep = time.perf_counter()
    wake_up = sleep_time + fall_sleep
    while time.perf_counter() < wake_up:
        pass


# 精准睡眠(最简)(纳秒)
def sleep_pc_ns_easy(sleep_time):
    fall_sleep = time.perf_counter_ns()
    wake_up = sleep_time + fall_sleep
    while time.perf_counter_ns() < wake_up:
        pass


# 精准苏醒
def sleep_to_pc(wake_up):
    while time.perf_counter() < wake_up:
        pass


# 精准苏醒
def sleep_to_pc_ns(wake_up):
    while time.perf_counter_ns() < wake_up:
        pass


if __name__ == "__main__":
    start_pc = time.perf_counter_ns()
    # 这几个函数从上往下，能进行最短睡眠时间越短
    #################################################
    sleep(sleep_time_ns=1000)
    # sleep_pc(1000 / 1000000000)
    # sleep_pc_ns(1000)
    # sleep_pc_easy(1000 / 1000000000)
    # sleep_pc_ns_easy(1000)
    # sleep_to_pc(1000 / 1000000000)
    # sleep_to_pc_ns(1000)
    #################################################
    end_time = time.perf_counter_ns()
    print(start_pc)
    print(end_time)
    print(end_time - start_pc)
