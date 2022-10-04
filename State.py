from random import randrange
from re import I
from FrameBasedAnimation import FrameBasedAnimation
from keyboard import is_key_down
import pygame
from Circle import Circle
from Avatar import Avatar
from Background import Background
from Bullet import Bullet
from Zombie import Zombie
from Music import Sounds
from Score import Score
from Powerups import Powerups
from subprocess import Popen
from Lives import Lives

class State:
    def __init__(self):
        Sounds.begin_level.play()
        self.quit_tijd = 0
        self.death_loop = False
        self.circle = Circle()
        self.bullets = []
        self.shiet_delay = 15
        self.shiet_wacht = 0
        self.animations = []
        self.avatar = Avatar()
        self.score = Score()
        self.lives = Lives()
        self.__background = Background()
        self.pause = False
        self.powerups = []
        self.powerup_wait_timer = 1500
        self.heeft_power_up = False
        self.heeft_power_up_type = 0
        self.heeft_power_up_timer = 0
        
        self.zombies = []
        self.max_zombies = 6
        self.zombie_spawn_delay = 200
        self.zombie_spawn_delay_counter = 0
        self.zombie_update_amount_score = 10

        self.speed_avatar = 4
        self.speed_bullet = 8

        # Nodig voor immunity frames
        self.collision_immune = False
        self.collision_time = pygame.time.get_ticks()
        self.nuke = False
    
    def update(self, tijd):
        self.tijd = tijd*100
        
        self.x_avatar = self.speed_avatar * self.tijd
        self.y_avatar = self.speed_avatar * self.tijd
        
        self.x_bullet = self.speed_bullet * self.tijd
        self.y_bullet = self.speed_bullet * self.tijd

        # Update positie van background
        self.__background.update(tijd*100)

        # Coördinaten avatar meegeven
        if is_key_down(pygame.K_RIGHT):
            if self.avatar.x_cord <= 1106:
                self.avatar.update(self.avatar.x_cord+self.x_avatar, self.avatar.y_cord)
        elif is_key_down(pygame.K_LEFT):
            if self.avatar.x_cord >= 0:
                self.avatar.update(self.avatar.x_cord-self.x_avatar, self.avatar.y_cord)
        elif is_key_down(pygame.K_UP):
            if self.avatar.y_cord >=0:
                self.avatar.update(self.avatar.x_cord, self.avatar.y_cord-self.y_avatar)
        elif is_key_down(pygame.K_DOWN):
            if self.avatar.y_cord <= 696:
                self.avatar.update(self.avatar.x_cord, self.avatar.y_cord+self.y_avatar)
        
        # Schieten
        if self.shiet_wacht>0:
                self.shiet_wacht-=self.tijd

        def schiet_pea():
            Sounds.splat.play()
            nieuwe_bullet = Bullet(self.avatar.x_cord, self.avatar.y_cord)
            self.bullets.append(nieuwe_bullet)
            self.shiet_wacht = self.shiet_delay
            if self.heeft_power_up==True and self.heeft_power_up_type==2:
                nieuwe_bullet = Bullet(self.avatar.x_cord, self.avatar.y_cord-50)
                self.bullets.append(nieuwe_bullet)
                nieuwe_bullet = Bullet(self.avatar.x_cord, self.avatar.y_cord+50)
                self.bullets.append(nieuwe_bullet)

        if is_key_down(pygame.K_SPACE):
            if self.shiet_wacht <= 0:
                schiet_pea()

        for self.bullet in self.bullets:
            if self.bullet.x_cord > 1240:
                self.bullets.remove(self.bullet)
            self.bullet.update(self.bullet.x_cord+self.x_bullet, self.bullet.y_cord)

        # Spawn zombie na delay
        if self.zombie_spawn_delay_counter <= 0:
            aantal_zombies = len(self.zombies)
            if aantal_zombies<self.max_zombies:
                nieuwe_zombie = Zombie()
                self.zombies.append(nieuwe_zombie)
                self.zombie_spawn_delay_counter = self.zombie_spawn_delay

        if self.powerup_wait_timer>0 and self.heeft_power_up == False:
            self.powerup_wait_timer-=self.tijd

        if len(self.powerups)<1 and self.powerup_wait_timer<=1:
            nieuw_powerup = Powerups()
            self.powerups.append(nieuw_powerup)
            
        for powerup in self.powerups:
            powerup.update(powerup.x_cord, powerup.y_cord + 1)
            if powerup.y_cord>850:
                self.powerups.remove(powerup)
                self.powerup_wait_timer = 1500
            
            if check_collision(powerup.y_hitbox_min, powerup.y_hitbox_max, powerup.x_hitbox_min, powerup.x_hitbox_max, self.avatar.y_hitbox_min, self.avatar.y_hitbox_max, self.avatar.x_hitbox_min, self.avatar.x_hitbox_max):
                self.heeft_power_up = True
                self.heeft_power_up_type = powerup.powerup_type
                self.heeft_power_up_timer = 1000
                self.powerups.remove(powerup)
                self.powerup_wait_timer = 1500
                 
        if self.heeft_power_up_timer<=1:
            self.heeft_power_up = False
            self.avatar.changeImage(0)
            self.speed_bullet = 8
            self.shiet_delay = 15
            self.collision_immune = False

        if self.heeft_power_up==True:
            self.heeft_power_up_timer-=self.tijd

            if self.heeft_power_up_type == 1:
                # machine gun Avatar
                self.avatar.changeImage(1)
                self.speed_bullet = 16
                self.shiet_delay = 7.5
            if self.heeft_power_up_type == 2:
                # cone shooter
                self.avatar.changeImage(2)
            if self.heeft_power_up_type == 3:
                # imunity shooter
                self.avatar.changeImage(3)
                self.collision_immune = True
                
        
        if self.zombie_spawn_delay_counter>0:
            self.zombie_spawn_delay_counter-=self.tijd

        # Moeilijkheid verhogen
        
        if self.score.score >= self.zombie_update_amount_score:
            if self.score.score<=90:
                self.max_zombies+=1
                self.zombie_update_amount_score+=10
                self.zombie_spawn_delay-=self.zombie_spawn_delay/8
            if 91<=self.score.score<=140:
                self.max_zombies+=0.5
                self.zombie_update_amount_score+=10
                self.zombie_spawn_delay-=self.zombie_spawn_delay/10
            if 141<=self.score.score:
                self.max_zombies+=0.25
                self.zombie_update_amount_score+=10
                self.zombie_spawn_delay-=self.zombie_spawn_delay/15



        # Animatie bij doodgaan
        if self.death_loop == True:
            random_x=randrange(1200)
            random_y=randrange(800)
            frames_explosie = [pygame.image.load(f'explosion/{i}.png') for i in range(1, 10)]
            nieuwe_explosie = FrameBasedAnimation(frames_explosie, (random_x, random_y))
            self.animations.append(nieuwe_explosie)
            Sounds.game_over.play()
            if self.quit_tijd >= 300:
                Popen('python End_screen.py')
                pygame.quit()
            else:
                self.quit_tijd += self.tijd

        # Animatie als zombie einde bereikt
        for zombie in self.zombies:
            if zombie.x_cord <= 0:
                self.death_loop = True
            
            zombie.update(self.tijd)

        # Collision detection met kogels
        for zombie in self.zombies:
            for bulet in self.bullets:
                if check_collision(zombie.y_hitbox_min,zombie.y_hitbox_max,zombie.x_hitbox_min,zombie.x_hitbox_max, bulet.y_hitbox_min, bulet.y_hitbox_max, bulet.x_hitbox_min,bulet.x_hitbox_max):
                    # Aantal frames waar zombie rood kleurt bij hit
                    zombie.hit_counter = 5

                    self.bullets.remove(bulet)
                    zombie.lifes-=1

                    # Animatie als zombie sterft
                    if zombie.lifes == 0:
                        self.score.update(self.score.score+zombie.score_reward)
                        self.zombies.remove(zombie)
                        
                        frames_explosie = [pygame.image.load(f'explosion/{i}.png') for i in range(1, 10)]
                        nieuwe_explosie = FrameBasedAnimation(frames_explosie, (zombie.x_cord+50, zombie.y_cord+70))
                        self.animations.append(nieuwe_explosie)
                        Sounds.explosion.play()
        
        # Collision detection met speler
        for zombie in self.zombies:
            if check_collision(zombie.y_hitbox_min,zombie.y_hitbox_max,zombie.x_hitbox_min,zombie.x_hitbox_max, self.avatar.y_hitbox_min, self.avatar.y_hitbox_max, self.avatar.x_hitbox_min,self.avatar.x_hitbox_max):
                if self.avatar.lives != 0 and self.collision_immune == False:
                    self.avatar.lives -= 1
                    self.score.score -= 25
                    # Alle zombies verwijderen via nuke als speler leven verliest
                    self.nuke = True
                    self.collision_time = pygame.time.get_ticks()
                    self.lives.update(self.avatar.lives)
                elif self.avatar.lives != 0 and self.heeft_power_up == True and self.heeft_power_up_type == 3:
                    self.nuke = True
                    self.heeft_power_up_timer = 0
                elif self.avatar.lives == 0:
                    # Animatie als speler sterft
                    self.death_loop = True
                    
        # Alle zombies verwijderen    
        if self.nuke == True:
            for zombie in self.zombies:
                frames_explosie = [pygame.image.load(f'explosion/{i}.png') for i in range(1, 10)]
                nieuwe_explosie = FrameBasedAnimation(frames_explosie, (zombie.x_cord+50, zombie.y_cord+70))
                self.animations.append(nieuwe_explosie)
                Sounds.explosion.play()
            self.zombies = []
            self.nuke = False

        for explosie in self.animations:
            explosie.update(1/7,self.tijd)
            if explosie.disposed == True:
                self.animations.remove(explosie)



        
    def render(self, surface):
        clear_surface(surface)

        self.__background.render(surface)
        self.avatar.render(surface)
        self.score.render(surface)

        for powerup in self.powerups:
            powerup.render(surface)

        self.lives.render(surface)

        for bullet in self.bullets:
            bullet.render(surface)
        
        for zombie in self.zombies:
            if zombie.hit_counter != 0:
                zombie.render_hit(surface)
                zombie.hit_counter-=1
            else:
                zombie.render_not_hit(surface)

        for explosie in self.animations:
            explosie.render(surface)

        # Breng back buffer naar front buffer
        pygame.display.flip()


def clear_surface(surface):
    surface.fill((0,0,0))

def check_collision(y1_min, y1_max, x1_min, x1_max, y2_min, y2_max, x2_min, x2_max):
    rect1 = pygame.Rect(x1_min, y1_min, x1_max, y1_max)
    rect2 = pygame.Rect(x2_min, y2_min, x2_max, y2_max)

    return rect1.colliderect(rect2)

