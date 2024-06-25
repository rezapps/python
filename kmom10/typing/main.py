"""
Main function for Type Test
"""
import menu
import func


def main():
    """ choice handling """
    choice = menu.menu()
    if choice == "1":
        func.easy()

    if choice == "2":
        func.medium()

    if choice == "3":
        func.hard()

    if choice == "4":
        func.show_top_scores()

    elif choice == "q":
        func.quit_test()
        exit()

    else:
        func.not_valid()


if __name__ == "__main__":
    while (True):
        main()
