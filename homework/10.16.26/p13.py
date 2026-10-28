truck_speed = float(input("Введите скорость грузовика в км/ч: "))
car_delay = float(input("Через сколько часов после грузовика выехал легковой автомобиль: ")) 
car_speed = float(input("Введите скорость легкового автомобиля в км/ч: "))
car_time = float(input("Время движения легкового автомобиля в часах: "))

def calc_vehicle_distance(speed:float, travel_time:float, delay:float):
    return speed * (delay + travel_time)

def create():
    truck_distance = calc_vehicle_distance(truck_speed, car_time, car_delay)
    car_distance = calc_vehicle_distance(car_speed, car_time, 0)

    if car_distance < truck_distance:
        print("Легковой автомобиль не догонит грузовой")
    elif car_distance == truck_distance:
        print("Легковой автомобиль догонит грузовой ровно через t1 часов")
    else:
        print("Легковой автомобиль догонит грузовой раньше, чем через t1 часов")

create()