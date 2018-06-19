#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 14:31
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : splitCsvIntoMultipleFile.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com
"""
Description:
    Splits a CSV file into multiple files based on command line arguments.
    Arguments:
    `-h`: help file of usage of the script
    `-i`: input file name
    `-o`: output file name
    `-r`: row limit to split
    Default settings:
    `output_path` is the current directory
    headers are displayed on each split file
    the default delimeter is a comma
    Example usage:
    ```
    # split csv by every 100 rows
    >> python csv_split.py -i input.csv -o output -r 100
"""

import sys,os,csv,argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input_file",required=True,help="csv input file(with extension)",type=str)
    parser.add_argument("-o","--output_file",required=True,help="csv output file(with extension)",type=str)
    parser.add_argument("-r", "--row_limit", required=True, help="row limit to split csv at", type=int)
    args = parser.parse_args()

    is_valid_file(parser,args.input_file)

    is_valid_csv(parser,args.input_file,args.row_limit)

    return args.input_file,args.output_file,args.row_limit

def is_valid_file(parser,file_name):
    if not os.path.exists(file_name):
        parser.error("the file '{}' does not exist!".format(file_name))
        sys.exit()

def is_valid_csv(parser,file_name,row_limit):
    row_count = 0
    for row in csv.reader(open(file_name)):
        row_count += 1

    if row_limit > row_count:
        parser.error(
            "The 'row_count' of '{}' is > the number of rows in '{}'!".format(row_limit,file_name)
        )
        sys.exit()

def parse_file(arguments):
    input_file = arguments[0]
    output_file = arguments[1]
    row_limit = arguments[2]
    output_path = '.'

    with open(input_file,'r') as input_csv:
        datareader = csv.reader(input_csv)
        all_rows = []
        for row in datareader:
            all_rows.append(row)

        #remove header
        header = all_rows.pop(0)

        #split list of list into chunks
        current_chunk = 1

        for i in range(0,len(all_rows),row_limit):  # Loop through list
            chunk = all_rows[i:i+row_limit]         # Create single chunk

            current_output = os.path.join(
                output_path,"{}-{}.csv".format(output_file,current_chunk)
            )

            chunk.insert(0,header)

            with open(current_output,'w') as output_csv:
                writer = csv.wirter(output_csv)
                writer = writer.writerows(chunk)

            print("")
            print("Chunk # {}:".format(current_chunk))
            print("Filepath: {}".format(current_output))
            print("# of rows: {}".format(len(chunk)))

            current_chunk += 1

if __name__ == '__main__':
    arguments = get_arguments()
    parse_file(arguments)
    pass
