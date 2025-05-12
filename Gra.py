#Importuję moduły.
import pygame
from pygame.locals import *
import button

pygame.init()

####################
#Dźwięk
####################
#inicjalizacja miksera do odtwarzania dźwięków.
pygame.mixer.init()

pygame.mixer.music.load("apoxode_electric.ogg")
pygame.mixer.music.play(loops=-1)

# dźwięki towarzyszące zdarzeniom.

collision_sound = pygame.mixer.Sound("collision.ogg")

#Ustalam parametry czy ma lecieć muzyka dźwięki. Jeśli równa się 1, to muzyka i dźwięki są odtwarzane.
czy_leci_muzyka = 1
czy_leci_dzwiek = 1


####################
#Tworzę okno gry
####################
#ustalam szerokość i wysokość okna, w którym zostanie wyświetlona gra.
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

#Zmienne czy gra jest zapauzowana i w którym menu się znajdujemy.
game_paused = True
menu_state = "main"

#Pozostałe zmienne.
#Liczba kolumn i wierszy.
cols = 6
rows = 6
#Ustalam zegar.
clock = pygame.time.Clock()
fps = 60
#Zmienne dotyczące czy piłka jest w grze i stan gry.
live_ball = False
game_over = 0

#Ustalam fony, którymi będę pisał.
font_maly = pygame.font.SysFont("arialblack", 15)
font = pygame.font.SysFont("arialblack", 20)
font_duzy = pygame.font.SysFont("arialblack", 40)

####################
#Ładuję obrazy guzików.
####################
#Ładuję obrazy guzików.
nowa_gra_img = pygame.image.load("button_nowa_gra.png").convert_alpha()
zasady_img = pygame.image.load('button_zasady.png').convert_alpha()
opcje_img = pygame.image.load("button_opcje.png").convert_alpha()
wyjscie_img = pygame.image.load("button_wyjscie.png").convert_alpha()
wyniki_img = pygame.image.load('button_wyniki.png').convert_alpha()
usun_wyniki_img = pygame.image.load('button_usun_wyniki.png').convert_alpha()
konfiguracja_img = pygame.image.load('button_konfiguracja.png').convert_alpha()
autor_img = pygame.image.load('button_autor.png').convert_alpha()
muzyka_img = pygame.image.load("button_muzyka.png").convert_alpha()
dzwiek_img = pygame.image.load("button_dzwiek.png").convert_alpha()
I_miejsce_img = pygame.image.load("button_I_miejsce.png").convert_alpha()
II_miejsce_img = pygame.image.load("button_II_miejsce.png").convert_alpha()
III_miejsce_img = pygame.image.load("button_III_miejsce.png").convert_alpha()

#Obrazy określające muzykę.
muzyka_tak_img = pygame.image.load("button_muzyka_tak.png").convert_alpha()
muzyka_nie_img = pygame.image.load("button_muzyka_nie.png").convert_alpha()

#Obrazy określające dźwięk.
dzwiek_tak_img = pygame.image.load("button_dzwiek_tak.png").convert_alpha()
dzwiek_nie_img = pygame.image.load("button_dzwiek_nie.png").convert_alpha()

####################
#Tworzę guziki.
####################
#Tworzę właściwe guziki.
nowa_gra_button = button.Button(140, 50, nowa_gra_img, 1)
zasady_button = button.Button(140, 160, zasady_img, 1)
opcje_button = button.Button(140, 270, opcje_img, 1)
autor_button = button.Button(140, 380, autor_img, 1)
wyjscie_button = button.Button(140, 490, wyjscie_img, 1)
wyniki_button = button.Button(140, 50, wyniki_img, 1)
usun_wyniki_button = button.Button(140, 380, usun_wyniki_img, 1)
konfiguracja_button = button.Button(140, 160, konfiguracja_img, 1)
muzyka_button = button.Button(140, 50, muzyka_img, 1)
dzwiek_button = button.Button(140, 270, dzwiek_img, 1)
I_miejsce_button = button.Button(140, 50, I_miejsce_img, 1)
II_miejsce_button = button.Button(140, 160, II_miejsce_img, 1)
III_miejsce_button = button.Button(140, 270, III_miejsce_img, 1)

