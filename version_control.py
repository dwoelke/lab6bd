import pygame
import sys
from sudoku_generator import *
pygame.init()

WIDTH, HEIGHT = 400, 500
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (173, 216, 230)
RED = (255, 0, 0)

BUTTON_HEIGHT = 50
BUTTON_WIDTH = WIDTH // 3
font = pygame.font.Font(None, 36)

menu_image = pygame.image.load('background_menu.png')
easy_image = pygame.image.load('easy_image.png')
medium_image = pygame.image.load('medium_image.png')
hard_image = pygame.image.load('hard_image.png')

button_rect_1 = 0
button_rect_2 = 0
button_rect_3 = 0

menu_option = 0

example_grid = [[5, 4, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]]

selected_cell = None  # Initialize selected_cell

def draw_button(screen, image_path, position, size):
    button_image = pygame.image.load(image_path)
    button_image = pygame.transform.scale(button_image, (size, size))
    button_rect = button_image.get_rect(center=position)
    screen.blit(button_image, button_rect)
    return button_rect

def draw_menu():
    screen.blit(menu_image, (-10, 0))
    title_background_rect = pygame.Rect(0, 0, WIDTH, HEIGHT // 4)
    pygame.draw.rect(screen, BLUE, title_background_rect)

    title_surface = font.render("Welcome to Sudoku", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 8))
    screen.blit(title_surface, title_rect)

    # Draw buttons
    button_size = 100
    button_easy_rect = draw_button(screen, "easy_image.png", (WIDTH // 4, HEIGHT // 2), button_size)
    button_medium_rect = draw_button(screen, "medium_image.png", (WIDTH // 2, HEIGHT // 2), button_size)
    button_hard_rect = draw_button(screen, "hard_image.png", (3 * WIDTH // 4, HEIGHT // 2), button_size)

    return button_easy_rect, button_medium_rect, button_hard_rect

def draw_grid(grid, selected_cell, mouse_pos):
    global button_rect_1
    global button_rect_2
    global button_rect_3

    for row in range(9):
        for col in range(9):
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, cell_rect)
            pygame.draw.rect(screen, BLACK, cell_rect, 1)

            if grid[row][col] != 0:
                number_surface = font.render(str(grid[row][col]), True, BLACK)
                number_rect = number_surface.get_rect(center=cell_rect.center)
                screen.blit(number_surface, number_rect)

            if cell_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, RED, cell_rect, 2)

            if selected_cell == (row, col):  # Highlight selected cell
                pygame.draw.rect(screen, RED, cell_rect, 2)

    for i in range(0, 4):
        pygame.draw.line(screen, BLACK, (0, HEIGHT * i * 0.26), (WIDTH, HEIGHT * i * 0.26), 5)
        pygame.draw.line(screen, BLACK, (i * 0.33 * WIDTH, 0), (i * 0.33 * WIDTH, HEIGHT * 0.78), 5)

    # Draw buttons at the bottom
    # Button 1
    button_rect_1 = pygame.Rect(WIDTH * 0, HEIGHT * 0.8, BUTTON_WIDTH, HEIGHT * 0.1)
    pygame.draw.rect(screen, GRAY, button_rect_1)
    pygame.draw.rect(screen, BLACK, button_rect_1, 2)
    text_surface_1 = font.render("Reset", True, BLACK)
    text_rect_1 = text_surface_1.get_rect(center=button_rect_1.center)
    screen.blit(text_surface_1, text_rect_1)

    # Button 2
    button_rect_2 = pygame.Rect(WIDTH * 0.33, HEIGHT * 0.8, BUTTON_WIDTH, HEIGHT * 0.1)
    pygame.draw.rect(screen, GRAY, button_rect_2)
    pygame.draw.rect(screen, BLACK, button_rect_2, 2)
    text_surface_2 = font.render("Restart", True, BLACK)
    text_rect_2 = text_surface_2.get_rect(center=button_rect_2.center)
    screen.blit(text_surface_2, text_rect_2)

    # Button 3
    button_rect_3 = pygame.Rect(WIDTH * 0.66, HEIGHT * 0.8, BUTTON_WIDTH, HEIGHT * 0.1)
    pygame.draw.rect(screen, GRAY, button_rect_3)
    pygame.draw.rect(screen, BLACK, button_rect_3, 2)
    text_surface_3 = font.render("Exit", True, BLACK)
    text_rect_3 = text_surface_3.get_rect(center=button_rect_3.center)
    screen.blit(text_surface_3, text_rect_3)

def get_clicked_cell(mouse_pos):
    row = mouse_pos[1] // CELL_SIZE
    col = mouse_pos[0] // CELL_SIZE
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        return row, col
    else:
        return None

def is_board_correct(grid):
    # Implement your logic to check if the board is correct
    pass

def game_win():
    global menu_option
    screen.blit(menu_image, (-10, 0))
    title_background_rect = pygame.Rect(0, 0, WIDTH, HEIGHT // 4)
    pygame.draw.rect(screen, BLUE, title_background_rect)

    title_surface = font.render("Game Win!", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 8))
    screen.blit(title_surface, title_rect)

    button_rect_2 = pygame.Rect(WIDTH * 0.33, HEIGHT * 0.8, BUTTON_WIDTH, HEIGHT * 0.1)
    pygame.draw.rect(screen, GRAY, button_rect_2)
    pygame.draw.rect(screen, BLACK, button_rect_2, 2)
    text_surface_2 = font.render("Exit", True, BLACK)
    text_rect_2 = text_surface_2.get_rect(center=button_rect_2.center)
    screen.blit(text_surface_2, text_rect_2)

def game_over():
    global menu_option
    screen.blit(menu_image, (-10, 0))
    title_background_rect = pygame.Rect(0, 0, WIDTH, HEIGHT // 4)
    pygame.draw.rect(screen, BLUE, title_background_rect)

    title_surface = font.render("Game Over :(", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 8))
    screen.blit(title_surface, title_rect)

    button_rect_2 = pygame.Rect(WIDTH * 0.33, HEIGHT * 0.8, BUTTON_WIDTH, HEIGHT * 0.1)
    pygame.draw.rect(screen, GRAY, button_rect_2)
    pygame.draw.rect(screen, BLACK, button_rect_2, 2)
    text_surface_2 = font.render("Restart", True, BLACK)
    text_rect_2 = text_surface_2.get_rect(center=button_rect_2.center)
    screen.blit(text_surface_2, text_rect_2)

def main():
    pygame.display.set_caption("Sudoku Game")
    difficulty = None
    global button_rect_1
    global button_rect_2
    global button_rect_3
    global menu_option
    global example_grid  # Add this line to make example_grid global
    global selected_cell  # Add this line to make selected_cell global

    clicked_cell = None
    selected_cell = (0,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                clicked_cell = get_clicked_cell((x, y))
                if clicked_cell is not None:
                    selected_cell = clicked_cell
                if difficulty is None:
                    if button_easy_rect.collidepoint(x, y):
                        print("Easy")
                        difficulty = 1
                        if difficulty == 1:
                            example_grid = generate_sudoku(9, 30)  # Update example_grid

                    elif button_medium_rect.collidepoint(x, y):
                        difficulty = 2
                        print("Medium")
                        if difficulty == 2:
                            example_grid = generate_sudoku(9, 40)  # Update example_grid

                    elif button_hard_rect.collidepoint(x, y):
                        difficulty = 3
                        if difficulty == 3:
                            example_grid = generate_sudoku(9, 50)  # Update example_grid
                        print("Hard")
                else:
                    # Game state
                    if button_rect_1.collidepoint(x, y):
                        print("Reset button clicked")
                        menu_option = 5

                    elif button_rect_2.collidepoint(x, y):
                        print("Restart button clicked")
                        menu_option = 6

                    elif button_rect_3.collidepoint(x, y):
                        print("Exit button clicked")
                        menu_option = 7
                    clicked_cell = get_clicked_cell(pygame.mouse.get_pos())



            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    example_grid[selected_cell[0]][selected_cell[1]] = 1
                elif event.key == pygame.K_2:
                    example_grid[selected_cell[0]][selected_cell[1]] = 2
                elif event.key == pygame.K_3:
                    example_grid[selected_cell[0]][selected_cell[1]] = 3
                elif event.key == pygame.K_4:
                    example_grid[selected_cell[0]][selected_cell[1]] = 4
                elif event.key == pygame.K_5:
                    example_grid[selected_cell[0]][selected_cell[1]] = 5
                elif event.key == pygame.K_6:
                    example_grid[selected_cell[0]][selected_cell[1]] = 6
                elif event.key == pygame.K_7:
                    example_grid[selected_cell[0]][selected_cell[1]] = 7
                elif event.key == pygame.K_8:
                    example_grid[selected_cell[0]][selected_cell[1]] = 8
                elif event.key == pygame.K_9:
                    example_grid[selected_cell[0]][selected_cell[1]] = 9
                elif event.key == pygame.K_RETURN:

                    # Submit the guess (you can add your logic for checking correctness here)

                    if is_board_correct(example_grid):
                        game_win()
                    else:
                        game_over()
                elif event.key == pygame.K_DOWN and selected_cell[0] < 8:
                    selected_cell = (selected_cell[0] + 1, selected_cell[1])
                elif event.key == pygame.K_UP and selected_cell[0] > 0:
                    selected_cell = (selected_cell[0] - 1, selected_cell[1])
                elif event.key == pygame.K_RIGHT and selected_cell[1] < 8:
                    selected_cell = (selected_cell[0], selected_cell[1] + 1)
                elif event.key == pygame.K_LEFT and selected_cell[1] > 0:
                    selected_cell = (selected_cell[0], selected_cell[1] - 1)
        screen.fill(WHITE)

        if difficulty is None:
            # Draw menu
            button_easy_rect, button_medium_rect, button_hard_rect = draw_menu()





        elif menu_option == 5:
            for row in range(9):
                for col in range(9):
                    # Check if the cell was user-modified (not part of the original puzzle)
                    if example_grid[row][col] != 0:
                        example_grid[row][col] = 0
            selected_cell = (0, 0)  # Reset the selected cell
            menu_option = 0


        elif menu_option == 6:
            difficulty = None
            menu_option = 0

        elif menu_option == 7:
            exit()

        else:
            # Draw game grid
            draw_grid(example_grid, selected_cell, pygame.mouse.get_pos())
            if clicked_cell is not None:
                # Method that modifies the list
                print(clicked_cell)
                clicked_cell = None

        pygame.display.flip()

if __name__ == '__main__':
    main()

