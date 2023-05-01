import pygame
import random

# Init Pygame
pygame.init()

# Screen Size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



# Cells on the board
CELL_SIZE = 25
GRID_WIDTH = SCREEN_WIDTH / CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT / CELL_SIZE

# Muzzle velocity
SPEED = 5

# Create Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Class to create the snake
class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [(0, 0)]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = GREEN

    # Move Snake
    def move(self):
        x, y = self.positions[0]
        if self.direction == pygame.K_UP:
            y -= CELL_SIZE
        elif self.direction == pygame.K_DOWN:
            y += CELL_SIZE
        elif self.direction == pygame.K_LEFT:
            x -= CELL_SIZE
        elif self.direction == pygame.K_RIGHT:
            x += CELL_SIZE
        self.positions.insert(0, (x, y))
        if len(self.positions) > self.length:
            self.positions.pop()

    # Change the direction of the snake
    def change_direction(self, new_direction):
        if new_direction == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = new_direction
        elif new_direction == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = new_direction
        elif new_direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = new_direction
        elif new_direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = new_direction

    # Draw the Snake on the screen 
    def draw(self, surface):
        for position in self.positions:
            rect = pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, self.color, rect)

    # Increase the length of the snake
    def grow(self):
        self.length += 1

    # Reset Snake
    def reset(self):
        self.length = 1
        self.positions = [(0, 0)]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

# Food
class Food():
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

   # Draw food
    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, self.color, rect)


    def randomize_position(self):
        x = random.randint(0, GRID_WIDTH - 1) * CELL_SIZE
        y = random.randint(0, GRID_HEIGHT - 1) * CELL_SIZE
        self.position = (x, y)

# Check collision
def check_collision(position1, position2):
    return position1[0] == position2[0] and position1[1] == position2[1]

def main():
    # Objects
    snake = Snake()
    food = Food()

    # Clock
    clock = pygame.time.Clock()

    # Score
    score = 0

    # Loop 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    snake.change_direction(event.key)

        # Move snake
        snake.move()
        if check_collision(snake.positions[0], food.position):
            snake.grow()
            food.randomize_position()
            score += 10
        for position in snake.positions[1:]:
            if check_collision(snake.positions[0], position):
                score = 0
                snake.reset()

        # Drawn on th screen 
        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        pygame.display.set_caption("Snake Game | Score: " + str(score))
        pygame.display.update()

        # limit game speed
        clock.tick(SPEED)

# main
if __name__ == '__main__':
    main()