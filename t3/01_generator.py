import argparse
def swap_case_dec(func):
    def inner(*args, **kwargs):
        for i in func(*args, **kwargs):
            yield i.swapcase()

    return inner


@swap_case_dec
def duplicate_gen(file_path):
    with open(file_path) as f:
        word_list = f.read()
    word_list = word_list.split(' ')
    for i in word_list:
        flag = False
        for j in i:
            if i.count(j) > 1:
                flag = True
                break
        if flag:
            yield i


# for i in duplicate_gen('test'):
#     print(i)

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='duplicate generator')
    parser.add_argument('-f', '--file', metavar='FILE', action='store', help='file path')
    args = parser.parse_args()
    for i in duplicate_gen(args.file):
        print(i)