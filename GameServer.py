import threading 
import pygame
import socket
import sys
import random  # Import random for generating random colors and positions

name = "test"
posx = 200
posy = 550

# Add this function to generate random colors
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def GameThread():
    pygame.init()
    background = (204, 230, 255)
    shapeColor = (0, 51, 204)
    shapeColorOver = (255, 0, 204)
    
    fps = pygame.time.Clock()
    screen_size = screen_width, screen_height = 400, 600
    rect1 = pygame.Rect(0, 0, 50, 50)  # This is no longer used for drawing but still tracks position
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Welcome to CCN games')
    
    colorRect = (shapeColor)
    colorRect2 = (shapeColorOver)
    global posx 
    global posy 

    while True:
        # Initialize points counter
        points = 0
        font = pygame.font.Font(None, 36)  # Default font, size 36

        # List to store falling squares
        falling_squares = []

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Add a new falling square only if there are fewer than 2 on the screen
            if len(falling_squares) < 2 and random.randint(1, 50) == 1:  # Increase the range to make squares appear less frequently
                square_x = random.randint(0, screen_width - 25)
                square_color = random_color()
                falling_squares.append({'rect': pygame.Rect(square_x, 0, 25, 25), 'color': square_color})

            # Update positions of falling squares
            for square in falling_squares:
                square['rect'].y += 2 + points // 5  # Base speed is 2, increases by 1 every 5 points

            # Check for collisions between the circle and falling squares
            circle_rect = pygame.Rect(posx - 24, posy - 24, 48, 48)  # Create a rectangle around the circle
            for square in falling_squares:
                if circle_rect.colliderect(square['rect']):
                    points += 1  # Increment points
                    falling_squares.remove(square)  # Remove the square upon collision

            # Remove squares that have reached the bottom and prompt for restart
            for square in falling_squares[:]:
                if square['rect'].y >= screen_height:
                    # Display "Game Over" and restart prompt
                    screen.fill(background)
                    game_over_text = font.render("Game Over!", True, (255, 0, 0))  # Red text
                    restart_text = font.render("Press Y to Restart or N to Quit", True, (0, 0, 0))  # Black text
                    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - 50))
                    screen.blit(restart_text, (screen_width // 2 - restart_text.get_width() // 2, screen_height // 2 + 10))
                    pygame.display.update()

                    # Wait for user input
                    waiting_for_input = True
                    while waiting_for_input:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_y:  # Restart the game
                                    return
                                elif event.key == pygame.K_n:  # Quit the game
                                    pygame.quit()
                                    sys.exit()

            screen.fill(background)

            # Draw the controlled circle
            pygame.draw.circle(screen, colorRect, (posx, posy), 24)  # Draw a circle with radius 12

            # Draw falling squares
            for square in falling_squares:
                pygame.draw.rect(screen, square['color'], square['rect'])

            # Render and display the points counter
            points_text = font.render(f"Points: {points}", True, (0, 0, 0))  # Black text
            screen.blit(points_text, (screen_width // 2 - points_text.get_width() // 2, 10))  # Centered at the top

            pygame.display.update()
            fps.tick(60)

    pygame.quit()


def ServerThread():
    global posy
    global posx
    # get the hostname
    host = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()
    print(host)
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    print("Server enabled...")
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))    
    while True:        
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        
        print("from connected user: " + str(data))
        if(data == 'w'):
            posy -= 20
        if(data == 's'):
            posy += 20
        if(data == 'a'):
            posx -= 20
        if(data == 'd'):
            posx += 20
    conn.close()  # close the connection


t1 = threading.Thread(target=GameThread, args=[])
t2 = threading.Thread(target=ServerThread, args=[])
t1.start()
t2.start()