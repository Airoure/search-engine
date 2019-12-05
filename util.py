import pygame

class Controller:
    def __init__(self,title):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.title=title
        self.fps=30