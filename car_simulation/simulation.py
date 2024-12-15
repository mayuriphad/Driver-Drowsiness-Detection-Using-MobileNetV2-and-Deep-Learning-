import pygame

def run_car_simulation():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Car Simulation")

    # Load the car and road images
    try:
        car = pygame.image.load('car.png')
        road = pygame.image.load('road.jpg')  # Load the road image
    except pygame.error as e:
        print(f"Error loading image: {e}")
        return

    # Scale the road image to fit the entire window
    road = pygame.transform.scale(road, (800, 600))

    # Initial positions
    car_x, car_y = 330, 200  # Position the car at the bottom
    road_y = 0  # Start the road at the top
    speed = 10
    running = True

    # Set up clock for frame rate control
    clock = pygame.time.Clock()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move the road vertically
        road_y += speed

        # If the road goes off the screen, reset its position
        if road_y > 0:
            road_y = -600  # Start from the top again

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the road at the current position
        screen.blit(road, (0, road_y))
        screen.blit(road, (0, road_y + 600))  # Draw a second road image to cover the whole window

        # Draw the car on top of the road
        screen.blit(car, (car_x, car_y))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(60)

    pygame.quit()

# Run the simulation with the car stationary and road moving
run_car_simulation()
