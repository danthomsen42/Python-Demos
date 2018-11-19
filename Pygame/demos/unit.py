import pygame

import graphics


class unit(object):
	def __init__(self, x, y):
			self.x = x
			self.y = y
			self.frame = 0.0
			
class George(unit):
	def __init__(self, x, y):
		super(George, self).__init__(x, y)
		self.spritesheet = graphics.load("spritesheet2.png")
		self.LorR = True
		self.key_states = pygame.event.get()
		self.keys = pygame.key.get_pressed()
		self.shoot = False
		self.velocity = [0, 0]
		#width 2020
		#height 4000
        #20 total high
        #10 max wide
		#self.charLeft = graphics.load("spriteCharLeft.png")
		self.mapping = {
			"shootRunLeft" : [(202 * i , 0, 202, 200) for i in range(1, 10)],
			"jumpShootLeft": [(202 * i, 200, 202, 200) for i in range(5, 10)],
			"runLeft": 		 [(202 * i, 400, 202, 200) for i in range(2, 10)],
			"shootLeft": 	 [(202 * i, 600, 202, 200) for i in range(6, 10)],
			"idleLeft": 	 [(202 * i, 800, 202, 200) for i in range(0, 10)],
			"jumpMeleeLeft": [(202 * i, 1000, 202, 200) for i in range(2, 10)],
			"meleeLeft": 	 [(202 * i, 1200, 202, 200) for i in range(2, 10)],
			"slideLeft": 	 [(202 * i, 1400, 202, 200) for i in range(10)],
			"jumpLeft": 	 [(202 * i, 1600, 202, 200) for i in range(10)],
			"dieLeft": 	  	 [(202 * i, 1800, 202, 200) for i in range(10)],
			"shootRunRight": [(202 * i, 2000, 202, 200) for i in range(9)],
			"jumpShootRight":[(202 * i, 2200, 202, 200) for i in range(5)],
			"runRight": 	 [(202 * i, 2400, 202, 200) for i in range(8)],
			"shootRight": 	 [(202 * i, 2600, 202, 200) for i in range(4)],
			"idleRight": 	 [(202 * i, 2800, 202, 200) for i in range(10)],
			"jumpMeleeRight":[(202 * i, 3000, 202, 200) for i in range(8)],
			"meleeRight": 	 [(202 * i, 3200, 202, 200) for i in range(8)],
			"slideRight": 	 [(202 * i, 3400, 202, 200) for i in range(10)],
			"jumpRight": 	 [(202 * i, 3600, 202, 200) for i in range(10)],
			"dieRight": 	 [(202 * i, 3800, 202, 200) for i in range(10)]

		}
		self.facing = "idleLeft"
		self.speed = 0.6
		
	def update(self):
		self.frame = (self.frame + self.speed) % len(self.mapping[self.facing])

	def render(self, surface):
		surface.blit(self.spritesheet,
		             (self.x, self.y, 202,200),
		             self.mapping[self.facing][int(self.frame)])
					 
	def handler(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				self.shoot = True
			else:
				self.shoot = False

			if event.key == pygame.K_UP:
				self.y -= 5
				if self.y < 0:
					self.y = 0
			elif event.key == pygame.K_DOWN:
				self.y += 5
				if self.y > (2019 - 202):
					self.y = 2019 - 202
			elif event.key == pygame.K_LEFT:
				if self.shoot:
					self.facing = "shootRunLeft"
				else:
					self.facing = "runLeft"
				self.LorR = True
				self.x -= 5
				if self.x < 0:
					self.x = 0

			elif event.key == pygame.K_RIGHT:
				if self.shoot:
					self.facing = "shootRunRight"
				else:
					self.facing = "runRight"
				self.LorR = False

				self.x += 5
				if self.x > (3999 - 200):
					self.x = 3999 - 200

		else:
			if self.LorR:
				self.facing = "idleLeft"
			else:
				self.facing = "idleRight"
				
					
