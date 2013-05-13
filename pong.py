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
background.fill((255,255,255), top_border)
background.fill((255,255,255), bottom_border)
screen.blit(background, (0, 0))

paddles = pygame.sprite.Group()
player = paddle.Paddle((30, window_size[1]/2), paddles)
computer = paddle.Paddle((window_size[0]-30, window_size[1]/2), paddles)

balls = pygame.sprite.Group()
main_ball = ball.Ball((window_size[0]/2,window_size[1]/2), balls)

def check_collisions():
    for ball in balls:
        for paddle in paddles:
            if ball.rect.colliderect(paddle.rect):
                ball.collide(True)
        if ball.rect.colliderect(top_border) or ball.rect.colliderect(bottom_border):
            ball.collide(False)

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
    check_collisions()
    paddles.clear(screen, background)
    balls.clear(screen, background)
    paddles.draw(screen)
    balls.draw(screen)
    pygame.display.flip()
