def main():
    # We want to know if a phone is fully charged, partially charged, or no power
    phone_battery_level = 50 # in percentage

    if phone_battery_level == 100:
        print("Phone is fully charged")
    elif phone_battery_level >= 50:
        print("Phone is partially charged")
    elif phone_battery_level >= 20:
        print("You should charge your phone")
    elif phone_battery_level >= 10:
        print("Battery critical")
    else:
        print("Phone has no charge")

if __name__ == "__main__":
    main()