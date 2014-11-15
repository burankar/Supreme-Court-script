'''This is a basic script that will output the U.S. Supreme Court makeup based on user input of a year. I'm making it to practice python objects and syntax. it will be updated with more functionality as I get more comfortable with Python.
'''
	
'''specific courts set as empty lists working reverse chronologically'''

#Roberts Court: 2005 - present
roberts_court = []

#Renquist Court: 1986 - 2005
renquist_court = []

#Burger Court: 1969 - 1986
burger_court = []

#Warren Court: 1954 -1969
warren_court = []

#Vinson Court: 1946 - 1953
vinson_court = []

#Stone Court: 1941 - 1946
stone_court = []

#Hughes Court: 1930 - 1041
hughes_court = []

#Taft Court: 1921 - 1930
taft_court = []

#White Court: 1910 - 1921
white_court = []

#Fuller Court: 1888 - 1910
fuller_court = []

#Waite Court: 1874 - 1888
waite_court = []

#Chase Court: 1864 - 1873 
chase_court = []

#Taney Court: 1835 - 1864
taney_court = []

#Marshall Court: 1801 - 1835
marshall_court = []

#Ellsworth Court: 1796 - 1800
ellsworth_court = []

#Rutledge Court: 1795 - 1795
rutledge_court = []

#Jay Court: 1789 - 1795
jay_court = []

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

def justice_sorting(list):
	for x in list:
		if x.end_date >= 2005:
			roberts_court.append(x.name)
	return roberts_court

justice_sorting(list_of_justices)	
print roberts_court

	
'''
#elif statements to break up years of courts
YEAR_INPUT = int(raw_input("Please enter year:"))

if YEAR_INPUT >= 2005:
'''	

