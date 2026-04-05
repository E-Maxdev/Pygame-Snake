import pygame

from enum import Enum

from settings import *
from color import *

from grid import Grid
from player import Player
from food import Food

class GameState(Enum):
    MAINMENU = 0
    GAME = 1

class Main:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake")

        self.grid = Grid(self.screen)
        self.player = Player()
        self.food = Food(self.grid)

        self.playbutton_rect = pygame.Rect(WIDTH // 2 - 225, 450, 450, 100)

        self.running = True
        self.gamestate = GameState.MAINMENU

    def run(self):
        while self.running:
            
            self.events()

            match self.gamestate:
                case GameState.MAINMENU:
                    self.draw_mainmenu()
                case GameState.GAME:
                    self.draw_game()

                    self.player.get_input()
                    if self.player.move(self.grid, self.food) == False:
                        self.reset()
                    

            

    def draw_game(self):
        self.screen.fill((DARK_GREY))

        # Score Text
        score_font = pygame.font.Font("assets/font.ttf", 60)

        score_surface = score_font.render(f"SCORE: {self.player.get_score()}", True, WHITE)
        score_x = (WIDTH - score_surface.get_width()) // 2
        score_y = 10
        self.screen.blit(score_surface, (score_x, score_y))

        self.grid.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playbutton_rect.collidepoint(event.pos):
                    self.gamestate = GameState.GAME

    def reset(self):
        self.grid = Grid(self.screen)
        self.player = Player()
        self.food = Food(self.grid)

        self.gamestate = GameState.MAINMENU

    def draw_mainmenu(self):
        self.screen.fill((DARK_GREY))

        # SNAKE text
        title_font = pygame.font.Font("assets/font.ttf", 90)

        title_surface = title_font.render("SNAKE", True, WHITE)
        title_x = (WIDTH - title_surface.get_width()) // 2
        self.screen.blit(title_surface, (title_x, 300))

        # Play Button Text
        playfont = pygame.font.Font("assets/font.ttf", 70)

        playtext_surface = playfont.render("PLAY", True, WHITE)
        playtext_x = self.playbutton_rect.centerx - playtext_surface.get_width() // 2
        playtext_y = self.playbutton_rect.centery - playtext_surface.get_height() // 2
        self.screen.blit(playtext_surface, (playtext_x, playtext_y))

        # Play Button
        pygame.draw.rect(self.screen, WHITE, self.playbutton_rect, 2, border_radius=10)

        pygame.display.flip()
        self.clock.tick(60) 

Main().run()