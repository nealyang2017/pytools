# -*- coding: utf-8 -*-
"""
Read in TXT log file and produce a CSV file containing the path.

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import re

data_x = []
data_y = []
f = open("20170714_154201RTLS_log.txt")
line_index = 0
for line in f:
    if "LE:0" in line:
        if line_index %  8== 0:
            pattern = re.compile(r'(\[.*?\])')
            match = re.findall(pattern, line)[0][1:-1].split(',')
            data_x.append(float(match[0]))
            data_y.append(float(match[1]))
        line_index += 1
file = open("path.tsv", 'w')
for i in range(len(data_x)):
    file.write(str(data_x[i]) + '\t')
    file.write(str(data_y[i]) + '\t')
    file.write('\n')
file.close()