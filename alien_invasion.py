import sys # Para controlar la salida del juego
import pygame
from settings import Settings # Importamos la clase Settings del module settings


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create resource"""
        pygame.init() # Crea los componentes de pygame para que funcione apropiadamente.
        self.settings = Settings() # crea una instancia de la Clase Settings.

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height) ) # Devuelve un objeto called surface que representa un componente en la pantalla, de tamaño 1200x800.
        pygame.display.set_caption("Alien Invasion") # Ajusta el title


    def run_game(self):
        """Start the main loop for the game"""

        while True: # Conocido como el patter game para update the game every frame.
            # Watch for keyboard and mouse events.
            for event in pygame.event.get(): # Devuelve una lista de eventos generada cada vez que entra al loop.
                if event.type == pygame.QUIT: # Evento generado cuando se cierra la pantalla
                    sys,exit() # Termina la ejecucion del programa.

            # Redraw the screen during each pass through the looṕ
            self.screen.fill(self.settings.bg_color)

            # Make the most recently draw screen visible.
            pygame.display.flip() # udpate screen and borrow old screen.


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game();


        
