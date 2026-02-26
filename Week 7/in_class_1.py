def avg_acc(velocity, time):
    return velocity / time

def main():
    velocity = float(input("Velocity: "))
    time = float(input("Time: "))

    print(f"Avg. Acceleration: {avg_acc(velocity, time)}")

if __name__ == "__main__":
    main()