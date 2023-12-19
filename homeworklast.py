# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

import sys
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")


logging.info("New start")

logging.info(sys.argv)
if len(sys.argv) == 2:
    if (float(sys.argv[1]).is_integer()):
        N = int(sys.argv[1])
        if not (N < 0 or N > 100000):
            simple = True
            if N > 1:
                for i in range(2, N-1):
                    if N % i == 0:
                        simple = False
                    break
                if simple:
                    print(N, " - простое число ", end="")
                    logging.info("{N} - simple - {simple} ")
                else:
                    print(N, " - составное число ", end="")
                    logging.info("{N} - simple - {simple} ")
            else:
                print(
                    "Числа 0 и 1 не являются ни простыми, ни составными - это особый случай", end="")
                logging.info("{N} - special case")
        else:
            logging.error("Argument out of range")
            print("Введите целое число от 0 до 100 000", end="")
    else:
        logging.error("Wrong argument type")
        print("Введите целое число", end="")
else:
    logging.error("Wrong cmd argument count")
    print("Введите в командную строку имя скрипта и через пробел одно целое число от 0 до 100 000", end="")
logging.info("Over")
