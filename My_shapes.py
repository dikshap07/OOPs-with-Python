# -*- coding: utf-8 -*-
from shapes import Paper,Triangle,Rectangle, Oval

paper = Paper()


#creating Rectangle and setting attributes using methods in the shape
#class which is the parent class of Rectangle
rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(300)
rect1.set_x(10)
rect1.set_y(10)
rect1.set_color('red')

rect1.draw() #to draw the rectangle on Paper 

#to display the drawing of the Rectangle
#paper.display()

rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_x(100)
rect2.set_y(100)
rect2.set_color('yellow')

rect2.draw()

#paper.display()


#creating an Oval

oval1 = Oval()
oval1.set_width(70)
oval1.set_x(400)
oval1.set_y(400)
oval1.draw()
#paper.display()

#creating a Triangle

triangle1 = Triangle()
triangle1.randomize()

triangle1.draw()

paper.display()

