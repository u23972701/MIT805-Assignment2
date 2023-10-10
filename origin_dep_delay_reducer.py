#!/usr/bin/python3

from operator import itemgetter 
import sys

# keep a map of the sum of arrival delay of each origin and carrier
carrier_departure_delay_map = {}

# Read input from standard input
for line in sys.stdin:
    # Split the input line into key and value
    carrier, origin, dest, year, month, week, departure_delay = line.strip().split('\t')
    
    try:
        departure_delay = int(departure_delay)
        carrier_departure_delay_map[(origin, dest, carrier, year, month, week)] = carrier_departure_delay_map.get(carrier, 0) + departure_delay
    except ValueError:
        # ignore lines where the count is not a number
        pass

# sort the carriers alphabetically;
alphabetic_carrier_departure_delay_map = sorted(carrier_departure_delay_map.items(), key=itemgetter(0))

# output to STDOUT
for key, val in alphabetic_carrier_departure_delay_map:
    print('%s\t%s\t%s\t%s\t%s\t%s\t%s'% (key[0], key[1], key[2], key[3], key[4], key[5], val))
    
    
