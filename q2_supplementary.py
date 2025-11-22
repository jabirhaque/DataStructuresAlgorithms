from dataclasses import dataclass

@dataclass
class Node:
    """Implements a node from a (singly) linked grid.
    For a Node n:
        n.data holds an integer value
        n.nextX refers to the next Node horizontally in the linked grid, or None
        n.nextY refers to the next Node vertically in the linked grid, or None
    You must not modify this code.
    """
    data: int
    nextX: 'Node' = None
    nextY: 'Node' = None

@dataclass
class LinkedGrid:
    """Implements a (singly) linked grid.
    You must not modify this code.
    """
    head: Node = None
    sizeX: int = 0
    sizeY: int = 0

@dataclass
class LinkedGridWithTails:
    """Implements a (singly) linked grid with tails.
    You must not modify this code.
    """
    head: Node = None
    tailX: Node = None
    tailY: Node = None
    tailXY: Node = None
    sizeX: int = 0
    sizeY: int = 0


#### WRITE YOUR SOLUTION BELOW; DO NOT MODIFY CODE ABOVE THIS LINE####
#### COPY YOUR CODE FROM BELOW INTO A FILE q2.py FOR SUBMISSION ####
#### DO NOT INCLUDE CODE ABOVE THIS LINE IN q2.py ####

def show(linkedgrid):
    """Prints the linked grid in a readable format (for debugging)."""
    raise NotImplementedError("Implement this function")


def fetch(linkedgrid, i, j):
    """Returns the data at position (i, j) in the linked grid; i.e. the data held in the ith row and the jth column.
    Note: i and j are 1-indexed. fetch(linkedgrid, 1, 1) returns the data in the head node.
    """
    raise NotImplementedError("Implement this function")



def hor_cat(linked_grid_a, linked_grid_b):
    """Horizontally concatenates two linked grids of the same height (same sizeY)
    and returns the resulting linked grid. May modify inputs."""
    raise NotImplementedError("Implement this function")

    

def smart_hor_cat(tailed_grid_a, tailed_grid_b):
    """Horizontally concatenates two linked grids with tails of the same height
    and returns the resulting linked grid with tails. May modify inputs."""
    raise NotImplementedError("Implement this function")

def transpose(linked_grid):
    """Returns the transpose of the inputted linked grid with tails.
    May modify the inputted linked grid."""
    raise NotImplementedError("Implement this function")

def element_wise_add(linked_grid_a, linked_grid_b):
    """Returns a linked grid which is the element-wise sum of the two inputted linked grids.
    Assumes the two inputted linked grids have the same dimensions. May modify inputs."""
    raise NotImplementedError("Implement this function")


#### WRITE YOUR SOLUTION ABOVE; DO NOT MODIFY CODE BELOW THIS LINE ####
#### DO NOT INCLUDE CODE BELOW THIS LINE IN q2.py ####


