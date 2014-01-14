"""
University of Alberta - CMPUT410 Lab 1 Python Classes For Noobs
Copyright (C) 2014  Alexander Wong

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class Student:
      courseMarks={}
      name= ""
      
      def __init__(self, name):
          self.name = name
      
      def addCourseMark(self, course, mark):
          self.courseMarks[course] = mark
          
      def average(self):
          avelist = self.courseMarks.values()
          return sum(avelist)/len(avelist)

x = Student("Biologist In Training")
x.addCourseMark("BIOL100", 4.0)
x.addCourseMark("BIOL101", 3.0)
print x.average()
