import pygame
import sys
from pygame.locals import *
#inicjacja modułu pygame
pygame.init()
#szerokość i wysokość okna
oknogry_szer = 800
oknogry_wys = 800
#kolor okna gry, składowe - RGB
LT_BLUE = (207 ,217 ,227)

#inicjacja pola gry
oknogry = pygame.display.set_mode((oknogry_szer,oknogry_wys), 0,32)

#tytół okna gry
pygame.display.set_caption('SNEK')


#SNEK rysowanie bohatera
SNEK_szer = 30
SNEK_wys = 30
ORANGE = (255, 85, 0)#kolor postaci
SNEK_poz = (350 ,350)#początkowa pozycja SNEKA
SNEK = pygame.Surface([SNEK_szer, SNEK_wys])
SNEK.fill(ORANGE)


#ustawienia prostokąta zawierającego sneka w początkowej pozycji
SNEK_prost = SNEK.get_rect()
SNEK_prost.x = SNEK_poz[0]
SNEK_prost.y = SNEK_poz[1]
oknogry.blit(SNEK, SNEK_prost)


#pętla główna programu
while True:
    #obsługa zdarzeń generowanych przez gracza
    for event in pygame.event.get():
        #zamknięcie okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #przechwyć ruch myszy
        if event.type == MOUSEMOTION:
            myszaX, myszaY = event.pos #współrzędne x,y kursora myszy


            #oblicz przesunięcie SNEKA
            przesuniecie = myszaX - (SNEK_szer / 3)
            przesuniecie = myszaY - (SNEK_wys / 2)
            #jeżeli wykracza poza ekran w prawo
            if przesuniecie > oknogry_szer - SNEK_szer:
                przesuniecie = oknogry_szer - SNEK_szer

                #jeżeli w lewo
            if przesuniecie < 0:
                przesuniecie = 0

            #zaktualizuj położenie SNEKA w poziomie
            SNEK_prost.x = przesuniecie

    #rysowanie obiektów
    oknogry.fill(LT_BLUE) #kolor okna gry

    #narysuj w oknie gry SNEKA
    oknogry.blit(SNEK, SNEK_prost)

    #zaktualizuj okno i wyświetl
    pygame.display.update()
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
