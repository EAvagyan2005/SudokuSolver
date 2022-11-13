import math
import time
import os

s_list = [None] * 11
null_list = list()
NULL_VAL = 0
end_rec = False
probable_list = [None] * 11
exit_file = open('answers.txt', 'w')
end_x, end_y = 0, 0
interbetprints = 1000 # interval between prints
currnumofcyclbefprint = 0 # current number of cycles before print


def get_input():
    file = open("sudoku.txt", "r")
    global s_list
    for j in range(1, 10):
        s_list[j] = list(map(lambda x: int(x), file.readline().split()))
        s_list[j].insert(0, "$")


def get_nulls():
    global null_list
    for j in range(1, 10):
        for l in range(1, 10):
            if s_list[j][l] == NULL_VAL:
                null_list.append((j, l))


def check(x, y, sl_list):
    for j in range(1, 10):
        if (sl_list[x][y] == sl_list[j][y] and x != j) or \
                (sl_list[x][y] == sl_list[x][j] and y != j):
            return False
    range_x = math.ceil(x / 3) * 3
    range_y = math.ceil(y / 3) * 3
    for j in range(range_x - 2, range_x + 1):
        for l in range(range_y - 2, range_y + 1):
            if (j != x or l != y) and sl_list[x][y] == sl_list[j][l]:
                return False
    return True


def print_list(ls):
    print()
    for j in ls:
        if j is not None:
            for l in j:
                print(l if str(l).isdigit() else ' ', end=' ')
                exit_file.write(str(l) if str(l).isdigit() else ' ')
                exit_file.write(' ')
            print()
            exit_file.write('\n')
    


def try_comb(k, sl_list):
    global end_rec
    global currnumofcyclbefprint
    if len(null_list) == k+1:
        end_rec = True
        print_list(sl_list)
        return True

    curr_x, curr_y = null_list[k + 1]
    for j in range(1, 10):
        x = False
        new_sl_list = sl_list.copy()
        new_sl_list[curr_x][curr_y] = j
        if check(curr_x, curr_y, new_sl_list) and not end_rec:

            # if currnumofcyclbefprint >= interbetprints:
            #     os.system("cls")
            #     print_list(new_sl_list) 
            #     currnumofcyclbefprint = 0
            #     time.sleep(0.1)
            # currnumofcyclbefprint += 1

            # you can turn this on to see the process of brute-force
            x = try_comb(k + 1, new_sl_list)
            if new_sl_list[end_x][end_y] > 0:
                end_rec = True
                return True
    if not end_rec:
        new_sl_list[curr_x][curr_y] = 0


def start_solving():
    global end_x, end_y
    end_x = null_list[-1][0]
    end_y = null_list[-1][1]

    for i in range(1, 10):
        n_sl_list = s_list.copy()
        n_sl_list[null_list[0][0]][null_list[0][1]] = i
        if check(null_list[0][0], null_list[0][1], n_sl_list) and not end_rec:
            try_comb(0, s_list)


if __name__ == "__main__":
    get_input()
    get_nulls()
    start_solving()
