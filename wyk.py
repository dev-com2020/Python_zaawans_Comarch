import modul
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


LICZBY = [

    (1963309, 2265973), (2030677, 3814172),
    (1551645, 2229620), (2039045, 2020802),
    (1823712, 1924928), (2293129, 1020491),
    (1281238, 2273782), (3823812, 4237281),
    (3812741, 4729139), (1292391, 2123811),
]


def main():
    start = time.time()
    pula = ProcessPoolExecutor(max_workers=2)
    wynik = list(pula.map(modul.gcd, LICZBY))
    end = time.time()
    roznica = end - start
    print(f"Obliczenia zabrały: {roznica:.2f} sek")


if __name__ == '__main__':
    main()
