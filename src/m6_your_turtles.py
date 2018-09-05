"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Bryan Wolfe
"""
###############################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
#  Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
import rosegraphics as rg
window = rg.TurtleWindow()
turtle1 = rg.SimpleTurtle('turtle')
turtle2 = rg.SimpleTurtle('turtle')
turtle1.pen = rg.Pen('blue', 7)
turtle2.pen = rg.Pen('red', 7)
turtle1.speed = 15
turtle2.speed = 15
size = 100
for k in range(15):
    turtle1.draw_circle(size)
    turtle2.draw_circle(size)
    turtle1.pen_up()
    turtle2.pen_up()
    turtle1.forward(5)
    turtle2.backward(5)
    turtle1.pen_down()
    turtle2.pen_down()
    size = size-5

window.close_on_mouse_click()
###############################################################################
