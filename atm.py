import decimal
import logging
import argparse


logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.INFO, filename="atm_log.log", encoding="utf-8")

money_in_atm = 0
count_operation = 0


def tax():
    global money_in_atm
    if money_in_atm > 5_000_000:
        money_in_atm *= decimal.Decimal(0.9)
        print("Налог 10% при сумме более 5_000_000 у.е.")
        logging.info("Налог 10% при сумме более 5_000_000 у.е.")


def is_multiple_of_50(value):
    return value % 50 == 0


def count_increase():
    global count_operation
    count_operation += 1
    if count_operation % 3 == 0:  
        global money_in_atm
        money_in_atm *= decimal.Decimal(1.03)
        print("Начисление 3%")
        logging.info("Начисление 3%")


def put_money(value):
    tax()
    global money_in_atm
    if is_multiple_of_50(value):
        money_in_atm += value
        count_increase()
        logging.info(f"Счет пополнен на {value} у.е.")
        return f"Счет пополнен на {value} у.е."
    else:
        logging.info("Можно пополнять на сумму, кратную 50")
        return "Можно пополнять на сумму, кратную 50"


def take_money(value):
    tax()
    TAXFORTAKEMONEY = 1.5
    global money_in_atm
    if is_multiple_of_50(value):
        if money_in_atm >= value:  
            comisia = decimal.Decimal(value * 0.015)
            if comisia < 30:
                comisia = 30
            elif comisia > 600: 
                comisia = 600
            money_in_atm -= decimal.Decimal(value + comisia)
            count_increase()
            logging.info(
                f"Вы сняли {value} у.е. Налог на снятие {comisia:.2f}")
            return f"Вы сняли {value} у.е. Налог на снятие {comisia:.2f}"
        else:
            logging.info("Неудачная попытка снятия средств")
            return "На Вашем счету недостаточно средств"
    logging.info("Неудачная попытка снятия средств")
    return "Можно снять сумму, кратную 50"


def task():
    while True:
        logging.info(f"На Вашем счету {money_in_atm:.2f} у.е.")
        print(f"На Вашем счету {money_in_atm:.2f} у.е.")
        print("Введите от 1 до 3")
        print("1 - Пополнить счет")
        print("2 - Снять со счета")
        print("3 - Выйти")
        choice = input()

        if choice == "1":
            amount = int(
                input("Введите сумму, на которую вы хотите пополнить счет: "))
            print(put_money(amount))
        elif choice == "2":
            amount = int(input("Введите сумму снятия: "))
            print(take_money(amount))
        elif choice == "3":
            break
        else:
            print("Введено неверное значение")


def main():
    task()


def out_parser():
    parser = argparse.ArgumentParser(
        description="команда для запуска программы 'python atm.py'")

    main()


if __name__ == "__main__":
    out = out_parser()
