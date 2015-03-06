#!/usr/bin/python

import sys
import getopt
from decimal import *
from datetime import *
import calendar

def add_months(sourcedate,months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month / 12
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime.strptime(str(year)+str(month)+str(day),'%Y%m%d')

def main(argv):
    period_date = datetime.today()
    try:
        opts, args = getopt.getopt(argv,"hP:i:t:s:e:",["-principal=","interest=","term=","start_date=","end_date="])
    except getopt.GetoptError:
        print 'test.py -P <principal> -i <interest> -t <term> -s <start> -e <end>'
	sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -P <principal> -i <interest> -t <term> -s <start> -e <end>'
            sys.exit()
        elif opt in ("-P", "--principal"):
            P = Decimal(arg)
        elif opt in ("-i", "--interest"):
            i = (Decimal(arg)/12)/100
	elif opt in ("-t", "--term"):
            t = int(arg)
	elif opt in ("-s", "--start-date"):
	    start_date = datetime.strptime(arg, '%d-%b-%Y')
	elif opt in ("-e", "--end-date"):
	    period_date = datetime.strptime(arg, '%d-%b-%Y')
	
    n = ((period_date.year - start_date.year )*12)+(period_date.month - start_date.month)
    A = P * (i*(1+i)**t)/(((1+i)**t)-1)
    period_owed = (P * ((1+i)**n)) - (A*((((1+i)**n) - 1)/i))
    period_interest = period_owed*i
    period_principal = A - period_interest
    print(period_date)
    print(period_owed)
    print(period_interest)
    print(period_principal)
    print(A)
   
if __name__ == "__main__":
	   main(sys.argv[1:])
