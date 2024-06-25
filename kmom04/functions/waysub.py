# pylint: disable=missing-docstring
# import sandwich

from math import floor as lower, ceil
import sandwich as s

ingredients = ["ost", "bacon", "sallad", "majonnäs"]

# ingredients_string = sandwich.create_sandwich_string(ingredients, "En BLT innehåller")
ingredients_string = s.create_sandwich_string(ingredients, "Blt is made of: ")
print(ingredients_string)


print(lower(3.14))
# skriver ut: 3
print(ceil(3.14))
# skriver ut: 4
print(pow(5, 2))
