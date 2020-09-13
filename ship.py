import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen # Obtiene el object de main screen.
        self.screen_rect = ai_game.screen.get_rect() # Obtengo la forma de object screen.
        self.settings = ai_game.settings # pass reference object settings.

        #Load the ship game and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() # Obtengo su forma en un rectangulo
        #Start each new ship at the button center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom # Devuelve las coordenadas del punto media de parte de button del whole screen.

        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x) # Integer -> Float

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    
    def update(self): # Encargar de ajustar el moviento de la nave
        """Update the ship's position based on the movement flag"""
        #Update the ship's x value, not the rect.
        #Solo mueve la nave si se presiona la tecla right/left y no pasado borders screen.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # move the ship to the right.
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x.
        self.rect.x = self.x # casting implicito float -> int
        



    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect) # Pass imagen and position initial.



