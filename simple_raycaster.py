import math, pygame

class Game():
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 600,600
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 1
        self.fps = 0
        self.player_x, self.player_y = 1.5 , 1.5
        self.player_angle = 0
        self.render_quality = 30
        pygame.display.set_caption("Raycaster")

        self.MAP = [
        "111111111111",
        "100000000001",
        "100000000001",
        "100011110001",
        "100011110001",
        "100000000001",
        "100000000001",
        "111111111111"
        ]

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                self.player_angle += 0.05 * self.dt
            if keys[pygame.K_LEFT]:
                self.player_angle -= 0.05 * self.dt
            if keys[pygame.K_UP]:
                self.player_x += 0.1 * math.cos(self.player_angle) * self.dt
                self.player_y += 0.1 * math.sin(self.player_angle) * self.dt
            if keys[pygame.K_DOWN]:
                self.player_x -= 0.1 * math.cos(self.player_angle) * self.dt
                self.player_y -= 0.1 * math.sin(self.player_angle) * self.dt


            self.screen.fill("black")


            #raycasting
            for x in range(self.WIDTH):
                ray_angle = self.player_angle - math.pi / 4 + (x / self.WIDTH) * math.pi / 2


                ray_x, ray_y = self.player_x, self.player_y

                step_x = math.cos(ray_angle) / self.render_quality
                step_y = math.sin(ray_angle) / self.render_quality

                hit_wall = False
                while not hit_wall:
                    ray_x += step_x
                    ray_y += step_y

                    map_x, map_y = int(ray_x),int(ray_y)

                    if self.MAP[map_x][map_y] == '1':
                        hit_wall = True
                
                distance = math.sqrt((ray_x-self.player_x)**2+(ray_y-self.player_y)**2)
                correction = math.cos(self.player_angle - ray_angle)

                wall_height = self.HEIGHT / (distance * correction)

                wall_color = int((20 - distance) / 20 * 255)

                pygame.draw.line(self.screen,(wall_color,wall_color,wall_color),(x, self.HEIGHT/2 - wall_height/2),(x, self.HEIGHT/2 + wall_height/2),1)


            pygame.display.flip()

            self.dt = self.clock.tick(self.fps) / 30

                




if __name__ == '__main__':
    Game().run()


        