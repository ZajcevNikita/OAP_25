minutes_limit = float(input("Введите норму минут в месяц: "))
base_fee = float(input("Введите плату за норму: "))
price_per_minute = float(input("Введите стоимость минуты сверх нормы: "))
talk_minutes = float(input("Введите время разговоров за месяц в минутах: "))

def calculate_price(minutes_limit:float, base_fee:float, price_per_minute:float, talk_minutes:float):
    if talk_minutes <= minutes_limit:
        return base_fee
    else:
        return base_fee + (talk_minutes - minutes_limit) * price_per_minute

def create():
    total_payment = calculate_price(minutes_limit, base_fee, price_per_minute, talk_minutes)

    print(f"Плата за пользование телефоном: {total_payment} руб")

create()