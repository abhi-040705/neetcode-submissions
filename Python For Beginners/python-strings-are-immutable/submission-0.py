def remove_fourth_character(word: str) -> str:

    char3 = word[0:3]
    char5 = word[4:]
    return char3+char5


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
