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
	start_date = datetime.strptime('1-JAN-2015', '%d-%b-%Y')
	P = Decimal('100000.00')
	i = Decimal((8.5/12)/100)
	t = int(252)
	n = int(55)
	A = P * (i*(1+i)**t)/(((1+i)**t)-1)
	period_owed = (P * ((1+i)**n)) - (A*((((1+i)**n) - 1)/i))
	period_interest = period_owed*i
	period_principal = A - period_interest
	period_date = add_months(start_date, n)
	print(period_date)
	print(period_owed)
	print(period_interest)
	print(period_principal)
	print(A)


if __name__ == "__main__":
	   main(sys.argv[1:])
