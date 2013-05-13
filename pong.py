import pygame, sys, os, paddle, ball

pygame.init()

window_size = (640, 480)

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Pypong")

screen = pygame.display.get_surface()
background = pygame.Surface(window_size)
clock = pygame.time.Clock()

borders = pygame.sprite.Group()
top_border = pygame.Rect(0, 0, window_size[0], 15)
bottom_border = pygame.Rect(0, window_size[1]-15, window_size[0], 15)

paddles = pygame.sprite.Group()
player = paddle.Paddle((30, window_size[1]/2), (paddles, borders))
computer = paddle.Paddle((window_size[0]-30, window_size[1]/2), (paddles, borders))

balls = pygame.sprite.Group()
main_ball = ball.Ball((window_size[0]/2,window_size[1]/2), balls)

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.speed = 0
            elif event.key == pygame.K_DOWN:
                player.speed = 0
    paddles.update()
    balls.update()
    paddles.clear(screen, background)
    balls.clear(screen, background)
    paddles.draw(screen)
    balls.draw(screen)
    pygame.display.flip()
