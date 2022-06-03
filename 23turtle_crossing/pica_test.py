
import turtle
 
# turtle object
img_turtle = turtle.Turtle()
  
# registering the image
# as a new shape
turtle.register_shape('pica.gif')

# setting the image as cursor
img_turtle.shape('pica.gif')