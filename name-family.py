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

To run with tests, type "python name-family.py -v"
"""

class Student:
      courseMarks={}
      name= ""
      
      def __init__(self, name):
            """
            Initializes the student object
            
            >>> biologist = Student("Biologist In Training")
            >>> print biologist.name
            Biologist In Training
            """

            self.courseMarks = {}
            self.name = name
            
      def addCourseMark(self, course, mark):
            """
            Adds a course to the course marks.
            Assumes that mark is a float/int. Does not type check.
            
            >>> engineer = Student("Engineer In Training")
            >>> engineer.addCourseMark("MATH100", 2.0)
            >>> print(engineer.courseMarks["MATH100"])
            2.0
            """

            self.courseMarks[course] = mark
          
      def average(self):
            """
            Returns the average of all the course marks for this student
            
            Assumes that all marks are floats/ints, use default operators
            Note: This is not guaranteed to be floating point precise
            
            >>> man = Student("Man In Training")
            >>> man.addCourseMark("MAN100", 4.0)
            >>> man.addCourseMark("MAN200", 3.0)
            >>> print man.average()
            3.5
            """
            
            avelist = self.courseMarks.values()
            return sum(avelist)/len(avelist)
      
if __name__ == "__main__":
      import doctest
      doctest.testmod()
