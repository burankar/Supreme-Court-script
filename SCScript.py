'''This is a basic script that will output the U.S. Supreme Court makeup based on user input of a year. I'm making it to practice python objects and syntax. it will be updated with more functionality as I get more comfortable with Python.
'''
	
#specific courts set as empty lists working reverse chronologically
roberts_court = []
renquist_court = []
burger_court = []
warren_court = []
vinson_court = []
stone_court = []
hughes_court = []
taft_court = []
white_court = []
fuller_court = []
waite_court = [] 
chase_court = []
taney_court = []
marshall_court = []
ellsworth_court = []
rutledge_court = []
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

'''
sorts through list of justices. It's close to being complete but still not perfect. If someone raw inputs '2014' it will probably draw the Roberts court with additional justices such as David Souter (served in Roberts court but retired in 2009). I think I need to add a boolean based around raw_input to fix it.
'''

def justice_sorting(list):
	for x in list:
		if x.end_date >= 2005:
			roberts_court.append(x.name)
		elif x.end_date <= 2005 && x.end_date >= 1986:
			rehnquist_court.append(x.name)
		elif x.end_date <= 1986 && x.end_date >= 1969:
			burger_court.append(x.name)
		elif x.end_date <= 1969 && x.end_date >= 1954:
			warren_court.append(x.name)
		elif x.end_date <= 1954 && x.end_date >= 1946:
			vinson_court.append(x.name)
		elif x.end_date <= 1946 && x.end_date >= 1941:
			stone_court.append(x.name)
		elif x.end_date <= 1941 && x.end_date >= 1930:
			hughes_court.append(x.name)
		elif x.end_date <= 1930 && x.end_date >= 1921:
			taft_court.append(x.name)
		elif x.end_date <= 1921 && x.end_date >= 1910:
			white_court.append(x.name)
		elif x.end_date <= 1910 && x.end_date >= 1888:
			fuller_court.append(x.name)
		elif x.end_date <= 1888 && x.end_date >= 1874:
			waite_court.append(x.name)
		elif x.end_date <= 1874 && x.end_date >= 1864:
			chase_court.append(x.name)
		elif x.end_date <= 1864 && x.end_date >= 1835:
			taney_court.append(x.name)
		elif x.end_date <= 1835 && x.end_date >= 1801:
			marshall_court.append(x.name)
		elif x.end_date <= 1800 && x.end_date >= 1796:
			ellsworth_court.append(x.name)
		elif x.end_date <= 1796 && x.end_date >= 1795:
			rutledge_court.append(x.name)
		elif x.end_date <= 1795 && x.end_date >= 1789:
			jay_court.append(x.name)	
			
justice_sorting(list_of_justices)	
print roberts_court

	
'''
#elif statements to break up years of courts
YEAR_INPUT = int(raw_input("Please enter year:"))

if YEAR_INPUT >= 2005:
'''	