# Some basic tests
def q2_simple_tests():
        
    # Setting up a 2x2 grid
    N1 = Node(data=7)
    N2 = Node(data=4)
    N3 = Node(data=3)
    N4 = Node(data=5)
    N1.nextX = N2
    N1.nextY = N3
    N2.nextY = N4
    N3.nextX = N4
    N2.nextX = None
    N3.nextY = None
    N4.nextX = None
    N4.nextY = None
    linked_grid_a = LinkedGrid(head=N1, sizeX=2, sizeY=2)

    print("Linked Grid A:")
    show(linked_grid_a)
    # should print
    #  7 4
    #  3 5
    print("Fetch (1,1):", end=" ")
    print(fetch(linked_grid_a, 1, 1))  # should print 7

    # Setting up a 2x1 grid (height 2, width 1)
    N5 = Node(data=201)
    N6 = Node(data=202)
    N5.nextY = N6
    N6.nextY = None 
    N5.nextX = None
    N6.nextX = None
    linked_grid_b = LinkedGrid(head=N5, sizeX=1, sizeY=2)
    print("Linked Grid B:")
    show(linked_grid_b)
    # should print
    # 201
    # 202

    # Horizontal concatenation of linked_grid_a and linked_grid_b
    linked_grid_c = hor_cat(linked_grid_a, linked_grid_b)
    print("Horizontal Concatenation of A and B:")
    show(linked_grid_c)
    # should print
    #  7 4 201
    #  3 5 202

    # Setting up a 2x2 grid with tails
    N1 = Node(data=11)
    N2 = Node(data=12)
    N3 = Node(data=13)
    N4 = Node(data=14)
    N1.nextX = N2
    N1.nextY = N3
    N2.nextY = N4
    N3.nextX = N4
    N2.nextX = None
    N3.nextY = None
    N4.nextX = None
    N4.nextY = None
    tailed_grid_a = LinkedGridWithTails(head=N1, tailX=N2, tailY=N3, tailXY=N4, sizeX=2, sizeY=2)
    print("Tailed Grid A:")
    show(tailed_grid_a)
    # should print
    #  11 12
    #  13 14
    print("Transposed Tailed Grid A:")
    show(transpose(tailed_grid_a))
    # should print
    #  11 13
    #  12 14

    ### Setting up a 2x1 grid with tails (height 2, width 1)
    N5 = Node(data=201)
    N6 = Node(data=202)
    N5.nextY = N6
    N6.nextY = None
    N5.nextX = None
    N6.nextX = None
    tailed_grid_b = LinkedGridWithTails(head=N5, tailX=N5, tailY=N6, tailXY=N6, sizeX=1, sizeY=2)
    print("Tailed Grid B:")
    show(tailed_grid_b)
    # should print
    # 201
    # 202
    print("Transposed Tailed Grid B:")
    show(transpose(tailed_grid_b))
    # should print
    # 201 202


    # Reset tailed_grid_a and tailed_grid_b; previous methods may have modified them
    N1 = Node(data=11)
    N2 = Node(data=12)
    N3 = Node(data=13)
    N4 = Node(data=14)
    N1.nextX = N2
    N1.nextY = N3
    N2.nextY = N4
    N3.nextX = N4
    N2.nextX = None
    N3.nextY = None
    N4.nextX = None
    N4.nextY = None
    tailed_grid_a = LinkedGridWithTails(head=N1, tailX=N2, tailY=N3, tailXY=N4, sizeX=2, sizeY=2)
    N5 = Node(data=201)
    N6 = Node(data=202)
    N5.nextY = N6
    N6.nextY = None
    N5.nextX = None
    N6.nextX = None
    tailed_grid_b = LinkedGridWithTails(head=N5, tailX=N6, tailY=N6, tailXY=N6, sizeX=1, sizeY=2)
    # Test for smart_hor_cat
    tailed_grid_c = smart_hor_cat(tailed_grid_a, tailed_grid_b)
    print("Smart Horizontal Concatenation of Tailed Grid A and B:")
    show(tailed_grid_c)


    # Test element-wise addition
    # Resetting linked_grid_a
    N1 = Node(data=7)
    N2 = Node(data=4)
    N3 = Node(data=3)
    N4 = Node(data=5)
    N1.nextX = N2
    N1.nextY = N3
    N2.nextY = N4
    N3.nextX = N4
    N2.nextX = None
    N3.nextY = None
    N4.nextX = None
    N4.nextY = None
    linked_grid_a = LinkedGrid(head=N1, sizeX=2, sizeY=2)

    # Resetting linked_grid_a
    N5 = Node(data=17)
    N6 = Node(data=14)
    N7 = Node(data=13)
    N8 = Node(data=15)
    N5.nextX = N6
    N5.nextY = N7
    N6.nextY = N8
    N7.nextX = N8
    N6.nextX = None
    N7.nextY = None
    N8.nextX = None
    N8.nextY = None
    linked_grid_b = LinkedGrid(head=N5, sizeX=2, sizeY=2)

    print("Element-wise Addition of Linked Grid A and B:")
    show(element_wise_add(linked_grid_a, linked_grid_b))
    # should print
    #  24 18
    #  16 20