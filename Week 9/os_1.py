import os
import time

def main():
    print(os.getcwd())

    print(os.listdir())

    print(os.listdir("C:/1321"))

    os.mkdir("remove me")

    time.sleep(10)

    os.remove("C:/Users/kimen/OneDrive - Kennesaw State University/Documents/2026/Spring/CSE 1321/github/Spring26-CSE-1321-51/remove me")

if __name__ == "__main__":
    main()