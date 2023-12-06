import pygame
import sys
import random

# Constants for UI
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells=40):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for _ in range(row_length)]
        self.solution = [[0] * row_length for _ in range(row_length)]
        self.fill_values()

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return num not in [self.board[row][col] for row in range(self.row_length)]

    def valid_in_box(self, row_start, col_start, num):
        box_values = [self.board[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)]
        return num not in box_values

    def is_valid(self, row, col, num):
        return (
            self.valid_in_row(row, num) and
            self.valid_in_col(col, num) and
            self.valid_in_box(row - row % 3, col - col % 3, num)
        )

    def fill_box(self, row_start, col_start):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                while not self.is_valid(i, j, nums[-1]):
                    random.shuffle(nums)
                self.board[i][j] = nums.pop()

    def fill_diagonal(self):
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        if row == self.row_length - 1 and col == self.row_length:
            return True

        if col == self.row_length:
            row += 1
            col = 0

        if self.board[row][col] != 0:
            return self.fill_remaining(row, col + 1)

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0

        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, 3)
        self.solution = [row[:] for row in self.board]

    def remove_cells(self):
        cells_to_remove = self.removed_cells
        while cells_to_remove > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_to_remove -= 1

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        # Implement if needed
        pass

    def draw(self):
        font = pygame.font.Font(None, 36)
        text = font.render(str(self.value) if self.value != 0 else '', True, BLACK)
        rect = pygame.Rect(self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.screen, RED if self.selected else WHITE, rect)
        self.screen.blit(text, rect)

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, screen) for j in range(width)] for i in range(height)]
        self.selected_cell = None

    def draw(self):
        for row in self.cells:
            for cell in row:
                cell.draw()
        self.draw_grid()

    def draw_grid(self):
        for i in range(1, GRID_SIZE):
            pygame.draw.line(self.screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT))
            pygame.draw.line(self.screen, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE))

    def select(self, row, col):
        if 0 <= row < self.height and 0 <= col < self.width:
            if self.selected_cell:
                self.selected_cell.selected = False
            self.selected_cell = self.cells[row][col]
            self.selected_cell.selected = True

    def click(self, x, y):
        row = y // CELL_SIZE
        col = x // CELL_SIZE
        return row, col

# UI and Main code in sudoku.py
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku Game")

    board = Board(GRID_SIZE, GRID_SIZE, screen, "easy")
    sudoku_generator = SudokuGenerator(row_length=GRID_SIZE, removed_cells=40)
    sudoku_generator.remove_cells()
    board.cells = [[Cell(sudoku_generator.board[i][j], i, j, screen) for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
    
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = board.click(x, y)
                board.select(row, col)

        screen.fill(WHITE)
        board.draw()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()

