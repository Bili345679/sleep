import sleep_v_0__1
import sleep_v_0_0
import sleep_v_0_1
import sleep_v_0_2_a
import sleep_v_0_2_b
import sleep_v_0_3
import time
import json

# 对齐刷新时间
def update_align():
    first_time = time.time()
    while time.time() == first_time:
        pass
    return True

num = 0
offset_list = []
while num < 100:
    sleep_time = 1 / 60 / 2
    # sleep_time = 0.01

    update_align()
    start_time = time.time()
    # 开始时间不是准确的
    sleep_v_0_3.sleep(sleep_time)
    # 结束时间不是准确的
    end_time = time.time()

    # 差值能准确？
    interval_time = end_time - start_time
    # print("\n")
    # print("sleep_to", start_time + sleep_time)
    # print(start_time)
    # print(end_time)
    # print(interval_time)
    # print((interval_time - sleep_time) / sleep_time * 100, "%")

    # 偏差百分比（能准确？）
    offset_list.append((interval_time - sleep_time) / sleep_time * 100)
    num += 1

with open("./test_record/3.json", "w+") as file:
    json.dump(offset_list, file)
