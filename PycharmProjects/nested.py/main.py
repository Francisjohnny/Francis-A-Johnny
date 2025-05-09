capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in Dictionary

# travel_log = {
#  "Nigeria": ["Bayelsa", "Rivers", "Delta"],
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Stuttgart", "Berlin"],
#}

# print Rivers
#print(travel_log["Nigeria"][1])

nested_list = ["A", "B", ["C", "D"]]

# print(nested_list[2][1])

travel_log = {
    "Nigeria": {
        "num_times_visited": 12,
        "cities_visited": ["Bayelsa", "Rivers", "Delta", "Edo", "Lagos"],
    },
    "France": {
        "num_times_visited": 7,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["Nigeria"]["cities_visited"][3])