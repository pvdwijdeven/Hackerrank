from os import listdir
from os.path import isfile, join

ORIGINAL_PATH = "C:\Kaggle\Original CSV"
SAMPLE_PATH = "C:\Kaggle\Samples"


def get_file_list():
    files_ = []
    try:
        files_ = [f for f in listdir(ORIGINAL_PATH) if isfile(join(ORIGINAL_PATH, f)) and f.endswith(".csv")]
    except WindowsError:
        exit("Aborting: %s does not exist, please make sure folder is correct!" % ORIGINAL_PATH)
    if not files_:
        exit("Aborting: no .csv files in %s!" % ORIGINAL_PATH)
    return files_


def investigate_files():
    files = get_file_list()
    results = [["filename", "columns", "rows"]]
    for filename in files:
        print ("counting lines in %s..." % filename)
        rows = 0
        with open(ORIGINAL_PATH + "\\" + filename, 'r') as f:
            for row in f:
                rows += 1
            print ("%s consists of: %i columns and %i rows" % (filename, len(row), rows))
            results.append([filename, len(row), rows])
    return results


def save_results(results):
    def add_padding(result_):
        output = ""
        for element, length in enumerate(max_length):
            output += '{s:{c}<{n}}'.format(s=result_[element], n=length + 1, c=' ')
        return output + "\n"

    max_length = []
    for item in range(len(results[0])):
        max_length.append(len(str(max(results, key=lambda x: len(str(x[item])))[item])))
    with open(ORIGINAL_PATH + "\\" + "data_sizes.txt", 'w') as f:
        for result in results:
            f.write(add_padding(result))


def create_sample_files(sample_size):
    files = get_file_list()
    for filename in files:
        print ("create sample of %s..." % filename)
        rows = 0
        results = []
        with open(ORIGINAL_PATH + "\\" + filename, 'r') as f:
            while rows <= sample_size:
                results.append(f.readline())
                rows += 1
        try:
            with open(SAMPLE_PATH + "\\" + str(sample_size) + "sample_" + filename, 'w') as f:
                for line in results:
                    f.write(line)
        except IOError:
            exit("Aborting: %s does not exist, please create folder first!" % SAMPLE_PATH)


#save_results(investigate_files())  # comment this after first use, takes a lot of time!
create_sample_files(1000)

print ("done!!!")
