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
        # collect origin, carrier and departure delay time in minutes
        year = fields[0]
        month = fields[1]
        week = fields[3]
        carrier= fields[8]
        departure_delay = int(fields[15])
        origin = fields[16]
        dest = fields[17]
        print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (carrier, origin, dest, year, month, week, departure_delay))
    except ValueError:
        pass

