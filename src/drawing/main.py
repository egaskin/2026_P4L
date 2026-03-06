import pygame
import os
print(os.getcwd())

"""
Notes:
- use "digital color meter" on Mac to see colors of individual pixels
- see introduction to python graphics lesson on P4L: https://programmingforlovers.com/chapter-3-building-a-self-replicating-cellular-automaton-with-top-down-programming/chapter-3-python-code-alongs/introduction-to-graphics/
    - RGB color chart
    - graphics coordinates vs cartesian coordinates


In this we will draw a snowperson using pyame, and then we will draw a game board for the game of life using rectangles and circles for the cells.

In the next lesson we will animate the game of life board. Some self assinged exercises to try before then:
- try adding gridlines to the game board
"""

def main():
    print("Drawing in python with pyame")
    pygame.init() # creates a pygame session
    width, height = 1000, 2000

    # make a blank canvas object that is width x height pixels
    surface = pygame.Surface((width, height))

    black = (0, 0, 0)
    white = (255, 255, 255)
    gray = (128, 128, 128)
    orange = (255, 165, 0)

    # fill the surface with the background color
    surface.fill(black)

    # objects are functionally pass by reference
    # technically everything in Python is an object, and 
    # everything is "pass by object reference"
    # draw a circle in the middle of the surface
    draw_snowperson(surface, white, black, orange)

    # save the image and quit pygame to save memory
    pygame.image.save(surface, "./snowperson.png")

    # let's draw the board for the game of life as displayed in the P4L chapter 3 code along,
    # Programming for Lovers in Python: Drawing and Animating with Pygame
    dark_gray = (64, 64, 64)
    cell_width = 1000//2 # pixels
    # copy code from two_d_arrays for the r_pentamino board
    # declare the R Pentamino with everything starting as False
    num_cols = 5
    num_rows = 5
    r_pentomino = [[False] * num_cols for _ in range(num_rows)]
    # set the values that are alive to True
    r_pentomino[1][2] = True
    r_pentomino[1][3] = True
    r_pentomino[2][2] = True
    r_pentomino[2][1] = True
    r_pentomino[3][2] = True
    # print(r_pentomino)

    pentamino_surface = draw_game_board_v1(r_pentomino, white, dark_gray, cell_width)
    pygame.image.save(pentamino_surface, "./r_pentamino_rectangle.png")

    pentamino_surface = draw_game_board_v2(r_pentomino, white, dark_gray, cell_width, scaling_factor = 0.95)
    pygame.image.save(pentamino_surface, "./r_pentamino_circle.png")

    # put at end of main to close the pygame session and save memory. if you don't do this, you might have multiple pygame sessions running at the same time, which can cause memory leaks and crashes
    pygame.quit()

def draw_snowperson(
        surface: pygame.Surface, 
        body_color: tuple[int, int, int], 
        object_color: tuple[int, int, int], 
        accent_color: tuple[int, int, int]
):
    """
    Draw a snowperson to a given canvas.

    :param surface: The canvas to draw on.
    :type surface: pygame.Surface
    :param body_color: The color of the snowperson's body.
    :type body_color: tuple[int, int, int]
    :param object_color: The color of the snowperson's objects.
    :type object_color: tuple[int, int, int]
    :param accent_color: The color of the snowperson's accent.
    :type accent_color: tuple[int, int, int]

    Returns:
    None
    """ 
    draw_bottom(surface, body_color, object_color, accent_color)
    draw_middle(surface, body_color, object_color, accent_color)
    draw_head(surface, body_color, object_color, accent_color)

