# Complete your game here
import pygame, random

class Game:
    total_coins = 10
    total_monster = 4
    game_mode = 0
    total_coins_collected = 0
    high_score = 0
    p1_coins_collected = 0
    p2_coins_collected = 0

    def __init__(self):
        pygame.init()

        self.load_images()

        self.width, self.height = 640, 530
        self.window = pygame.display.set_mode((self.width, self.height))

        self.robot_height = self.images["robot"].get_height()
        self.robot_width = self.images["robot"].get_width()

        self.coin_height = self.images["coin"].get_height()
        self.coin_width = self.images["coin"].get_width()

        self.monster_height = self.images["monster"].get_height()
        self.monster_width = self.images["monster"].get_width()

        self.game_font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption(f'{" "*90}Coins')

        self.p1_to_right = False
        self.p1_to_left = False
        self.p2_to_right = False
        self.p2_to_left = False
        self.p1_game_over = False
        self.p2_game_over = False
        self.show_high_score = False

        self.generate_starting_coins_and_monsters()

        self.p1_robot_x, self.p1_robot_y = self.width/2 - self.robot_width, self.height - self.robot_height
        self.p2_robot_x, self.p2_robot_y = self.width/2 - self.robot_width/4, self.height - self.robot_height

        self.clock = pygame.time.Clock()

        self.game_choice()
        self.main_loop()

    def load_images(self):
        self.images = {name: pygame.image.load(name + ".png") for name in ["coin", "monster", "robot"]}

    def generate_starting_coins_and_monsters(self):
        self.coins = [[random.randint(0, self.width-self.coin_width), -random.randint(0, 1000)] for i in range(Game.total_coins)]
        self.monsters = [[random.randint(0, self.width-self.monster_width), -random.randint(0, 1000)] for i in range(Game.total_monster)]

    def game_choice(self):
        running = True
        while running:
            self.window.fill((186,255,201))

            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit()
	
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_1:
                        Game.game_mode = 1
                        running = False
                    if events.key == pygame.K_2:
                        Game.game_mode = 2
                        running = False
                    if events.key == pygame.K_ESCAPE:
                        exit()

            self.create_text("1 = Single Player", self.width/2 - 148/2, self.height/4)
            self.create_text("2 = Two Players", self.width/2 - 139/2, ((self.height-self.height/2)-28))
            self.create_text("Esc = exit", self.width/2 - 86/2, ((self.height-self.height/4)-28))

            pygame.display.flip()

    def main_loop(self):
        while True:
            self.check_events()
            self.movement()
            self.collision_check()
            self.draw_window()

    def check_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_LEFT:
                    self.p1_to_left = True 
                if events.key == pygame.K_RIGHT:
                    self.p1_to_right = True

                if events.key == pygame.K_a:
                    self.p2_to_left = True
                if events.key == pygame.K_d:
                    self.p2_to_right = True

                if events.key == pygame.K_F2:
                    Game.p1_coins_collected = 0
                    Game.p2_coins_collected = 0
                    Game.total_coins_collected = 0
                    self.__init__()

                if events.key == pygame.K_ESCAPE:
                    exit()
        
            if events.type == pygame.KEYUP:
                if events.key == pygame.K_LEFT:
                    self.p1_to_left = False
                if events.key == pygame.K_RIGHT:
                    self.p1_to_right = False

                if events.key == pygame.K_a:
                    self.p2_to_left = False
                if events.key == pygame.K_d:
                    self.p2_to_right = False

    def movement(self):
        if not self.p1_game_over:
            if self.p1_to_left:
                self.p1_robot_x -= 1
            if self.p1_to_right:
                self.p1_robot_x += 1

        if not self.p2_game_over:
            if self.p2_to_left:
                self.p2_robot_x -= 1
            if self.p2_to_right:
                self.p2_robot_x += 1

        self.p1_robot_x = max(0, min(self.p1_robot_x, self.width-self.robot_width))
        self.p2_robot_x = max(0, min(self.p2_robot_x, self.width-self.robot_width))

    def collision_check(self):
        if not self.p1_game_over or not self.p2_game_over:

            if Game.game_mode == 1:
                self.p2_game_over = True

            for i in range(Game.total_coins):
                self.coins[i][1] += 1

                if (self.coins[i][1] + self.coin_height >= self.p1_robot_y and not self.p1_game_over and 
                    self.coins[i][1] + self.coin_height >= self.p2_robot_y and not self.p2_game_over and
                    self.p1_robot_x < self.coins[i][0] + self.coin_width and self.p1_robot_x + self.robot_width > self.coins[i][0] and 
                    self.p2_robot_x < self.coins[i][0] + self.coin_width and self.p2_robot_x + self.robot_width > self.coins[i][0] and
                    Game.game_mode == 2):
                        self.spawn_new_coin(i)
                        Game.p1_coins_collected += 1
                        Game.p2_coins_collected += 1

                if (self.coins[i][1] + self.coin_height >= self.p1_robot_y and not self.p1_game_over and
                    self.p1_robot_x < self.coins[i][0] + self.coin_width and self.p1_robot_x + self.robot_width > self.coins[i][0]):
                        self.spawn_new_coin(i)
                        Game.p1_coins_collected += 1
                        if Game.game_mode == 1:
                            Game.total_coins_collected += 1

                if (self.coins[i][1] + self.coin_height >= self.p2_robot_y and not self.p2_game_over and
                    self.p2_robot_x < self.coins[i][0] + self.coin_width and self.p2_robot_x + self.robot_width > self.coins[i][0] and
                    Game.game_mode == 2):
                        self.spawn_new_coin(i)
                        Game.p2_coins_collected += 1

                if self.coins[i][1] + self.coin_width > self.height:
                    self.spawn_new_coin(i)

            for i in range(Game.total_monster):
                self.monsters[i][1] += 1

                if (self.monsters[i][1] + self.monster_height >= self.p1_robot_y and
                    self.p1_robot_x < self.monsters[i][0] + self.monster_width and self.p1_robot_x + self.monster_width > self.monsters[i][0]):
                        self.p1_game_over = True
                        if Game.total_coins_collected > Game.high_score:
                            self.show_high_score = True
                            Game.high_score = Game.total_coins_collected

                if (self.monsters[i][1] + self.monster_height >= self.p2_robot_y and
                    self.p2_robot_x < self.monsters[i][0] + self.monster_width and self.p2_robot_x + self.monster_width > self.monsters[i][0]):
                        self.p2_game_over = True

                if self.monsters[i][1] + self.monster_width > self.height:
                    self.spawn_new_monster(i)

    def spawn_new_coin(self, i: int):
        self.coins[i] = [random.randint(0, self.width-self.coin_width), -random.randint(0, 1000)]

    def spawn_new_monster(self, i: int):
        self.monsters[i] = [random.randint(0, self.width-self.monster_width), -random.randint(0, 1000)]

    def draw_window(self):
        self.window.fill((251,238,229))

        for i in range(Game.total_coins):
            self.window.blit(self.images["coin"], (self.coins[i]))

        for i in range(Game.total_monster):
            self.window.blit(self.images["monster"], (self.monsters[i]))

        pygame.draw.rect(self.window, (186,225,255), (0, 0, self.width, 50))

        if Game.game_mode == 1:
            self.create_text(f"Coins: {Game.p1_coins_collected}", 25, 11)
            self.create_text(f"High Score: {Game.high_score}", self.width-151, 11)

        if Game.game_mode == 2:
            self.window.blit(self.images["robot"], (self.p2_robot_x, self.p2_robot_y))
            self.create_text("P2", self.p2_robot_x+13, self.p2_robot_y+37)

            self.create_text(f"P1 Coins: {Game.p1_coins_collected}", 25, 11)
            self.create_text(f"P2 Coins: {Game.p2_coins_collected}", self.width-133, 11)

        self.window.blit(self.images["robot"], (self.p1_robot_x, self.p1_robot_y))
        self.create_text("P1", self.p1_robot_x+14, self.p1_robot_y+37)

        self.create_text("F2 = New Game", self.width/2 - 162, 11)
        self.create_text("Esc = Exit Game", self.width/2, 11)

        if self.p1_game_over and self.p2_game_over:
            if self.game_mode == 1 and self.show_high_score:
                    self.create_text("New High Score", self.width/2 - 141/2, self.height/2 - 28/2, (199,0,57))

            if self.game_mode == 2:
                if Game.p1_coins_collected > Game.p2_coins_collected:
                    self.create_text("Player 1 wins", self.width/2 - 116/2, self.height/2 - 28/2, (199,0,57))
                elif Game.p2_coins_collected > Game.p1_coins_collected:
                    self.create_text("Player 2 wins", self.width/2 - 116/2, self.height/2 - 28/2, (199,0,57))
                else:
                    self.create_text("Draw", self.width/2 - 47/2, self.height/2 - 28/2, (199,0,57))

        self.clock.tick(200)
        pygame.display.flip()

    def create_text(self, text: str, x: float, y: float, color: tuple = (3,0,46)):
        text = self.game_font.render(text, True, color)
        self.window.blit(text, (x, y))

if __name__ == "__main__":
    Game()