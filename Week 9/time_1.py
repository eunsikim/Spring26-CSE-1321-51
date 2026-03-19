import time

def main():
    # time() returns a number of seconds
    # since Jan 1st 1970 00:00:00 UTC (-5 hrs ET)
    print(time.time())

    print(time.ctime(1773766833.9560313))

    

if __name__ == "__main__":
    main()