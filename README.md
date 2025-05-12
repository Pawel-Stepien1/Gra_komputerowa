# Gra komputerowa

## Opis
Napisałem grę arkadową w Python (biblioteka pygame), która bazuje na "Breakout" wydanej przez firmę Atari na automaty do gier.  
Rozgrywka rozpoczyna się z sześcioma rzędami „cegiełek” w trzech różnych kolorach – od dołu: czerwone, zielone i niebieskie. Gracz kontrolujący paletkę poruszającą się poziomo po dole ekranu przy pomocy piłki musi zniszczyć jak najwięcej cegiełek, jeśli gracz nie zdoła utrzymać piłki na ekranie to traci on jedno życie. Startowa liczba żyć to 3. Celem gry jest zniszczenie wszystkich „cegiełek”. W zależności od koloru „cegiełki” posiada ona różny stopień wytrzymałości. Kolor czerwony - jedno uderzenie, żeby zniszczyć; kolor zielony - dwa uderzenia; kolor niebieski - trzy uderzenia. Wraz z kolejnymi uderzeniami, „cegiełki” zmieniają swój kolor, w zależności od wytrzymałości jaka im pozostała.  
W grze możemy włączyć i wyłączyć zarówno muzykę oraz dźwięki. Posiadamy także tabelę najlepszych wyników oraz guzik do ich wyzerowania. Znajdziemy także zakładkę z instrukcją gry oraz infomcje o autorze.

## Pliki
Gra.py - cały kod zawierjący i włączający grę.
button.py - plik, gdzie została zaimplementowana klasa guzika.
wyniki.txt - plik, zawierający najlepsze wyniki.
Wszystkie pliki z rozszerzeniem ".png" to grafiki, które są zawarte w grze.
Wszystkie pliki z rozszerzeniem ".ogg" to dźwięki, które są zawarte w grze.
