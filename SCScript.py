'''This is a basic script that will output the U.S. Supreme Court makeup based on user input of a year. I'm making it to practice python objects and syntax. it will be updated with more functionality as I get more comfortable with Python.
'''


#This thing is already getting unwieldy. I need to make a SC justice class.
class Justice(object):
	
	def __init__(self, name, begin_date, end_date):
		self.name = name
		self.begin_date = begin_date
		self.end_date = end_date

'''
I need to define a function that will allow for quick substitution of Justices. Justices may serve/leave courts in between CJ terms and creating SC instances for each year would be a PITA.
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

#elif statements to break up years of courts
#How to handle transitional years?


