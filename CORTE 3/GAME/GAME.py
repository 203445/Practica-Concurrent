import pygame, random ,threading
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0,255,0)
BLUE = (0, 0 ,255)


def scores(surface, text, size, x , y ):
	font = pygame.font.Font("assets/scoree.ttf", size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def barra_hp(surface, x , y , hp):
	largo = 120
	ancho = 25
	cal_barr = int((player.hp / 100) * largo)
	borde = pygame.Rect(x,y, largo, ancho)
	recta = pygame.Rect(x,y, cal_barr, ancho)
	pygame.draw.rect(surface, BLACK, borde,3)
	pygame.draw.rect(surface, "#DC143C" ,recta)
	live = pygame.image.load("assets/live.png").convert()
	live.set_colorkey(BLACK)
	surface.blit(pygame.transform.scale(live,(25,25)),(620,15))
	


def texto(surface, text, size, x, y):
	font = pygame.font.Font("assets/scoree.ttf", size)
	text_surface = font.render(text, True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)	

def pantalla_perder():
	fondo2 = pygame.image.load("assets/init.png").convert()
	ancho_deseado = 800
	alto_deseado = 600
	fondoxd = pygame.transform.scale(fondo2, (ancho_deseado, alto_deseado))
	screen.blit(fondoxd, [0, 0])

	texto(screen, "Space XS", 65, WIDTH // 2, HEIGHT // 4)
	texto(screen, "Presiona cualquier tecla", 20, WIDTH //2, HEIGHT * 3/4)
	pygame.display.flip()	

	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.mixer.music.load('assets/gameover.wav')
				pygame.mixer.music.set_volume(0.75)
				pygame.mixer.music.play(-1, 0.0)
				pygame.quit()
				
			if event.type == pygame.KEYUP:
				waiting = False			
	
class Player(pygame.sprite.Sprite, threading.Thread):
	def __init__(self):
		super().__init__()
		threading.Thread.__init__(self)
		self.image = pygame.image.load("assets/novita.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.radius = 27
		# pygame.draw.circle(self.image, GREEN,self.rect.center,self.radius )
		self.rect.center = (200,200)
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0
		self.hp = 100
		self.killed = False
		self.vida = 3
		
	def update(self):
		pos_mouse = pygame.mouse.get_pos()
		player.rect.x = pos_mouse[0]
		player.rect.y = 500
		

	def dispara(self):
		laser =  Laser(self.rect.centerx, self.rect.top)
		all_sprites.add(laser)
		laser_list.add(laser)

	# def terminar(self):
    # 	self.killed = True

class Asteroide(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/asteroide3.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.radius = 14
		# pygame.draw.circle(self.image, BLUE ,self.rect.center,self.radius)
		self.rect.center = (200,200)
		self.rect.x = random.randrange(WIDTH - self.rect.width) 
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-3, 3)
	
	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)

class Laser(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.image.load("assets/laser4.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.y = y
		self.speedy = -10


	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()


class Enemigos(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/ovni1.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.radius = 37
		# pygame.draw.circle(self.image, BLUE ,self.rect.center,self.radius)
		self.rect.center = (150,150)
		self.rect.y = random.randrange(HEIGHT - self.rect.height)
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.speedy = random.randrange(1, 2)
		self.speedx = random.randrange(1, 2)
		self.hp = 30
		
	def update(self): 
		self.rect.x += self.speedx
		self.rect.y += self.speedy

		# Limita el margen izquierdo
		if self.rect.left < 0:
			self.speedx  += 1

		# Limita el margen derecho
		if self.rect.right > WIDTH:
			self.speedx  -= 1

		# Limita el margen inferior
		if self.rect.bottom > HEIGHT:
			self.speedy  -= 1

		# Limita el margen superior
		if self.rect.top < 0:
			self.speedy  += 1

# INICIO
pygame.init()
pygame.mixer.init()
score = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space XS")
clock = pygame.time.Clock() 	 	

# Music
pygame.mixer.music.load('assets/fondo.wav')
pygame.mixer.music.set_volume(0.75)
pygame.mixer.music.play(-1, 0.0)	

asteroides_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
all_sprites4 = pygame.sprite.Group()
all_sprites3 = pygame.sprite.Group()

laser_list = pygame.sprite.Group()
enemige_list = pygame.sprite.Group()

background = pygame.image.load("assets/uni.jpg").convert()

# Game start
perder = True
nova = True
while nova:
	
	if perder:
		pantalla_perder()
		perder = False
		# for x in range(3):
		player = Player()
		# player2 = Player()
		# player3 = Player() crwando los otros hilos
		# player4 = Player()
		
		# player.start()
		# player2.start() iniciando los otros hilos
		# player3.start()
		# player4.start()

		all_sprites.add(player) 
		# all_sprites2.add(player2)
		# all_sprites3.add(player3)
		# all_sprites4.add(player4)

		score = 0 
		
	if not enemige_list or not asteroides_list:
		
		enemigo1 = Enemigos()
		enemige_list.add(enemigo1)	
		all_sprites.add(enemigo1)	

		# for i in range(2):
		astero = Asteroide()
		all_sprites.add(astero)
		asteroides_list.add(astero)
	
	# Actualiza
	all_sprites.update()
	asteroides_list.update()
	enemige_list.update()
	laser_list.update()
	# all_sprites2.update()  parte de la aplicación para el hilo
	# all_sprites3.update()
	# all_sprites4.update()

	# Velocidad de FDS
	clock.tick(60)
	# Eventos
	for event in pygame.event.get():
		# Verifica el cierre de ventana
		# print(event)
		if event.type == pygame.QUIT:
			running = False
	
		elif event.type == pygame.MOUSEBUTTONDOWN:
			player.dispara()	

	# COLOSIONES LASER
	disparoAsteroides = pygame.sprite.groupcollide(asteroides_list, laser_list, True, True)
	# COLOSIONES ENEMIGOS
	disparoEnemigos = pygame.sprite.groupcollide(enemige_list, laser_list, False, True)

	#COLOSIONES Asteroides
	disparo =  pygame.sprite.spritecollide(player, asteroides_list,True, pygame.sprite.collide_circle)
	# COLOSIONES ENEMIGOS
	disparo2 =  pygame.sprite.spritecollide(player, enemige_list, True,pygame.sprite.collide_circle)
	
	if disparo :
		# nova = False
		player.hp -=10
	if disparo2:
		# nova = False
		player.hp -=20

	
		# if score >=0:
		# 	score -=10
		# 	if score < 0 :
		# 		score = 0
		# nova = False
	
	if disparoAsteroides:	
		for d in disparoAsteroides:
			score += 5
			astero = Asteroide()
			all_sprites.add(astero)
			asteroides_list.add(astero)

	
	# if score == 10:
	if disparoEnemigos:
		score += 10
		# enemigo1 = Enemigos()
		# all_sprites.add(enemigo1)
		# enemige_list.add(enemigo1)
		enemigo1.hp -= 10

	if enemigo1.hp <= 0:
		enemigo1.kill()	
		# enemigo2 = Enemigos()
		# all_sprites.add(enemigo2)
		# enemige_list.add(enemigo2)
		# enemigo2.hp -= 10
	
	if score == 500 :
		print("nivel 2")
	
	
	# if player.hp <=0:
	# 	nova = False
	
	# if player.hp < 0 and player.vida == 3:
	# 	player.hp = 0 

	if player.hp < 0 and player.vida == 3:
		player.kill()
		player = Player()
		# # player2.start()
		# all_sprites2.add(player2)
		all_sprites.add(player)
		player.vida = 2

	if player.vida == 2:
		if player.hp < 0:
			player.kill()
			player = Player()
			# # player3.start()
			# all_sprites3.add(player3)
			all_sprites.add(player)
			player.vida = 1

	if player.vida == 1:
		if player.hp < 0:
			player.kill()
			player= Player()
			# all_sprites4.add(player4)
			all_sprites.add(player)
			player.vida = 0

	if player.vida == 0:
		if player.hp < 0:
			player.kill()
			player.hp = 0
			break
	# Color de Fondo
	screen.fill(BLACK)
	screen.blit(background, [0, 0])
	all_sprites.draw(screen)
	# all_sprites2.draw(screen)    inconclusooo
	# all_sprites3.draw(screen)
	# all_sprites4.draw(screen)
	# enemige_list.draw(screen)
	asteroides_list.draw(screen)
	laser_list.draw(screen)


	# Dibujos en la pantalla
	scores(screen, str(score).zfill(2), 25, WIDTH // 2, 20 )
	barra_hp(screen, 650,15, player.hp)
	pygame.display.flip()

pygame.quit()

# if __name__ == '__main__':
# 	player = Player()
# 	# player.start()
# 	all_sprites.add(player)
	