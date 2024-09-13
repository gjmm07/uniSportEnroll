# uniSportEnroll


Tiny script to enroll into courses at [Hochschulsport Köln](https://www.hochschulsport-koeln.de/) 

Tested for [schwimmen](https://anmeldung.hochschulsport-koeln.de/anmeldung.php?course=64&offer=44)

Please install python with [selenium](https://pypi.org/project/selenium/) and run 

```sh
python main.py -f firstname -l lastname -m mat-no -e email -u 1 -s url -p phone-no -d date
```

### Special flags: 
- -u: the university you study at:
  - 1: Universltät zu Köln
  - 2: Technische Hochschule Köln 
- -s: the exact course you want to apply for, e.g. [schwimmen](https://anmeldung.hochschulsport-koeln.de/anmeldung.php?course=64&offer=44)
- -d: exact time when the application phase starts in the form of dd.mm.YYY_HH:MM:SS

