from os import listdir
from os.path import isfile, join
from random import randint, seed
from time import time
from math import ceil

ORIGINAL_PATH = "H:\\R\\Kaggle\\Bosch\\data\\originals"
TRAIN_PATH = "H:\\R\\Kaggle\\Bosch\\data\\training"


def get_file_list(path=ORIGINAL_PATH, starts=""):
    files_ = []
    try:
        files_ = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(".csv") and f.startswith(starts)]
    except WindowsError:
        exit("Aborting: %s does not exist, please make sure folder is correct!" % path)
    if not files_:
        exit("Aborting: no .csv files in %s!" % path)
    return files_


def split_train_data(station_list, percentage=80):
    files = get_file_list(ORIGINAL_PATH, "train")
    seed(100)  # make sure every time this will create the same sets
    f1 = open(ORIGINAL_PATH + "\\" + files[0], 'r')
    f2 = open(ORIGINAL_PATH + "\\" + files[1], 'r')
    f3 = open(ORIGINAL_PATH + "\\" + files[2], 'r')
    temp_headers = f1.readline().split(",") + f2.readline().split(",")[1:] + f3.readline().split(",")[1:]
    headers = {}
    for i, header in enumerate(temp_headers):
        headers[header] = i
    # print headers
    train_headers = {}
    train_indices = {}
    for trainset in station_list:
        cur_header = []
        cur_index = []
        for station in station_list[trainset]:
            for header in headers:
                if station in header:
                    idx = headers[header]
                    cur_header.append(header)
                    cur_index.append(idx)
            cur_header.append("Response\n")
            response_idx = headers["Response\n"]
            cur_header = ["Id"] + cur_header
            ID_idx = headers["Id"]
            train_headers[trainset] = cur_header
            train_indices[trainset] = cur_index
            f = open(TRAIN_PATH + "\\" + trainset + "_train.csv", 'w')
            f.write(",".join(cur_header))
            f.close()
            f = open(TRAIN_PATH + "\\" + trainset + "_test.csv", 'w')
            f.write(",".join(cur_header))
            f.close()
    cnt = 0
    start = time()
    for line1 in f1:
        cnt += 1
        if cnt % int(1183749 / 100.0) == 0:
            perc = ceil(cnt / 11837.49)
            print ("Done so far: %i %%, estimated time left: %i seconds" % (
                perc, (100 - perc) * (time() - start) / float(perc)))
            print ("Processing for %i seconds now" % (time() - start))
        line2 = f2.readline()
        line3 = f3.readline()
        cur_line = map(str, line1.split(",") + line2.split(",")[1:] + line3.split(",")[1:])
        test_perc = randint(0, 100)
        if test_perc < percentage:
            target = "train"
        else:
            target = "test"
        for trainset in station_list:
            data = []
            has_data = False
            for idx in train_indices[trainset]:
                cur_dat = cur_line[idx]
                if cur_dat != "":
                    has_data = True
                data.append(cur_dat)
            if has_data:
                data = [cur_line[ID_idx]] + data + [cur_line[response_idx]]
                with open(TRAIN_PATH + "\\" + trainset + "_" + target + ".csv", 'a') as f:
                    f.write(",".join(data))

    f1.close()
    f2.close()
    f3.close()


stat_list = {"L3_S32": ["L3_S32"], "L3_S38": ["L3_S38"]}
split_train_data(stat_list, 80)
# stat_list = {"first_flow": ["L3_S29", "L3_S30", "L3_S37", "L3_S49", "L3_S51"]}
# split_train_data(stat_list, 80)
