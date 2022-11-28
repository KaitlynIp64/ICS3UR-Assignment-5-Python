#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Nov 2022
# This program prints a word and the number of times the user chooses to enter


def main():
    user_word_input = 0
    user_num_input = 0

    while True:
        user_word_input = input("Input a word: ")
        user_num_input = input(
            "Input the number of times you want the word to repeat: "
        )

        try:
            user_num_input = int(user_num_input)
            if user_num_input >= 0:
                print(user_word_input * user_num_input)
                break
            elif user_num_input <= 0:
                print("That is not a proper number.")
        except ValueError:
            print("That is not a valid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
