import datetime
import logging


#конфігурація логера в окремий файл
logging.basicConfig(
            filename='hb_test.log',
            level=logging.WARNING,
            format='%(asctime)s:  %(message)s'
        )
logger = logging.getLogger("log_event")


#сортує переданий файл і дістає з нього список рядків, які включають переданий ключ
def sort_logs(filename, key):
    res_list = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                if key in line:
                    res_list.append(line)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return res_list


#дістає таймстемп з окремого рядка
def get_item_timestamp(line):
    start_position = line.find('Timestamp ') + len('Timestamp ')
    time_str = line[start_position : start_position+8]
    timestamp = datetime.datetime.strptime(time_str, '%H:%M:%S')
    return timestamp


#перебирає список рядків і дістає з них список таймстемпів
def get_timestamp_list(filename, key):
    timestamp_list = []
    for item in sort_logs(filename, key):
        timestamp_list.append(get_item_timestamp(item))
    return timestamp_list


#перебирає пари таймстемпів і порівнює дельту з вказаними значеннями норми. При порушенні норми логує повідомлення в файл
def analyse_logs(logs_list, min=31, max=33):
    for i in range(0, len(logs_list)-1):
        t1 = logs_list[i]
        t2 = logs_list[i+1]
        delta = (t1 - t2).total_seconds()
        if min < delta < max:
            logger.warning(f'"{t1}" - "{t2}" = {delta} seconds difference')
        elif delta >= max:
            logger.error(f'"{t1}" - "{t2}" = {delta} seconds difference')


lst = get_timestamp_list('hblog.txt', 'Key TSTFEED0300|7E3E|0400')
analyse_logs(lst)