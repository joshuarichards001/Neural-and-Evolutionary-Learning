import sys


# A class defining a certain wine
class Wine:
    def __init__(self, classification, values):
        self.classification = int(classification)
        self.values = values


# parsers the wines from a file into a list
def parser(file_num):
    wines = list()
    with open(sys.argv[file_num]) as f:
        lines = [line.rstrip() for line in f]
    iter_lines = iter(lines)
    next(iter_lines)
    for line in iter_lines:
        wine_list = list(map(float, line.split()))
        wines.append(Wine(wine_list[13], [wine_list[0], wine_list[1], wine_list[2], wine_list[3], wine_list[4],
                                          wine_list[5], wine_list[6], wine_list[7], wine_list[8], wine_list[9],
                                          wine_list[10], wine_list[11], wine_list[12]]))
    return wines


# Main code
if __name__ == '__main__':
    train_set = parser(-2)  # First file
    test_set = parser(-1)  # Second file