def draw_head(
        surface: pygame.Surface, 
        body_color: tuple[int, int, int], 
        object_color: tuple[int, int, int], 
        accent_color: tuple[int, int, int]
):
    """
    Draw the head of a snowperson to a given canvas.

    :param surface: The canvas to draw on.
    :type surface: pygame.Surface
    :param body_color: The color of the snowperson's body.
    :type body_color: tuple[int, int, int]
    :param object_color: The color of the snowperson's objects.
    :type object_color: tuple[int, int, int]
    :param accent_color: The color of the snowperson's accent.
    :type accent_color: tuple[int, int, int]

    Returns:
    None
    """

    width, height = surface.get_size()

    center = (width * 0.5, height * 0.22)
    head_width = 0.2*width
    # paint a big circle for the head. a circle is defined by its center and radius
    pygame.draw.circle(surface, body_color, center = center, radius = head_width)

    # draw nose
    pygame.draw.circle(surface, accent_color, center = (center[0], center[1] + 0.2*head_width), radius = 0.10*head_width)

    # draw eyes
    eye_radius = 0.125*head_width
    eye_width = 0.5*head_width
    eye_height = center[1] - 0.25*head_width
    right_eye_center = (center[0] + eye_width, eye_height)
    left_eye_center = (center[0] - eye_width, eye_height)
    # right eye
    pygame.draw.circle(surface, object_color, center = right_eye_center, radius = eye_radius)
    # left eye
    pygame.draw.circle(surface, object_color, center = left_eye_center, radius = eye_radius)

    # draw a rectangle for mouth
    # rectangle is defined by its top left corner, width, and height in pixels
    mouth_width = 0.75*head_width
    mouth_height = 0.1*head_width
    # lower than the nose, so add 0.4*head_width to the y coordinate of the center
    # left of the center, so subtract 0.5*mouth_width from the x coordinate of the center
    mouth_top_left = (center[0] - mouth_width*0.5, center[1] + 0.4*head_width)
    pygame.draw.rect(surface, object_color, (mouth_top_left[0], mouth_top_left[1], mouth_width, mouth_height))

    # finally draw some eyebrows
    eyebrow_width = 0.3*head_width
    eyebrow_height = 0.1*head_width
    # above the eyes, so subtract 0.25*head_width from the y coordinate of the center
    # left of the eye, so subtract 0.5*eyebrow_width from the x coordinate of the eye center
    right_eyebrow_top_left = (right_eye_center[0] - eyebrow_width*0.5, right_eye_center[1] - 0.25*head_width)
    left_eyebrow_top_left = (left_eye_center[0] - eyebrow_width*0.5, left_eye_center[1] - 0.25*head_width)
    pygame.draw.rect(surface, object_color, (right_eyebrow_top_left[0], right_eyebrow_top_left[1], eyebrow_width, eyebrow_height))
    pygame.draw.rect(surface, object_color, (left_eyebrow_top_left[0], left_eyebrow_top_left[1], eyebrow_width, eyebrow_height))

def draw_middle(
        surface: pygame.Surface, 
        body_color: tuple[int, int, int], 
        object_color: tuple[int, int, int], 
        accent_color: tuple[int, int, int]
):
    """
    Draw the middle of a snowperson to a given canvas.

    :param surface: The canvas to draw on.
    :type surface: pygame.Surface
    :param body_color: The color of the snowperson's body.
    :type body_color: tuple[int, int, int]
    :param object_color: The color of the snowperson's objects.
    :type object_color: tuple[int, int, int]
    :param accent_color: The color of the snowperson's accent.
    :type accent_color: tuple[int, int, int]

    Returns:
    None
    """
    width, height = surface.get_size()

    # same (x coordinate as the head, but lower y coordinate)
    center = (width * 0.5, height * 0.4)
    middle_radius = 0.25*width
    # paint a circle for the middle that is slightly bigger than the head
    pygame.draw.circle(surface, body_color, center = center, radius = middle_radius) 

    # draw a button in the top of the middle circle
    button_radius = 0.1*middle_radius
    top_button_center = (center[0], center[1] - 0.5*middle_radius)
    pygame.draw.circle(surface, object_color, center = top_button_center, radius = button_radius)

    # draw a button in the middle of the middle circle
    pygame.draw.circle(surface, object_color, center = center, radius = button_radius)

    # draw a button in the bottom of the middle circle
    bottom_button_center = (center[0], center[1] + 0.5*middle_radius)
    pygame.draw.circle(surface, object_color, center = bottom_button_center, radius = button_radius)


