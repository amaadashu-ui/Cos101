# STUDENT 1 - PHYSICS CALCULATOR

def speed():
    distance = float(input("Enter distance: "))
    time = float(input("Enter time: "))
    if time > 0:
        print("Speed =", distance / time, "m/s")
    else:
        print("Time must be greater than zero")

def force():
    mass = float(input("Enter mass: "))
    acceleration = float(input("Enter acceleration: "))
    print("Force =", mass * acceleration, "Newtons")

def work():
    force_value = float(input("Enter force: "))
    distance = float(input("Enter distance: "))
    print("Work done =", force_value * distance, "Joules")

def power():
    work_done = float(input("Enter work done: "))
    time = float(input("Enter time: "))
    if time > 0:
        print("Power =", work_done / time, "Watts")
    else:
        print("Time must be greater than zero")

def acceleration():
    u = float(input("Enter initial velocity: "))
    v = float(input("Enter final velocity: "))
    t = float(input("Enter time: "))
    if t > 0:
        print("Acceleration =", (v-u)/t, "m/s2")
    else:
        print("Time must be greater than zero")

while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Speed")
    print("2. Force")
    print("3. Work Done")
    print("4. Power")
    print("5. Acceleration")

    choice = input("Select an operation (1-5): ")

    if choice == "1":
        speed()
    elif choice == "2":
        force()
    elif choice == "3":
        work()
    elif choice == "4":
        power()
    elif choice == "5":
        acceleration()
    else:
        print("Invalid choice")

    again = input("\nDo you want to perform another operation? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using the calculator!")
        break
