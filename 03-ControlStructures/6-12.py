car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140
if not speed_limit_min <= car_speed <= speed_limit_max:
    print('Warning: invalid car speed!!')
