# Scorpio-zadanie-rekrutacyjne

## Etap 1
Program napisałem w pythonie przy wykorzystaniu biblioteki psutil. Nie zrobiłem jedynie odczytu temperatury każdego rdzenia, gdyż korzystajac z virtual machine nie jestem w stanie ich odczytać.


## Etap 2
Aby program wykonywał się na starcie systemu wykorzystałem crontaba.
```
sudo cp -i /home/pjury/Desktop/Scorpio-zadanie-rekrutacyjne/main.py /bin
sudo crontab -e
```
I dodałem taka linie
```
@reboot python /bin/main.py &
```
Nastepnie po każdym ponownym włączeniu systemu, plik system_data_readings.txt jest aktualizowany co około 5s.


## Etap 3
Wykorztując fetch API pobieram dane z pliku, a następnie z odrobiną JS'a uzupełniam tabele danymi. Aby móc korzystać z fetcha potrzebowałem serwera. Wykorzystałem do tego  prosty serwer pythonowy ```python3 -m http.server 8000 --bind 127.0.0.1```. Wygląda to następująco:
![image](https://user-images.githubusercontent.com/77162184/193583898-cc78492c-3dc6-4b85-87d5-756911d7e9fc.png)
