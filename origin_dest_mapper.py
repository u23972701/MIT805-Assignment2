#!/usr/bin/python3

import sys

# Function to get the column index by name
def get_column_index(header, column_name):
    try:
        return header.index(column_name)
    except ValueError:
        return None


for line in sys.stdin:
    # Split the input line into columns
    fields = line.strip().split(',')
    try:
        # collect origin, carrier and arrival delay time in minutes
        year = fields[0]
        month = fields[1]
        week = fields[3]
        carrier= fields[8]
        arrival_delay = int(fields[14])
        origin = fields[16]
        dest = fields[17]
        print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (carrier, origin, dest, year, month, week, arrival_delay))
    except ValueError:
        pass

