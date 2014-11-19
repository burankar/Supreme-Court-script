'''
This is the first Python program I've written completely from scratch.
It is a basic script that will output the U.S. Supreme Court makeup based on user input of a year.
I'm making it to practice objects, syntax, proper PEP 8 conventions, and source code management.
It will be updated with more functionality as I get more comfortable with Python.
I don't have every justice added because...well, there are a lot of justices!
'''
'''
The MIT License (MIT)
Copyright (c) 2014 Brian Urankar
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

class Justice(object):


	def __init__(self, name, begin_date, end_date):
		self.name = name
		self.begin_date = begin_date
		self.end_date = end_date
		
		

roberts = Justice('John Roberts', 2005, 2014)
kagan = Justice('Elena Kagan', 2010, 2014)
sotomayor = Justice('Sonia Sotomayor', 2009, 2014)
alito = Justice('Samuel Alito', 2006, 2014)
breyer = Justice('Stephen Breyer', 1994, 2014)
ginsburg = Justice('Ruth Bader Ginsburg', 1994, 2014)
thomas = Justice('Clarence Thomas', 1991, 2014)
kennedy = Justice('Anthony Kennedy', 1988, 2014)
scalia = Justice('Antonin Scalia', 1986, 2014)
souter = Justice('David Souter', 1990, 2009)
oconnor = Justice("Sandra Day O'Connor", 1981, 2006)
stevens = Justice('John Paul Stevens', 1975, 2010)
rehnquist = Justice('William Rehnquist', 1972, 2005)
powell = Justice('Lewis F. Powell, Jr.', 1972, 1987)
blackmun = Justice('Harry Blackmun', 1970, 1994)
burger = Justice('Warren E. Burger', 1969, 1986)
marshall = Justice('Thurgood Marshall', 1967, 1991)
fortas = Justice('Abe Fortas', 1965, 1969)
goldberg = Justice('Arthur Goldberg', 1962, 1965)
white = Justice('Byron White', 1962, 1993)

list_of_justices = [roberts, kagan, sotomayor, alito, breyer, ginsburg, \
					thomas, kennedy, scalia, souter, oconnor, stevens, \
					rehnquist, powell, blackmun, burger, marshall, fortas, \
					goldberg, white]
while True:
	try: 
		YEAR_INPUT = int(raw_input("Please enter year(YYYY):"))
		break
	except ValueError:
		print "Sorry!This program only accepts years in YYYY format."
	
RESULTS = []
LEFT_COURT = []
ENTERED_COURT = []
INP_STR = str(YEAR_INPUT)


def calculate_court(list):
	for x in list:
		if YEAR_INPUT >= x.begin_date and YEAR_INPUT <= x.end_date:
			RESULTS.append(x.name)
		if len(RESULTS) >= 10:
			for x in list_of_justices:
				if YEAR_INPUT == x.end_date:
					RESULTS.remove(x.name)
					LEFT_COURT.append(x.name)
				if YEAR_INPUT == x.begin_date:
					RESULTS.remove(x.name)
					ENTERED_COURT.append(x.name)

def correct_answer():
	print "In " + INP_STR + " the Justices were:"
	for x in RESULTS:
		print x
	for x in LEFT_COURT:
		print "Justice " + x + " left the court in " + INP_STR
	for x in ENTERED_COURT:
		print "Justice " + x + " joined the court in " + INP_STR

calculate_court(list_of_justices)
correct_answer()
