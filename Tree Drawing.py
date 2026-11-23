"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
import turtle

def draw_tree(my_turtle, branch_length, leaf_color, trunk_color):
    if branch_length <= 20:
        my_turtle.color(leaf_color)
        my_turtle.forward(branch_length)
        my_turtle.backward(branch_length)
        my_turtle.color(trunk_color)
    else:
        my_turtle.forward(branch_length * .8)
        my_turtle.left(30)
        draw_tree(my_turtle, branch_length * .8, leaf_color, trunk_color)
        my_turtle.right(60)
        draw_tree(my_turtle, branch_length * .8, leaf_color, trunk_color)
        my_turtle.left(30)
        my_turtle.backward(branch_length * .8)
