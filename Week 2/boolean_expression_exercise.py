def main():
    # Evaluate each boolean expression (True or False)
    print(f"1. {3 > 4}")
    print(f"2. {3 > 4 and 10 == 10}")
    print(f"3. {3 < 4 and 10 == 10}")
    print(f"4. {3 > 4 or 10 >= 10}")
    print(f"5. {3 > 4 or 10 > 10 and 3 <= 3}")
    print(f"6. {3 > 4 or not 10 > 10 and 3 <= 3}")
    print(f"7. {(3 > 4 or not 10 > 10) and 3 <= 3}")

if __name__ == "__main__":
    main()