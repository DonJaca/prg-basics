import time

countdown = int(input("Enter the number of seconds to count down: "))
last_five = {5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}

while countdown > 0:
    print(last_five.get(countdown, countdown))
    countdown -= 1
    time.sleep(1)

print("Time's up!")
