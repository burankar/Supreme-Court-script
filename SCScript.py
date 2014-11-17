'''This is a basic script that will output the U.S. Supreme Court makeup based on user input of a year. I'm making it to practice python objects and syntax. it will be updated with more functionality as I get more comfortable with Python.
Author: Brian Urankar
'''
	
#elif statement to verify integer input

#Justice class. Each justice is an instance of this
class Justice(object):
	
	def __init__(self, name, begin_date, end_date):
		self.name = name
		self.begin_date = begin_date
		self.end_date = end_date

#current justices
roberts = Justice('John Roberts', 2005, 2014)
kagan = Justice('Elena Kagan', 2010, 2014)
sotomayor = Justice('Sonia Sotomayor', 2009, 2014)
alito = Justice('Samuel Alito', 2006, 2014)
breyer = Justice('Stephen Breyer', 1994, 2014)
ginsburg = Justice('Ruth Bader Ginsburg', 1994, 2014)
thomas = Justice('Clarence Thomas', 1991, 2014)
kennedy = Justice('Anthony Kennedy', 1988, 2014)
scalia = Justice('Antonin Scalia', 1986, 2014)


list_of_justices = [roberts, kagan, sotomayor, alito, breyer, ginsburg, thomas, kennedy, scalia]

YEAR_INPUT = int(raw_input("Please enter year:"))
RESULTS = []
LEFT_COURT = []
ENTERED_COURT = []

def calculate_court(list):
	for x in list:
		if YEAR_INPUT >= x.begin_date and YEAR_INPUT <= x.end_date:
			RESULTS.append(x.name)
	if len(RESULTS) >= 10:
		for x in list:
			if YEAR_INPUT == x.end_date:
				RESULTS.remove(x.name)
				LEFT_COURT.append(x.name)
			if YEAR_INPUT == x.begin_date:
				RESULTS.remove(x.name)
				ENTERED_COURT.append(x.name)

print YEAR_INPUT			
calculate_court(list_of_justices)
print RESULTS
print LEFT_COURT
print ENTERED_COURT

#print 'The Supreme Court Justices were: %s, %s, %s, %s, %s, %s, %s, %s, %s,' % tuple(RESULTS)
			


