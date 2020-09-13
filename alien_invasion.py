import sys # Para controlar la salida del juego
import pygame
from settings import Settings # Importamos la clase Settings del module settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create resource"""
        pygame.init() # Crea los componentes de pygame para que funcione apropiadamente.
        self.settings = Settings() # crea una instancia de la Clase Settings.

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height) ) # Devuelve un objeto called surface que representa un componente en la pantalla, de tamaño 1200x800.
        pygame.display.set_caption("Alien Invasion") # Ajusta el title

        self.ship = Ship(self) # Create instance of ship form game and pass argumnt the instance.


    def run_game(self):
        """Start the main loop for the game"""

        while True: # Conocido como el patter game para update the game every frame.
            # Reafactor code with method for encapsuling complexity.
            self._check_events() # Listenner events.
            self.ship.update() # Move ship. 
            self._update_screen() # Dibujar components game.


    def _check_events(self):
        """Respond to keypresses and mouse event"""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get(): # Devuelve una lista de eventos generada cada vez que entra al loop.
            if event.type == pygame.QUIT: # Evento generado cuando se cierra la pantalla
                sys,exit() # Termina la ejecucion del programa.

            elif event.type == pygame.KEYDOWN: # Dectecta si una tecla es presionada hacia abajo.
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP: # Detecta si una tecla es soltada
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT: # Identifica que tipo de letra es.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q: # Add alternative way for fished the game.
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT: # Identifica el tipo de letra soltada.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False



    def _update_screen(self):
        # Redraw the screen during each pass through the looṕ
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() # Draw ship

        # Make the most recently draw screen visible.
        pygame.display.flip() # udpate screen and borrow old screen.



if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game();

