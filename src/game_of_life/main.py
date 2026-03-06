import os
import sys
import pygame
# from pathlib import Path
from custom_io import read_board_from_file
from functions import play_game_of_life
from drawing import draw_game_board, draw_game_boards
from animate import animate_surfaces


def main():
    print("Coding the Game of Life!")

    if len(sys.argv) != 5:
        raise ValueError("Usage: python main.py initial_board.csv output_prefix cell_width num_gens")

    # when you run a program with command line args, they are put into a list of strings called sys.arv
    input_csv = sys.argv[1]
    output_prefix = sys.argv[2]
    cell_width = int(sys.argv[3])
    num_gens = int(sys.argv[4])

    print(f"Input CSV: {input_csv}")
    print(f"Output Prefix: {output_prefix}")
    print(f"Cell Width: {cell_width}")
    print(f"Number of Generations: {num_gens}")

    print("Parameters read in successfully!")
    
    pygame.init()  # Initialize pygame
    initial_board = read_board_from_file(input_csv)  # Read the initial board from the CSV file
    white = (255, 255, 255)
    dark_gray = (64, 64, 64)
    intial_surface = draw_game_board(initial_board, white, dark_gray, cell_width)  # Draw the initial board
    path = f"{output_prefix}"
    os.makedirs(path, exist_ok=True)
    pygame.image.save(intial_surface, f"{path}dinnerTable0.png")  # Save the initial board image
    automaton_boards = play_game_of_life(initial_board, num_gens)  # Get the boards for each generation
    print("We played the game of life successfully. Drawing now...")
    surfaces = draw_game_boards(automaton_boards, white, dark_gray, cell_width)
    
    print("Boards drawn! Animating the Game of Life now...")
    animate_surfaces(surfaces, video_path = f"{output_prefix}dinnerTable.mp4")
    pygame.quit()  # Quit pygame when done

    print("Animation finished! Exiting normally.")

if __name__ == "__main__":
    main()
