# Converts a in form "mm/dd/yyyy" to month, day, year

import string

def main():
    dateStr = raw_input("Enter a date(mm/dd/yyy): ")

    monthStr, dayStr, yearStr = string.split(dateStr, "/")

    months = ["January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]
    monthStr = months[int(monthStr)-1]

    print "The converted data is:", monthStr, dayStr+",", yearStr

main()
