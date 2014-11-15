'''This is a basic script that will output the U.S. Supreme Court makeup based on user input of a year. I'm making it to practice python objects and syntax. it will be updated with more functionality as I get more comfortable with Python.
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

list_of_justices = [roberts, kagan, sotomayor, alito, breyer, ginsburg, thomas]

'''
sorts through list of justices. It's close to being complete but still not perfect. If someone raw inputs '2014' it will probably draw the Roberts court with additional justices such as David Souter (served in Roberts court but retired in 2009). I think I need to add a boolean based around raw_input to fix it.
'''

YEAR_INPUT = int(raw_input("Please enter year:"))
RESULTS = []

def calculate_court(list):
	for x in list:
		if YEAR_INPUT >= x.begin_date and YEAR_INPUT <= x.end_date:
			RESULTS.append(x.name)

print YEAR_INPUT			
calculate_court(list_of_justices)
print 'The Supreme Court Justices were: %s, %s, %s, %s, %s, %s, %s, %s, %s,' % RESULTS
			


