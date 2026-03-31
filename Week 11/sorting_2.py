# Bubble Sort
# We push the largest (lowest) values at the end of the list
def main():
    cards = [5, 4, 3, 6, 2]

    print(cards)
    for i in range(len(cards)):
        for j in range(len(cards) - i - 1):
            current_indx = j
            next_indx = j + 1

            if cards[current_indx] > cards[next_indx]:
                cards[current_indx], cards[next_indx] = (cards[next_indx], cards[current_indx])
    print(cards)

if __name__ == "__main__":
    main()