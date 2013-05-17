import pygame, sys, os, paddle, ball

pygame.init()
pygame.font.init()

font = pygame.font.Font(None, 30)

window_size = (640, 480)

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pypong")

screen = pygame.display.get_surface()
background = pygame.Surface(window_size)
clock = pygame.time.Clock()

borders = pygame.sprite.Group()
top_border = pygame.Rect(0, 0, window_size[0], 15)
bottom_border = pygame.Rect(0, window_size[1]-15, window_size[0], 15)
left_border = pygame.Rect(0, 15, 10, window_size[1]-30)
right_border = pygame.Rect(window_size[0]-10, 15, 10, window_size[1]-30)
background.fill((0, 0, 0), left_border)
background.fill((0, 0, 0), right_border)
background.fill((255, 255, 255), top_border)
background.fill((255, 255, 255), bottom_border)
screen.blit(background, (0, 0))

paddles = pygame.sprite.Group()
player = paddle.Paddle((30, window_size[1]/2), paddles)
computer = paddle.Paddle((window_size[0]-30, window_size[1]/2), paddles)

balls = pygame.sprite.Group()
main_ball = ball.Ball((window_size[0]/2,window_size[1]/2), balls)

player_score = 0
computer_score = 0

def reset():
    global main_ball
    balls.remove(main_ball)
    main_ball = ball.Ball((window_size[0]/2, window_size[1]/2), balls)

def check_collisions():
    for ball in balls:
        for paddle in paddles:
            if ball.rect.colliderect(paddle.rect):
                ball.collide(True)
        if ball.rect.colliderect(top_border) or ball.rect.colliderect(bottom_border):
            ball.collide(False)
        elif ball.rect.colliderect(left_border):
            global computer_score
            computer_score += 1
            reset() 
        elif ball.rect.colliderect(right_border):
            global player_score
            player_score += 1
            reset()

while True:
    time_passed = clock.tick(60)
    for event in pygame.event.get():
        print event
        if event.type == pygame.QUIT:
            print "Quit"
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.speed = -3
            elif event.key == pygame.K_DOWN:
                player.speed = 3
            elif event.key == pygame.K_w:
                computer.speed = -3
            elif event.key == pygame.K_s:
                computer.speed = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.speed = 0
            elif event.key == pygame.K_DOWN:
                player.speed = 0
            elif event.key == pygame.K_w:
                computer.speed = 0
            elif event.key == pygame.K_s:
                computer.speed = 0
    paddles.update()
    balls.update()
    check_collisions()
    paddles.clear(screen, background)
    balls.clear(screen, background)
    background.fill((255, 255, 255), top_border)
    screen.blit(background, (0, 0))
    paddles.draw(screen)
    balls.draw(screen)
    font_surface = font.render(str(player_score) + "    " + str(computer_score), 0, (0, 0, 0))
    screen.blit(font_surface, (window_size[0]/2 - 30, -3))
    pygame.display.flip()
