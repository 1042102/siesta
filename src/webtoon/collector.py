# encoding=utf-8

import os

file_names = os.listdir('D:\\webtoon')

for file_name in file_names:
    # print file_name
    tmp_file_name = file_name.split('_')
    tmp_file_name[1] = tmp_file_name[1].zfill(4)
    tmp_file_name = '_'.join(tmp_file_name)
    # print tmp_file_name
    # print '_'.join(tmp_file_name)
    print '--------------------'

    os.rename('D:\\webtoon\\' + file_name, 'D:\\webtoon\\' + tmp_file_name)




# str_split = '119874_1_20100108110128_IMAG01_1.jpg'.split('_')
#
# print str_split
# print str_split[1]
# print str_split[1].zfill(4)
#
# str_split[1] = str_split[1].zfill(4)
#
# print str_split





