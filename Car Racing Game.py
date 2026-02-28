import pygame
import random
import xml.etree.ElementTree as ET

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("Car Racing Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT))






#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)   
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Parse XML file for car data
tree = ET.parse('cars.xml')
root = tree.getroot()

# Load spritesheet referenced by the XML (adjust filename as needed)
spritesheet = pygame.image.load('cars.png').convert_alpha()

# Create a dictionary to store vehicle sprites
vehicles = {}
for subtexture in root.findall('subtexture'):
    name = subtexture.get('name')
    x = int(subtexture.get('x'))
    y = int(subtexture.get('y'))
    width = int(subtexture.get('width'))
    height = int(subtexture.get('height'))
    vehicles[name] = (x, y, width, height)

# Car properties
player_car_name = "car1"  # Change this to the desired car name from the XML
player_car_rect = vehicles[player_car_name]
CAR_WIDTH = 60
CAR_HEIGHT = 100 
player_car = pygame.Surface((player_car_rect[2], player_car_rect[3]), pygame.SRCALPHA)
player_car.blit(spritesheet, (0, 0), player_car_rect)
player_car = pygame.transform.scale(player_car, (CAR_WIDTH, CAR_HEIGHT))

# Lane properties
LANE_COUNT = 4
LANE_WIDTH = WIDTH // LANE_COUNT
currnet_lane = LANE_COUNT // 2
car_x = currnet_lane * LANE_WIDTH + (LANE_WIDTH - CAR_WIDTH) // 2
car_y = HEIGHT - CAR_HEIGHT - 20

# Obstacle properties
OBSTACLE_WIDTH = 60
OBSTACLE_HEIGHT = 100
obstacle_speed = 5
obstacles = []

# Road properties
road_y = 0
road_speed = 5

# Game variables
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)

# Game states
Playing = 0
Game_Over = 1
game_state = Playing

def get_random_car():
    car_name = random.choice(list(vehicles.keys()))
    car_rect = vehicles[car_name]
    car_image = pygame.Surface((car_rect[2], car_rect[3]), pygame.SRCALPHA)
    car_image.blit(spritesheet, (0, 0), car_rect)
    return pygame.transform.scale(car_image, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

def show_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def draw_game_over():
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
overlay.fill((0, 0, 0, 180))  # Semi-transparent black
screen.blit(overlay, (0, 0))

game_over_text = large_font.render("Game Over", True, WHITE)
score_text = font.render(f"Final Score: {score}", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 10))

restart_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
pygame.draw.rect(screen, GREEN, restart_button)
restart_text = font.render("Restart", True, BLACK)
screen.blit(restart_button.centerx - restart_text.get_width() // 2, restart_button.centery - restart_text.get_height() // 2)
return restart_button


def reset_game():
    global currnet_lane, car_x, car_y, obstacles, score, game_state, road_y
    currnet_lane = LANE_COUNT // 2
    car_x = currnet_lane * LANE_WIDTH + (LANE_WIDTH - CAR_WIDTH) // 2
    car_y = HEIGHT - CAR_HEIGHT - 20
    obstacles = []
    score = 0
    game_state = Playing
    road_y = 0

# Game loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_state == Playing:
            if event.key == pygame.K_LEFT and currnet_lane > 0:
                currnet_lane -= 1
            elif event.key == pygame.K_RIGHT and currnet_lane < LANE_COUNT - 1:
                currnet_lane += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and game_state == Game_Over:
            mouse_pos = pygame.mouse.get_pos()
            if restart_button.collidepoint(mouse_pos):
                reset_game()

if game_state == Playing:
    # Update car position
    target_x = currnet_lane * LANE_WIDTH + (LANE_WIDTH - CAR_WIDTH) // 2
    car_x += (target_x - car_x) * 0.2  # create new obstacles
   if len(obstacles) < 5 and random.random() < 0.02:
        obstacle_x = random.randint(0, LANE_COUNT - 1) * LANE_WIDTH + (LANE_WIDTH - OBSTACLE_WIDTH) // 2
        obstacles.append([obstacle_x, -OBSTACLE_HEIGHT, get_random_car()])


# Check for overlap with extisting obstacles
overlap = any(any(abs(obstacle[1] - obstacle_y) < OBSTACLE_HEIGHT and abs(obstacle[0] - obstacle_x) < OBSTACLE_WIDTH for obstacle in obstacles) for obstacle_x in range(car_x, car_x + CAR_WIDTH, 10) for obstacle_y in range(car_y, car_y + CAR_HEIGHT, 10))
if not overlap:
    obstacles.append([obstacle_x, 0, get_random_car()])

    # Move and remove obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)
            score += 1
            
        # Check for collisions
        player_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
        for obstacle in obstacles:
            obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
            if player_rect.colliderect(obstacle_rect):
                game_state = Game_Over
                # Scroll the road
                road_y = (road_y + road_speed) road_image.get_height() % HEIGHT

                # clear the screen
                screen.fill(BLACK)
                # Draw the scrolling road
                screen.blit(road_image, (0, road_y - road_image.get_height()))
                screen.blit(road_image, (0, road_y))
                # Draw lane dividers
                for i in range(1, LANE_COUNT):
                    pygame.draw.line(screen, YELLOW, (i * LANE_WIDTH, 0), (i * LANE_WIDTH, HEIGHT), 2)
                # Draw the player's car
                screen.blit(player_car, (car_x, car_y))
                # Draw obstacles
                for obstacle in obstacles:
                    screen.blit(obstacle[2], (obstacle[0], obstacle[1]))
                    
            # show the score
            show_score()
elif game_state == Game_Over:
    restart_button = draw_game_over()


# Update the display
pygame.display.flip()

# Control the game speed
clock.tick(60)

# Quit the game
pygame.quit()


