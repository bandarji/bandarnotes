#!/usr/bin/env python

from sys import stdout
from time import sleep

def progress_bar(count, total, mark_count=50, mark_char='#', unmarked_char='.',
                 left_msg='', right_msg=''):
    msg_left = left_msg if len(left_msg) <= 20 else left_msg[:20]
    msg_right = right_msg if len(right_msg) <= 20 else right_msg[:20]
    bar_filled = int(round(mark_count*count/float(total)))
    percent_str = str(round(100.0*count/float(total), 1))
    marked_progress = mark_char*(bar_filled+1)
    unmarked_progress = unmarked_char*(mark_count-bar_filled)
    progress = marked_progress + unmarked_progress
    stdout.write('\r{:20} {} {:>6}% {:20}'.
        format(left_msg, progress, percent_str, right_msg))
    stdout.flush()

def install_file(file_name, file_size):
    for i in range(file_size):
        progress_bar(i, file_size, left_msg=file_name, right_msg='Installing')
        sleep(0.2) # only here for display effect; remove
        # read_file_chunk() or whatever process
    progress_bar(1, 1, left_msg=file_name, right_msg='Installed')
    print('')

def main():
    install_file('FILE_ONE', 51)
    install_file('FILE_TWO', 97)

if __name__ == '__main__':
    main()
