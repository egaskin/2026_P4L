import pygame
from datatypes import GameBoard
from functions import count_rows, count_cols


def draw_game_board(board: GameBoard, live_color: tuple[int, int, int], dead_color: tuple[int, int, int], cell_width: int, scaling_factor: float = 0.8) -> pygame.Surface:
    """   
    Draws a Game of Life automaton to a pygame.Surface object.

    Parameters:
    - board: 2-D list of booleans (True = alive, False = dead)
    - live_color: tuple of RGB values corresponding to live cells
    - dead_color: tuple of RGB values corresponding to dead cells
    - cell_width: integer representing the number of pixels (wide and tall) to represent a given cell of the game
    - scaling_factor: float representing a multiplier that is multiplied by the radius of the cell when we draw it (to prevent touching)

    Output:
    - pygame.Surface: canvas object corresponding to drawing the Game of Life board using the given parameters.
    """
    if not isinstance(cell_width, int) or cell_width <= 0:
        raise ValueError("Error: cell_width parameter has inappropriate type or value.")
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError("Error: board has inappropriate type or no rows.")
    # colors too

    # first thing we do is make the surface 
    width = cell_width * count_cols(board)
    height = cell_width * count_rows(board)
    surface = pygame.Surface((width, height))

    # fill the board with the background color, which is dead 
    surface.fill(dead_color)

    # range over all the cells in the board, and color each one with the appropriate color
    # note: because the background color is the dead color, I don't need to color the dead cells 
    for row in range(len(board)):
        for col in range(len(board[0])):
            # if the cell is alive, draw it!
            if board[row][col]:
                # draw circle: where is the center? Radius?

                radius = scaling_factor * (cell_width/2)
                # top left coordinates?
                x = col * cell_width + cell_width/2
                y = row * cell_width + cell_width/2

                pygame.draw.circle(surface, live_color, (int(x), int(y)), int(radius))

    return surface


def draw_game_boards(boards: list[GameBoard], live_color: tuple[int, int, int], dead_color: tuple[int, int, int], cell_width: int, scaling_factor: float = 0.8) -> list[pygame.Surface]:
    
    """
    Draw multiple GameBoards.
    Args:
        boards (list[GameBoard]): List of GameBoard objects.
        live_color (tuple[int, int, int])
        dead_color (tuple[int, int, int])
        cell_width (int): Pixel width of each cell.
        scaling_factor
    Returns:
        list[pygame.Surface]: Surfaces drawn for each board.
    """
    if not isinstance(boards, list) or len(boards) == 0:
        raise ValueError("boards must be a non-empty list.")
    
    result = []

    for board in boards:
        result.append(draw_game_board( board, live_color, dead_color, cell_width, scaling_factor))

    return result