def draw_bottom(
        surface: pygame.Surface, 
        body_color: tuple[int, int, int], 
        object_color: tuple[int, int, int], 
        accent_color: tuple[int, int, int]
):
    """
    Draw the bottom of a snowperson to a given canvas.

    :param surface: The canvas to draw on.
    :type surface: pygame.Surface
    :param body_color: The color of the snowperson's body.
    :type body_color: tuple[int, int, int]
    :param object_color: The color of the snowperson's objects.
    :type object_color: tuple[int, int, int]
    :param accent_color: The color of the snowperson's accent.
    :type accent_color: tuple[int, int, int]

    Returns:
    None
    """
    width, height = surface.get_size()

    # same (x coordinate as the head, but lower y coordinate)
    center = (width * 0.5, height * 0.6)
    bottom_radius = 0.32*width
    # paint a circle for the bottom that is slightly bigger than the middle
    pygame.draw.circle(surface, body_color, center = center, radius = bottom_radius) 

"""
Game of life code below here
"""
def draw_game_board_v1(
    board: list[list[bool]], 
    live_color: tuple[int, int, int],
    dead_color: tuple[int, int, int],
    cell_width: int
) -> pygame.Surface:
    """
    Draw a Game of Life cellular automaton board to a given canvas, using rectangles for cells

    :param board: the 2D list representing the game board, where each element is a boolean indicating whether the cell is alive (True) or dead (False).
    :type board: list[list[bool]]
    :param live_color: The color of the live cells.
    :type live_color: tuple[int, int, int]
    :param dead_color: The color of the dead cells.
    :type dead_color: tuple[int, int, int]
    :param cell_width: The width of each cell in pixels.
    :type cell_width: int

    Returns:
    - pygame.Surface: The canvas with the game board drawn on it.
    """

    if not isinstance(cell_width, int) or cell_width <= 0:
        raise ValueError("cell_width must be an integer")
    
    if not isinstance(board, list) or len(board) <= 0:
        raise ValueError("board must be a 2D list")
    
    # and colors too
    board_width = len(board[0])
    board_height = len(board)
    
    # fill the board with the background color, which is dead
    width = board_width * cell_width
    height = board_height * cell_width
    surface = pygame.Surface((width, height))
    surface.fill(dead_color)
    
    # fill the live cells with their color
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]: # if the cell is alive, draw a rectangle for it

                # define the coordinates of top left of rect
                x = col * cell_width
                y = row * cell_width

                pygame.draw.rect(surface, live_color, (x, y, cell_width, cell_width))
    
    return surface

def draw_game_board_v2(
    board: list[list[bool]], 
    live_color: tuple[int, int, int],
    dead_color: tuple[int, int, int],
    cell_width: int,
    scaling_factor: float = 1.0
) -> pygame.Surface:
    """
    Draw a Game of Life cellular automaton board to a given canvas using circles for cells instead of rectangles.

    :param board: the 2D list representing the game board, where each element is a boolean indicating whether the cell is alive (True) or dead (False).
    :type board: list[list[bool]]
    :param live_color: The color of the live cells.
    :type live_color: tuple[int, int, int]
    :param dead_color: The color of the dead cells.
    :type dead_color: tuple[int, int, int]
    :param cell_width: The width of each cell in pixels.
    :type cell_width: int
    :param scaling_factor: The scaling factor to apply to the cell radius to increase or decrease the size of the circles relative to the cell width. A value of 1 means the circles will have a radius equal to half the cell width, while a value less than 1 will make the circles smaller and a value greater than 1 will make them larger.
    :type scaling_factor: float

    Returns:
    - pygame.Surface: The canvas with the game board drawn on it.
    """

    if not isinstance(cell_width, int) or cell_width <= 0:
        raise ValueError("cell_width must be an integer")
    
    if not isinstance(board, list) or len(board) <= 0:
        raise ValueError("board must be a 2D list")
    
    # and colors too
    board_width = len(board[0])
    board_height = len(board)
    
    # fill the board with the background color, which is dead
    width = board_width * cell_width
    height = board_height * cell_width
    surface = pygame.Surface((width, height))
    surface.fill(dead_color)
    
    # fill the live cells with their color
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]: # if the cell is alive, draw a rectangle for it

                # define the coordinates of top left of rect
                x = int(col * cell_width)
                y = int(row * cell_width)

                center = (x + cell_width//2, y + cell_width//2)
                radius = (scaling_factor * cell_width)//2

                # draw a circle for each live cell
                pygame.draw.circle(surface, live_color, center = center, radius = radius)
    
    return surface

if __name__ == "__main__":
    main()