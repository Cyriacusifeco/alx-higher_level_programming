#!/usr/bin/python3

if __name__ == "__main__":

    def safe_print_list(my_list=[], x=0):
        i = 0
        count = 0

        while i < x:
            try:
                print(my_list[i], end='')
                count = count + 1

            except IndexError:
                return count

            i = i + 1
        print('\n')
        return count