#Tworzę guziki określające muzykę
muzyka_tak_button = button.Button(140, 160, muzyka_tak_img, 1)
muzyka_nie_button = button.Button(140, 160, muzyka_nie_img, 1)
#Tworzę guziki określające dźwięk.
dzwiek_tak_button = button.Button(140, 380, dzwiek_tak_img, 1)
dzwiek_nie_button = button.Button(140, 380, dzwiek_nie_img, 1)

####################
#Tworzę kolory.
####################
#Ustalam kolor tła.
bg = (234, 218, 184)
#Kolory klocków.
block_red = (242, 85, 96)
block_green = (86, 174, 87)
block_blue = (69, 177, 232)
#Kolor paletki.
paddle_col = (142, 135, 123)
paddle_outline = (100, 100, 100)
#Kolory tekstu.
text_col = (78, 81, 139)
text_col_2 = (255, 255, 255)

####################
#Tworzę funkcję do rysowania tekstu na ekranie.
####################

def draw_text(text, font, text_col, x, y):
    """Funkcja:
    Rysuje tekst na ekranie.
    Input:
    text(str) = tekst,który chcemy wypisać."
    font = czcionka i jej wielkość.
    text_col = kolor napisu.
    x = współrzędna x.
    y = współrzędna y.
    Output:
    Tekst wyrysowany na ekranie.
    """
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

####################
####################
#Tworzę klasy.
####################
####################


####################
#Tworzę klasę wall, która odpowiada za klocki.
####################
class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50

    def create_wall(self):
        self.blocks = []
        block_individual = []
        for row in range(rows):
            block_row = []
            for col in range(cols):
                #Ustalam współrzędne x i y.
                block_x = col * self.width
                block_y = row * self.height
                #Tworzę prostokąty(klocki).
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                #Ustalam wytrzymałość bloków w zależności od wiersza.
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1
                #Tworzę listę bloków.
                block_individual = [rect, strength]
                #Dodaję bloki do listy wiersza.
                block_row.append(block_individual)
            #Tworzę pełną listę bloków.
            self.blocks.append(block_row)
    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                #Ustalam kolor klocka w zależności od wytrzymałości.
                if block[1] == 3:
                    block_col = block_blue
                elif block[1] == 2:
                    block_col = block_green
                elif block[1] == 1:
                    block_col = block_red
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, bg, (block[0]), 2)

####################
#Tworzę klasę paddle, która odpowiada za paletkę.
####################
class paddle():
    def __init__(self):
        self.reset()

    def move(self):
        """
        Funkcja:
        Odpowiada za ruch palteki.
        """
        #kierunek ruchu.
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self):
        """
        Funkcja:
        Rysuje paletkę.
        """
        pygame.draw.rect(screen, paddle_col, self.rect)
        pygame.draw.rect(screen, paddle_outline, self.rect, 3)

    def reset(self):
        """
        Funkcja:
        Resetuje paletkę.
        """
        #Określenie parametrów paletki.
        self.height = 20
        self.width = int(screen_width / cols)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0

