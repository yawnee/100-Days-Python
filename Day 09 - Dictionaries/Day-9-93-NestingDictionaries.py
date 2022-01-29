#Can put a list and a dictionary inside a dictionary

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",

}

#Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

#Nested lists is not as useful as nesting in a dictionary

#Nesting dictionary in a dictionary
# cities_visited = {
#     "Paris": 1,
#     "Lille": 2
# }
# travel_log1 = {
#     "France": cities_visited,
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }
travel_log1 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}
print(travel_log1['France'])
print("\n")
#Nesting dictionaries into a list
travel_log2 = [
    {
    "Country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    {
    "Country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
    }
]

print(travel_log2[0])

