# pygame-background-scene
# Henry Roeser
# 3/5/25

import pygame
import sys
import config # Import the config module
import shapes # Import the shapes module


def init_game():  # Initialize game screen
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

# Function to draw a rectangle across the screen
def draw_rectangle(screen, rect, color, thickness):  # Draws a rectangle on the pygame window
    pygame.draw.rect(screen, config.DARKGREEN, (0, config.WINDOW_HEIGHT  - 155, config.WINDOW_WIDTH, 250))

# Function draw a square
def draw_square(screen, square_pos, square_size, square_color):
    pygame.draw.rect(screen, square_color, (square_pos[0], square_pos[1], square_size, square_size))

# Function to draw a circle
def draw_circle(screen, center, radius, color, thickness):  # Draws a circle on the pygame window
    pygame.draw.circle(screen, color, center, radius, thickness)


# Function to draw a line
def draw_line(screen, color, start_pos, end_pos, thickness):  # Draws a line on the pygame window
    pygame.draw.line(screen, color, start_pos, end_pos, thickness)

# Function to draw text
def draw_text(screen, text, font, text_col, x, y, bold=True, italic=True):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False  # Return False to indicate quitting
    return True  # Continue running if no quit event

# Function to draw a polygon
def draw_polygon(screen, color, points, thickness = 0): # default thickness of 0 will fill the polygon with color
    pygame.draw.polygon(screen, color, points, thickness)

def main():
    screen = init_game()
    clock = pygame.time.Clock()  # Initialize the clock

    running = True
    while running:
        running = handle_events()
        screen.fill(config.BLUE)  # Use color from config

        text_font3 = pygame.font.SysFont('Times New Roman', 55, bold=True, italic=True) # System font

        # Draw a green rectangle with thickness of 8 pixels (The grass)
        my_rect1 = [400, 400, 400, 400]
        thickness1 = 0
        draw_rectangle(screen, my_rect1, config.DARKGREEN, thickness1)

        # Draw a filled yellow circle (The sun)
        circle_center = (700, 95)  # Center point of the circle (x, y)
        circle_radius = 50  # Radius of circle
        circle_color = config.YELLOW  # Color of circle
        circle_thickness = 0  # 0 pixels creates a filled circle
        draw_circle(screen, circle_center, circle_radius, circle_color, circle_thickness)

        # Draw a polygon (The tree)
        pygame.draw.rect(screen, config.BROWN, [60, 400, 30, 45])
        polygon1_points = [[150, 400], [75, 250], [0, 400]]
        draw_polygon(screen, config.GREEN, polygon1_points)

        polygon2_points = [[140, 350], [75, 230], [10, 350]]
        draw_polygon(screen, config.GREEN, polygon2_points)

        # Draw a square (The house)
        square_pos = (300, 270)
        square_size = 175
        square_color = config.BROWN
        draw_square(screen, square_pos, square_size, square_color)

        # Draw brown triangle (Roof on house)
        polygon3_points = [[475, 270], [300, 270], [385, 200]]
        draw_polygon(screen, config.BROWN, polygon3_points)

        # Draw black rectangle (Door on house)
        pygame.draw.rect(screen, config.BLACK, [363, 370, 50, 75])

        # Draw text
        draw_text(screen, 'Hello World',text_font3, config.RED, 250, 450, bold=True, italic=True)

        # Draw a black line with thickness of 5 pixels
        draw_line(screen, config.BLACK, [300, 275], [475, 275], 5)
        draw_line(screen, config.BLACK, [300, 300], [475, 300], 5)
        draw_line(screen, config.BLACK, [300, 325], [475, 325], 5)
        draw_line(screen, config.BLACK, [300, 350], [475, 350], 5)
        draw_line(screen, config.BLACK, [300, 375], [475, 375], 5)
        draw_line(screen, config.BLACK, [300, 400], [475, 400], 5)
        draw_line(screen, config.BLACK, [300, 425], [475, 425], 5)
        draw_line(screen, config.BLACK, [340, 275], [340, 445], 5)
        draw_line(screen, config.BLACK, [388, 275], [388, 440], 5)
        draw_line(screen, config.BLACK, [435, 275], [435, 445], 5)

        polygon4_points = [[550, 445], [650, 445], [600, 390]]
        draw_polygon(screen, config.WHITE, polygon4_points)
        polygon5_points = [[500, 445], [600, 445], [550, 410]]
        draw_polygon(screen, config.WHITE, polygon5_points)
        polygon6_points = [[600, 445], [700, 445], [650, 410]]
        draw_polygon(screen, config.WHITE, polygon6_points)

        # update the window display
        pygame.display.flip()

        clock.tick(config.FPS)  # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
