# Scorpio zadanie-rekrutacyjne

## Etap 1
Program napisałem w pythonie przy wykorzystaniu biblioteki psutil. Nie zrobiłem jedynie odczytu temperatury każdego rdzenia, gdyż korzystajac z virtual machine nie jestem wstanie ich odczytać.


## Etap 2
Aby program wykonywał się na starcie systemu wykorzystałem crontaba.
```
sudo cp -i /home/pjury/Desktop/scorpio/main.py /bin
sudo crontab -e
@reboot python /bin/main.py &
```
Nastepnie po każdym ponownym włączeniu systemu, plik system_data_readings.txt jest aktualizowany.


## Etap 3
Wykorztując fetch API pobieram dane z pliku, a następnie z odrobiną JS'a wkładam dane do tabelki. Aby móc korzystać z fetcha potrzebowałem serwera wykorzystałem do tego  prosty serwer pythonowy ```python3 -m http.server 8000 --bind 127.0.0.1```. Wygląda to następująco:
![image](https://user-images.githubusercontent.com/77162184/192109430-8b7f01bc-a299-445b-8a14-ac634776adc1.png)
