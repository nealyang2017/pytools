# -*- coding: utf-8 -*-
"""
A text processing module.
Read in TXT log file and produce a CSV file containing the path.

"""
import matplotlib.pyplot as plt
import re

def path_log_process(log_file):
    """Read in a .text log file and produce a .csv file containing 
       corresponding path coordinates.
    """
    data_x = []
    data_y = []
    f = open(log_file)
    line_index = 0
    for line in f:
        if "LE:0" in line:
            if line_index %  8== 0:
                pattern = re.compile(r'(\[.*?\])')
                match = re.findall(pattern, line)[0][1:-1].split(',')
                data_x.append(float(match[0]))
                data_y.append(float(match[1]))
            line_index += 1
    file = open(log_file + ".tsv", 'w')
    for i in range(len(data_x)):
        file.write(str(data_x[i]) + '\t')
        file.write(str(data_y[i]) + '\t')
        file.write('\n')
    file.close()
