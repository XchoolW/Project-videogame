# Importing all the necesary librarys and Classes

import random
import pygame
from pygame import mixer
from GameClass import Game
import os
from PlayerClass import Player
from EnemyClass import Enemy
from DrawClass import Drawing
from ScreenNameClass import ScreenName
from MainMenuClass import MainMenu
from AboutMenuClass import About
from ScoreMenuClass import Score
from GiftClass import Gift

# Getting the current directory
current_dir = os.path.dirname(__file__)

# Constants for the game ---------------------------------------------

BACKGROUND = pygame.image.load(os.path.join(
    current_dir, 'img', 'background.png'))
ICON_IMAGE = pygame.image.load(os.path.join(
    current_dir, 'img', 'title_icon.png'))
TITLE = 'Space Invaders Proyecto Hybridge'
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
PLAYER_IMAGE = pygame.image.load(os.path.join(
    current_dir, 'img', 'player_image.png'))
COOLDOWN_TIME = 1000

pygame.display.set_caption(TITLE)

# Changing the icon in the task bar and the screen
pygame.display.set_icon(ICON_IMAGE)

# Init pygame
pygame.init()

# Loading the background music and handling the errors -------------
try:
    mixer.music.load('./sounds/background_song.mp3')
except:
    print('Sound could no be displayed')
    pass

# Main function ------------------------------------------------------
def main():
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    score = 0
    gifts = []
    gift_spawn_timer = 0  # Timer to control gift spawn rate

    # Music
    try:
        mixer.music.play(-1)
    except:
        pass

    # Setting the font
    font = pygame.font.SysFont('comicsans', 30)

    # Creating the player and its coordinates
    player_x = ((WIDTH)-(PLAYER_IMAGE.get_width())) / 2
    player_y = HEIGHT - 120

    player = Player(x=player_x, y=player_y, x_speed=5, y_speed=4)

    # Creating a game object
    game = Game(font, FPS, 3, player.health, WIN, WIDTH, HEIGHT, 3, clock)

    # Creating enemies
    enemy_init = Enemy(speed=1)
    enemy_wave = 6

    enemies = enemy_init.create(enemy_wave)

    # Drawing in the screen the past objects
    draw = Drawing(WIN)
    draw.drawing(game, player, enemies, gifts, FPS, score=0)

    # Cycle for running the game
    while run:
        clock.tick(FPS)

        # If the player exceeds the score
        if game.over():
            if score > game.max_score:

                sound = pygame.mixer.Sound('./sounds/win.mp3')
                sound.play()
                screen = ScreenName(score, main)

                pygame.quit()

            # Rerunning the code
            else:
                main_menu()
                run = False

        if game.escape():
            run = False
            continue

        # Player wins
        if len(enemies) == 0:
            game.level += 1
            enemy_wave += 2
            enemy_init.increase_speed()
            player.increase_speed()
            enemies = enemy_init.create(enemy_wave)
            new_level = True

        # If we get in level multiple of 3, we get 1 live and bullets
        if game.level % 3 == 0 and new_level == True:
            if player.max_amount_bullets < 16:
                player.max_amount_bullets += 1
            if game.lives < 8:
                game.lives += 1

            new_level = False

        # Player movement
        player.move()
        player.create_bullets()
        game.reload_bullet(len(player.bullets))
        player.cooldown()

        # Gifts for player
        gift_spawn_timer += 1  # Increase the timer with each frame
        if gift_spawn_timer > 100:  # Controls the rate at which gifts are created
            gift_spawn_timer = 0
            if random.randint(1, 100) < 5:  # 5% chance to create a gift
                gift = Gift.create()
                gifts.append(gift)

            # Move and handle gifts
            for gift in gifts[:]:
                gift.move()
                if gift.collision(player):  # Check collision with the player
                    print('Gift collected!')
                    # Remove gift from the list when collected
                    gifts.remove(gift)
                    score += 10  # Add score for collecting the gift
                    player.health += 10

                    # Conditioned reward
                    if player.max_amount_bullets < 16:
                        player.max_amount_bullets += 1
                    else:
                        score += 5

                if gift.y > HEIGHT:  # Remove gift if it goes off screen
                    gifts.remove(gift)

        # Controlling enemies
        for enemy in enemies:
            enemy.move()

            # Loading sounds for the game
            crash_sound = pygame.mixer.Sound('./sounds/crash.wav')
            shout_sound = pygame.mixer.Sound('./sounds/explosion.wav')

            # Player hit the enemy
            if player.hit(enemy):
                enemies.remove(enemy)
                player.fired_bullets.pop(0)
                score += 1
                pygame.mixer.Sound.play(shout_sound)

            # Enemy reach our "base"
            if enemy.y + enemy.get_height() >= HEIGHT:
                game.lives -= 1
                enemies.remove(enemy)
                pygame.mixer.Sound.play(crash_sound)

            # If we crash with the enemy, we get our health decreased
            if enemy.collision(player):
                player.take_damage(damage=10)
                game.health = player.health
                pygame.mixer.Sound.play(crash_sound)

            # If we get 0 health, we'll lost a live and health will restore
            if player.health == 0:
                game.lives -= 1
                player.health = 100

            # Updating the player to get the ship renew if we crashed
            player.update()

        draw.drawing(game, player, enemies, gifts, FPS, score)

# Executing the instances
def initGame():
    main()


def initScore():
    score_menu = Score(main_menu).run()


def initAbout():
    about_menu = About(main_menu).run()


def main_menu():
    main_menu = MainMenu(initGame, initScore, initAbout).main_menu()


main_menu()
