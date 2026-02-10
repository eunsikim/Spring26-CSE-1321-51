def main():
    cal = int( input("How many calories per day: ") )
    year = int( input("How many years: ") )

    # Assume the user enters a cal value >= 2500
    excess_per_day = cal - 2500

    lbs_per_day = excess_per_day / 3500

    total_lbs = lbs_per_day * 365 * year

    print(f"You would have gained {total_lbs} lbs.")

if __name__ == "__main__":
    main()