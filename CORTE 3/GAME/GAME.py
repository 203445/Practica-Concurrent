import time
import pygame, random ,threading
# from game_Player import
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

def barra_vida(surface, x , y , vida):
	largo = 100
	ancho = 25
	cal_barr = int((vida / 150 ) * largo)
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

def pantalla_ganar():
	fondo2 = pygame.image.load("assets/init.png").convert()
	ancho_deseado = 800
	alto_deseado = 600
	fondoxd = pygame.transform.scale(fondo2, (ancho_deseado, alto_deseado))
	screen.blit(fondoxd, [0, 0])

	texto(screen, "You Win!!", 65, WIDTH // 2, HEIGHT // 4)
	texto(screen, "Presiona alguna tecla para jugar de nuevo", 20, WIDTH //2, HEIGHT * 3/4)
	pygame.display.flip()	

	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				
			if event.type == pygame.KEYUP:
				waiting = False	
				return False	

def pantalla_perder():
	fondo2 = pygame.image.load("assets/init.png").convert()
	ancho_deseado = 800
	alto_deseado = 600
	fondoxd = pygame.transform.scale(fondo2, (ancho_deseado, alto_deseado))
	screen.blit(fondoxd, [0, 0])

	texto(screen, "Space Space", 65, WIDTH // 2, HEIGHT // 4)
	texto(screen, "Presiona cualquier tecla para iniciar", 20, WIDTH //2, HEIGHT * 3/4)
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

def pantalla_perder2():
	fondo2 = pygame.image.load("assets/init.png").convert()
	ancho_deseado = 800
	alto_deseado = 600
	fondoxd = pygame.transform.scale(fondo2, (ancho_deseado, alto_deseado))
	screen.blit(fondoxd, [0, 0])

	texto(screen, "Game Over", 65, WIDTH // 2, HEIGHT // 4)
	texto(screen, "Presiona cualquier tecla si quieres jugar de nuevo", 20, WIDTH //2, HEIGHT * 3/4)
	pygame.display.flip()	

	waiting = True
	
	pygame.mixer.music.load('assets/gameover.wav')
	pygame.mixer.music.set_volume(0.75)
	pygame.mixer.music.play(-1, 0.0)
	time.sleep(2)
	pygame.mixer.music.stop()
	time.sleep(1)
	pygame.mixer.music.load('assets/fondo.wav')
	pygame.mixer.music.set_volume(0.75)
	pygame.mixer.music.play(-1, 0.0)

		

	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				
			if event.type == pygame.KEYUP:
				waiting = False	
				return False		
	
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
		self.killed = False
		self.vida = 150 #Tiene 3 vidas el jugador pero se dividen los 150 en tres, que son 50 cada vida.

	def update(self):
		pos_mouse = pygame.mouse.get_pos()
		player.rect.x = pos_mouse[0]
		player.rect.y = 500
		
	def dispara(self):
		laser =  Laser(self.rect.centerx, self.rect.top)
		all_sprites.add(laser)
		laser_list.add(laser)

	def kill(self):
		self.killed = True

	def run(self):
		self.update()

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

class Jefe(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/jefe1.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.radius = 37
		# pygame.draw.circle(self.image, BLUE ,self.rect.center,self.radius)
		self.rect.center = (150,150)
		self.rect.y = random.randrange(HEIGHT - self.rect.height)
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.speedy = random.randrange(1, 2)
		self.speedx = random.randrange(1, 2)
		self.hp =1000

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
			self.speedy  -=1

		# Limita el margen superior
		if self.rect.top < 0:
			self.speedy  += 1	
	
# INICIO
pygame.init()
pygame.mixer.init()
score = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Space")
clock = pygame.time.Clock() 	 	

# Music
pygame.mixer.music.load('assets/fondo.wav')
pygame.mixer.music.set_volume(0.75)
pygame.mixer.music.play(-1, 0.0)	

asteroides_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
laser_list = pygame.sprite.Group()
enemige_list = pygame.sprite.Group()
jefe_list = pygame.sprite.Group()

background = pygame.image.load("assets/uni.jpg").convert()


player = Player()
jefesito = Jefe ()
def main():
	# Game start
	perder = True
	perder2 = False
	start = True
	termina = False

	
	while start:
		
		if not enemige_list or not asteroides_list:	
			
			enemigo1 = Enemigos()
			enemige_list.add(enemigo1)	
			all_sprites.add(enemigo1)	

			astero = Asteroide()
			all_sprites.add(astero)
			asteroides_list.add(astero)

		if termina:
			pantalla_ganar()
			termina = False
			perder = True
			perder2 = False
			jefesito.hp = 1000
			score = 0

		if perder2:
			perder2 = pantalla_perder2()
			perder = False

			if not player.is_alive():
				player.run()
				all_sprites.add(player) 
			player.vida = 150
			score = 0 

		if perder:
			pantalla_perder()
			perder = False
			player.run()
			player.vida = 150
			all_sprites.add(player) 

			score = 0 
			
		
		# Actualiza
		all_sprites.update()
		asteroides_list.update()
		enemige_list.update()
		laser_list.update()
		jefe_list.update()

		# Velocidad de FDS
		clock.tick(60)
		# Eventos
		for event in pygame.event.get():
			# Verifica el cierre de ventana
			# print(event)
			if event.type == pygame.QUIT:
				start = False

			elif event.type == pygame.MOUSEBUTTONDOWN:
				player.dispara()	

		# COLOSIONES LASER
		disparoAsteroides = pygame.sprite.groupcollide(asteroides_list, laser_list, True, True)
		# COLOSIONES ENEMIGOS
		disparoEnemigos = pygame.sprite.groupcollide(enemige_list, laser_list, False, True)
		# COLOSIONES JEFE
		disparoJefe = pygame.sprite.groupcollide(jefe_list, laser_list, False, True)

		#COLOSIONES Asteroides
		choque =  pygame.sprite.spritecollide(player, asteroides_list,True, pygame.sprite.collide_circle)
		# COLOSIONES ENEMIGOS
		choque2 =  pygame.sprite.spritecollide(player, enemige_list, True,pygame.sprite.collide_circle)
		#COLISIONES JEFE
		choque3 =  pygame.sprite.spritecollide(player, jefe_list, True,pygame.sprite.collide_circle)

		if choque :
			player.vida -= 50

		if choque2:
			player.vida -= 100

		if choque3:
			player.vida -=300
			perder2 = True		

		if disparoAsteroides:	
			for d in disparoAsteroides:
				score += 5
				astero = Asteroide()
				all_sprites.add(astero)
				asteroides_list.add(astero)

		if disparoEnemigos:
			score += 10
			enemigo1.hp -= 10

		if enemigo1.hp <= 0:
			enemigo1.kill()		

		if disparoJefe:
			score += 50
			jefesito.hp -= 50

		if score > 100 :
			# all_sprites.add(jefesito)
			jefe_list.add(jefesito)

		if jefesito.hp <= 0:
			jefesito.kill()	
			termina = True
			score = 0

		if player.vida <=0:
			player.kill()
			player.vida = 0
			perder2 = True
		

		# Color de Fondo
		screen.fill(BLACK)
		screen.blit(background, [0, 0])
		all_sprites.draw(screen)
		asteroides_list.draw(screen)
		laser_list.draw(screen)
		jefe_list.draw(screen)

		# Dibujos en la pantalla
		scores(screen, str(score).zfill(2), 25, WIDTH // 2, 20 )
		barra_vida(screen, 650,15, player.vida)
		pygame.display.flip()

	pygame.quit()

if __name__ == '__main__':
	main()
	