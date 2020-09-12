import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen # Obtiene el object de main screen.
        self.screen_rect = ai_game.screen.get_rect() # Obtengo la forma de object screen.

        #Load the ship game and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # Obtengo su forma en un rectangulo
        #Start each new ship at the button center of the screen.
        self.rect.midbutton = self.screen_rect.midbutton # Devuelve las coordenadas del punto media de parte de button del whole screen.

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect) # Pass imagen and position initial.