####################
#Tworzę klasę game_ball, która odpowiada za piłkę.
####################
class game_ball():
    def __init__(self, x, y):
        self.reset(x, y)
        
    def liczenie(self):
        """
        Funkcja:
        Odpowiada za liczenie punktów, w związku z niszczeniem klocków.
        """
        wall_destroyed = 1
        row_count = 0
        licznik_punktow=0
        for row in wall.blocks:
            item_count = 0
            for item in row:
                if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                    wall_destroyed = 0
                else:
                    #Dodawanie punktów.
                    licznik_punktow+=1
                item_count += 1
            row_count += 1
        #Zwracanie liczby punktów.
        return licznik_punktow  

    def move(self):
        """
        Funkcja:
        Odpowiada za ruch piłki.
        """
        #Próg kolizji.
        collision_thresh = 5

        wall_destroyed = 1
        row_count = 0
        licznik_punktow=0
        for row in wall.blocks:
            item_count = 0
            for item in row:
                #Sprawdzanie kolizji.
                if self.rect.colliderect(item[0]):
                    #Sprawdzanie kolizji z góry. 
                    if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                        self.speed_y *= -1
                    #Sprawdzanie kolizji od dołu.
                    if abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                        self.speed_y *= -1
                    #Sprawdzanie kolizji z lewej strony.
                    if abs(self.rect.right - item[0].left) < collision_thresh and self.speed_x > 0:
                        self.speed_x *= -1
                    #Sprawdzanie kolizji z prawej strony.
                    if abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                        self.speed_x *= -1
                    #Zmniejszanie wytrzymałości bloku.
                    if wall.blocks[row_count][item_count][1] > 1:
                        #Jeśli dźwięki są włączone, puść dźwięk kolizji z blokiem.
                        if czy_leci_dzwiek == 1:
                            collision_sound.play()
                        wall.blocks[row_count][item_count][1] -= 1
                    else:
                        wall.blocks[row_count][item_count][0] = (0, 0, 0, 0)
                        if czy_leci_dzwiek == 1:
                            collision_sound.play()
                #Sprawdzanie czy bloki istnieją.
                if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                    wall_destroyed = 0
                item_count += 1
            row_count += 1
        #Jeśli ściana jest zniszczona, zmienna game_over = 1 i tym samym wygrywamy grę.
        if wall_destroyed == 1:
            self.game_over = 1

        #Odbijanie się piłki od lewej i prawej strony ekranu.
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1

        #Sprawdzanie kolizji piłki z górną i dolną krawędzią ekranu.
        #Odbijanie się piłki od górnej krawędzi ekranu.
        if self.rect.top < 0:
            self.speed_y *= -1
        #Piłka wypada poza dolną krawędź, co jest równoznaczne z utratą życia, zmienna game_over = -1.
        if self.rect.bottom > screen_height:
            self.game_over = -1

        #Odbijanie się piłki od paletki.
        if self.rect.colliderect(player_paddle):
            if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
                #W zależnośći od kierunku poruszania paletki i piłki, piłka przyśpiesza, bądź zwalnia.
                self.speed_x += player_paddle.direction
                #Ustalenie, żeby piłka nie przekraczała maksymalnej prędkości.
                if self.speed_x > self.speed_max:
                    self.speed_x = self.speed_max
                #Ustalenie, żeby prędkość piłki nie spadła poniżej minimalnej prędkości.
                elif self.speed_x < 0 and self.speed_x < -self.speed_max:
                    self.speed_x = -self.speed_max
            else:
                self.speed_x *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        #Zwrócenie stanu gry.
        return self.game_over

    def draw(self):
        """
        Funkcja:
        Rysuje piłkę.
        """
        pygame.draw.circle(screen, paddle_col, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(screen, paddle_outline, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)

    def reset(self, x, y):
        """
        Funkcja:
        Resetuje piłkę.
        """
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0

#Tworzę obiekt klasy wall.
wall = wall()

#Tworzę obiekt klasy paddle.
player_paddle = paddle()

#Tworzę obiekt klasy game_ball.
ball = game_ball(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)

#Tworzenie pętli gry.
run = True
while run:
    #Kolor tła.
    screen.fill((52, 78, 91))

    #Tworzenie gry, kiedy jest pauza.
    if game_paused == True:
        liczba_zyc = 3
        wall.create_wall()
        ball.reset(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)
        player_paddle.reset()
        ####################
        #Tworzę menu.
        ####################
        ###Główne menu. ###################################
        if menu_state == "main":
            #Guzik Nowa gra.
            if nowa_gra_button.draw(screen):
                game_paused = False
            #Guzik zasady.
            if zasady_button.draw(screen):
                menu_state = "zasady"
            #Guzik opcje.
            if opcje_button.draw(screen):
                menu_state = "opcje"
            #Guzik informacje o autorze.
            if autor_button.draw(screen):
                menu_state = "informacje_o_autorze"
            #Guzik wyjścia z gry.
            if wyjscie_button.draw(screen):
                run = False
        ###Tworzę menu "opcje". ###################################
        if menu_state == "opcje":
            #Guzik konfiguracji.
            if konfiguracja_button.draw(screen):
                if czy_leci_muzyka == 1:
                    menu_state = "konfiguracja"
                else:
                    menu_state = "konfiguracja2"
            #Guzik wyniki.
            if wyniki_button.draw(screen):
                menu_state = "wyniki"
            #Guzik wyjścia do głównego menu.
            if wyjscie_button.draw(screen):
                menu_state = "main"
        ###Tworzę menu "zasady". ###################################
        if menu_state == "zasady":
            draw_text('Oto zasady gry', font_duzy, text_col_2, 130, screen_height // 2 - 280)
            draw_text('Sterowanie', font, text_col_2, 10, screen_height // 2 - 210)
            draw_text('Gracz ma możliwość poruszać paletką:', font_maly, text_col_2, 10, screen_height // 2 - 170)
            draw_text('- w lewo za pomocą lewej strzałki na klawiaturze', font_maly, text_col_2, 10, screen_height // 2 - 140)
            draw_text('- w prawo za pomocą prawej strzałki na klawiaturze', font_maly, text_col_2, 10, screen_height // 2 - 110)
            draw_text('Aby wyjść z bieżącej gry do menu - kliknij "spacja"', font_maly, text_col_2, 10, screen_height // 2 - 80)
            draw_text('Aby kontynuować grę - kliknij "lewy guzik myszki"', font_maly, text_col_2, 10, screen_height // 2 - 50)
            draw_text('Rozgrywka', font, text_col_2, 10, screen_height // 2 - 10)
            draw_text('Poruszaj paletką, aby odbić lecącą piłkę. Piłka po uderzeniu w klocek,', font_maly, text_col_2, 10, screen_height // 2 + 20)
            draw_text('zniszczy go, bądź uszkodzi. W zależności od koloru, klocki mają różną', font_maly, text_col_2, 10, screen_height // 2 + 50)
            draw_text('wytrzymałość. Celem gry jest zniszczenie wszystkich klocków. Jednak ', font_maly, text_col_2, 10, screen_height // 2 + 80)
            draw_text('musisz uważać, aby piłka nie uciekła w dół. Tracisz wtedy życie, a masz', font_maly, text_col_2, 10, screen_height // 2 + 110)
            draw_text('ich zaledwie 3. POWODZENIA!!! ', font_maly, text_col_2, 10, screen_height // 2 + 140)
            #Guzik wyjścia do głównego menu.
            if wyjscie_button.draw(screen):
                menu_state = "main"
        ###Tworzę 3 menu konfiguracji, żeby podczas zmieniania ustawień, użytkownik miał wrażenie przebywania w tym samym menu konfiguracji.
        ###Tworzę menu "konfiguracja". ###################################
        if menu_state == "konfiguracja":
            if czy_leci_dzwiek == 1:
                dzwiek_tak_button.draw(screen)
            if czy_leci_dzwiek == -1:
                dzwiek_nie_button.draw(screen)
            muzyka_tak_button.draw(screen)
            #Guzik do wł/wył muzyki.
            if muzyka_button.draw(screen):
                czy_leci_muzyka = -1*czy_leci_muzyka
                if czy_leci_muzyka == -1:
                    pygame.mixer.music.stop()
                    menu_state = "konfiguracja2"
                elif czy_leci_muzyka == 1:
                    pygame.mixer.music.play(loops=-1)
            #Guzik do wł/wył dźwięków.
            if dzwiek_button.draw(screen):
                czy_leci_dzwiek = -1*czy_leci_dzwiek
            #Guzik wyjścia do menu opcje.
            if wyjscie_button.draw(screen):
                menu_state = "opcje"               
        ###Tworzę menu "konfiguracja2". ###################################
        if menu_state == "konfiguracja2":
            if czy_leci_dzwiek == 1:
                dzwiek_tak_button.draw(screen)
            if czy_leci_dzwiek == -1:
                dzwiek_nie_button.draw(screen)
            muzyka_nie_button.draw(screen)
            #Guzik do wł/wył muzyki.
            if muzyka_button.draw(screen):
                czy_leci_muzyka = -1*czy_leci_muzyka
                if czy_leci_muzyka == -1:
                    pygame.mixer.music.stop()
                elif czy_leci_muzyka == 1:
                    pygame.mixer.music.play(loops=-1)
                    menu_state = "konfiguracja"
            #Guzik do wł/wył dźwięków.
            if dzwiek_button.draw(screen):
                czy_leci_dzwiek = -1*czy_leci_dzwiek
                menu_state == "konfiguracja3"
            #Guzik wyjścia do menu opcje.
            if wyjscie_button.draw(screen):
                menu_state = "opcje"
        ###Tworzę menu "konfiguracja3". ###################################
        if menu_state == "konfiguracja3":
            if czy_leci_muzyka ==1:
                menu_state ="konfiguracja"
            else:
                menu_state = "konfiguracja2"
        ###Tworzę menu "wyniki". ###################################      
        if menu_state == "wyniki":
            #Otwieram plik z wynikami i odczytuję 3 najlepsze wynik.
            plik = open("wyniki.txt", "r")
            treść_3 = plik.read()
            plik.close()
            lista_z_pliku_wyniki = treść_3.split(",")
            posortowana_lista_z_pliku_wyniki = sorted(lista_z_pliku_wyniki, key=lambda x: int(x), reverse=True)
            #Wyświetlanie wyników.
            I_miejsce_button.draw(screen)
            II_miejsce_button.draw(screen)
            III_miejsce_button.draw(screen)
            #Guzik do usuwania wyników.
            if usun_wyniki_button.draw(screen):
                plik_czyszczenie = open("wyniki.txt", "w")
                po_czyszczeniu = "0,0,0"
                plik_czyszczenie.write(po_czyszczeniu)
                plik_czyszczenie.close()
            #Guzik wyjścia do menu opcje.
            if wyjscie_button.draw(screen):
                menu_state = "opcje"
            draw_text('{}'.format(posortowana_lista_z_pliku_wyniki[0]), font_duzy, text_col, 220, 53)
            draw_text('{}'.format(posortowana_lista_z_pliku_wyniki[1]), font_duzy, text_col, 220, 163)
            draw_text('{}'.format(posortowana_lista_z_pliku_wyniki[2]), font_duzy, text_col, 220, 273)
        ###Tworzę menu "informacje_o_autorze". ###################################
        if menu_state == "informacje_o_autorze":
            draw_text('Jeśli masz okazję zagrać w tą grę,', font, text_col_2, 10, screen_height // 2 - 200)
            draw_text('to najprawdopodobniej znasz jej autora osobiście.', font, text_col_2, 10, screen_height // 2 - 150)
            draw_text('Autor           Paweł Stępień', font, text_col_2, 10, screen_height // 2 - 100)
            draw_text('nr albumu    276 038', font, text_col_2, 10, screen_height // 2 - 50)
            #Guzik wyjścia do  głównego menu.
            if wyjscie_button.draw(screen):
                menu_state = "main"
    else:
        ####################
        #Tworzę właściwą część gry..
        ####################
        clock.tick(fps)
        screen.fill(bg)

        #Rysuję klocki, paletkę i piłkę.
        wall.draw_wall()
        player_paddle.draw()
        ball.draw()
        
        ###
        ###Piszę co się dzieje kiedy piłka "żyje" - NIE wyleciała poza dolną krawędź.
        ###

        if live_ball:
            #Jeśli piłka "żyje" to poruszamy paletką.
            player_paddle.move()
            #Pobieramy stan gry z metody move z klasy game_ball, przypisując go do zmiennej game_over.
            game_over = ball.move()

            #Pobieramy liczbę z metody liczenie z klasy game_ball, przypisując ją do zmiennej liczenie.
            licznik = ball.liczenie()

            #Tworzymy na ekranie licznik punktów i żyć.
            draw_text('Liczba pkt:{}'.format(licznik), font, text_col, 10, 570)
            draw_text('Liczba żyć:{}'.format(liczba_zyc), font, text_col, 450, 570)
            #Ustalamy kiedy gra zostaje przerwana. Jeśli game_over = 1 to wygrywamy grę, jeśli game_over = -1 to przegrywamy(tracimy życie; jeśli nie mamy już żadnych, to koniec gry.
            if game_over == 1:
                live_ball = False
            if game_over == -1:
                liczba_zyc=liczba_zyc -1
                live_ball = False

        ###
        ###Piszę co się dzieje kiedy piłka "nie żyje" - wyleci poza dolną krawędź.
        ###

        #Wypisuje instrukcję, które zostaną wyświetlone na ekranie, w zależności od sytuacji w grze.
        if not live_ball:
            #Jeśli wygrałeś.
            if game_over == 1:
                draw_text('Wygrałeś!', font, text_col, 240, screen_height // 2 + 50)
                draw_text('Jesteś prawdziym mistrzem tej gry', font, text_col, 100, screen_height // 2 + 100)
                draw_text('Twój ostateczny bilans pkt to {} pkt'.format(licznik), font, text_col, 100, screen_height // 2 + 150)
            #Jeśli przegrałeś, ale masz 2 życia.
            elif game_over == -1 and liczba_zyc == 2:
                #licznik = ball.move()[1]
                draw_text('Przegrałeś!', font, text_col, 240, screen_height // 2 + 50)
                draw_text('Ale nie martw się, masz jeszcze 2 życia', font, text_col, 100, screen_height // 2 + 100)
                draw_text('i udało Ci się zdobyć {} pkt'.format(licznik), font, text_col, 165, screen_height // 2 + 150)
            #Jeśli przegrałeś, ale masz 1 życie.
            elif game_over == -1 and liczba_zyc == 1:
                draw_text('Przegrałeś!', font, text_col, 240, screen_height // 2 + 50)
                draw_text('Ale nie martw się, masz jeszcze 1 życie', font, text_col, 100, screen_height // 2 + 100)
                draw_text('i udało Ci się zdobyć {} pkt'.format(licznik), font, text_col, 165, screen_height // 2 + 150)
            #Jeśli przegrałeś i nie masz już żyć.
            elif game_over == -1 and liczba_zyc == 0:
                draw_text('PRZEGRAŁEŚ!', font, text_col, 208, screen_height // 2 + 50)
                draw_text('NIE MASZ JUŻ ŻYĆ!', font, text_col, 180, screen_height // 2 + 100)
                draw_text('Twój ostateczny bilans pkt to {} pkt'.format(licznik), font, text_col, 100, screen_height // 2 + 150)
                    
    #Pętla zdarzeń
    for event in pygame.event.get():
        #Ustalam, że po naciśnięciu klawisza "spacja" zostaniemy przeniesieni do menu.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        #Ustalam, że po naciśnięciu X w prawym górnym rogu gra zostanie zamknięta.
        if event.type == pygame.QUIT:
            run = False
        #Ustalam, że po naciśnięciu lewego klawisza na myszce i "martwej piłce" gra zostanie wznowiona.
        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            #Jeśli liczba żyć wynosi 3,2 lub 1 to zresetujemy piłkę i paletkę.
            if liczba_zyc<=3 and liczba_zyc>0:
                ball.reset(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)
                player_paddle.reset()
            #else:
            #Jeśli liczba żyć wynosi 0 lub wygraliśmy to zapisujemy uzyskany przez nas wynik.
            if liczba_zyc == 0 or game_over == 1:
                plik = open("wyniki.txt", "r")
                treść = plik.read()
                plik.close()

                treść_2 = treść + "," + str(licznik) 
                plik_2 = open("wyniki.txt", "w")
                plik_2.write(str(treść_2))
                plik_2.close()
                #Jeśli liczba żyć wynosi 0 lub wygraliśmy to zresetujemy piłkę,paletkę i klocki - tworzymy nową grę.    
                liczba_zyc=3
                ball.reset(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)
                player_paddle.reset()
                wall.create_wall()
            

    pygame.display.update()

#Zatrzymujemy muzykę.
pygame.mixer.music.stop()
pygame.mixer.quit()

pygame.quit()
