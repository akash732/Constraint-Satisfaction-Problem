# Constraint-Satisfaction-Problem

INTRODUCTION:

In a Constraint satisfaction problem, we have a set of variables with known domains and a set of constraints that impose restrictions on the values those variables can take. Our task is to assign a value to each variable so that we fulfill all the constraints.

Graph coloring (also called vertex coloring) is a way of coloring a graph’s
vertices such that no two adjacent vertices share the same color.

PROBLEM STATEMENT:

Graph coloring problem involves assigning colors to certain elements of a graph subject to certain restrictions and constraints. In other words, the process of assigning colors to the states such that no two adjacent states have the same color is caller Graph Colouring.
 
ALGORITHM:

•	Color first state with first color.
•	Do following for remaining v-1 states:
•	Consider the currently picked state and color it with the lowest numbered color that has not been used on any previously coloured state adjacent to it.
•	If all previously used colors on states adjacent to v, assign a new color to it.
