# Alien Invasion Game

import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # adding code below will help with frame rate of the game
        self.clock = pygame.time.Clock()

        # making an instance of settings in project
        self.settings = Settings()
        # Full screen mode undo hashtags below
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #elf.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height


        # set background color
        # self.bg_color = (230, 230, 230)  now in settings module

        # Create a  window on which the games graphical elements are drawn the argument (1200, 800) is a tuple that defines dimension of game window

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        # This gives the Ship access to the games resources
        self.ship = Ship(self)

        # Create group that holds bullets
        self.bullets = pygame.sprite.Group()

        # initializing Alien
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        # for loop nested in while loop is the event loop
        while True:
            # To isolate the event management loop. Grants ability to manage events separately from other game aspects
            self._check_events()
            self.ship.update()
            self._update_bullets()
            

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
            # Update bullet position
            # Update the position of the bullets on each pass through the while loop
        self.bullets.update()
         
            # Get rid of bullets that have diappeared. 
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

        self._update_screen()
        self.clock.tick(60)

    def _check_events(self):
            # Watch for keyboard and mouse events. 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                    
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
                
                     
                        # move the ship to the right.
                self.ship.rect.x += 1
                    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            print("Quit Pressed") #debug message
            sys.exit()
        elif event.key == pygame.K_SPACE:
            print("Spacebar Pressed") #debug message
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False   
        
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            

    def _create_fleet(self):
        """Creates fleet of Aliens. """
        # Create an alien and keep addling aliens until there's no room left.
        #Spacing between aliens is one alien width
        alien = Alien(self)
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            new_alien = Alien(self)
            new_alien.x = current_x
            new_alien.rect.x = current_x
            self.aliens.add(alien)
            current_x +=2 * alien_width


    def _update_screen(self):

            # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()

        # To make alien ships appear nead to call the draw() method for screen
        self.aliens.draw(self.screen)

            # Make the most recently drawn screen visible.
        pygame.display.flip()

            # To make clock tick at the end of the game 
            # self.clock.tick(60) --> now earlier in the code

if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()