import pygame
import time
import random

pygame.init()

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)  # Черный цвет для счетчика
red = (213, 50, 80)  # Цвет змейки
dark_orange = (0, 255, 0)  #Цвет фона
orange = (255, 165, 0)  # Оранжевая еда

# Размеры экрана
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

# Настройки змейки
snake_block = 10
snake_speed = 15

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    """Отображение текущего счета."""
    value = score_font.render("Ваш счет: " + str(score), True, black)  # Изменен цвет на черный
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    """Отрисовка змейки."""
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])  # Красная змейка

def message(msg, color):
    """Отображение сообщения."""
    mesg = font_style.render(msg, True, color)
    # Центрируем текст по горизонтали
    text_width = mesg.get_width()
    text_height = mesg.get_height()
    dis.blit(mesg, [(dis_width - text_width) / 2, (dis_height - text_height) / 2])

def gameLoop():
    """Основной игровой цикл."""
    game_over = False
    game_close = False

    # Начальные координаты змейки
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Изменение координат
    x1_change = 0
    y1_change = 0

    # Змейка и начальная длина
    snake_List = []
    Length_of_snake = 1

    # Координаты еды
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(dark_orange)  # Темно-оранжевый фон при окончании игры
            message("Вы проиграли! Нажмите Q для выхода или C для повторения игры", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                elif event.key == pygame.K_ESCAPE:
                    game_over = True

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Обновление координат змейки
        x1 += x1_change
        y1 += y1_change

        # Отрисовка фона и еды
        dis.fill(dark_orange)  # Темно-оранжевый фон во время игры
        pygame.draw.rect(dis, orange, [foodx, foody, snake_block, snake_block])  # Оранжевая еда

        # Обновление тела змейки
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение с самим собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        # Проверка на съедание еды
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Запуск игры
gameLoop()