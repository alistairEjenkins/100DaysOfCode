
def add_new_country(country, visits, cities):

    travel_log2.append({'country': country, 'cities_visited': cities, 'total_visits': int(visits) })

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

travel_log["France"] = {'cities_visited' : ["Paris", "Lille", "Dijon"]}

print(travel_log)

travel_log2 = [
    {'country':'France',
     'cities_visited' :["Paris", "Lille", "Dijon"],
     'total_visits' : 12,
     },
    {'country':'Germany',
     'cities_visited' :["Berlin", "Hamburg", "Stuttgart"],
     'total_visits' : 5,
     },
]

print(travel_log2)

add_new_country('Russia', 2, ["Moscow", "St. Petersburg"])
print(travel_log2)
