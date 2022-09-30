import sleep_v_0__1
import sleep_v_0_0
import sleep_v_0_1
import sleep_v_0_2_a
import sleep_v_0_2_b
import sleep_v_0_3
import time
import json

num = 0
offset_list = []
while num < 100:
    sleep_time = 1 / 60 / 2
    # sleep_time = 0.01
    start_time = time.time()
    sleep_v_0_3.sleep(sleep_time)
    end_time = time.time()

    interval_time = end_time - start_time
    # print("\n")
    # print("sleep_to", start_time + sleep_time)
    # print(start_time)
    # print(end_time)
    # print(interval_time)
    # print((interval_time - sleep_time) / sleep_time * 100, "%")

    # 偏差百分比
    offset_list.append((interval_time - sleep_time) / sleep_time * 100)
    num += 1

with open("./test_record/3.json", "w+") as file:
    json.dump(offset_list, file)
