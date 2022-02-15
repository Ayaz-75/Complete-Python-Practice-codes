





visited_log=[
    {
        "country":"France",
        "Visited":12,
        "cities":["Paris","lile","Dijon"]
    }
    ,
    {
        "country":"Germany",
        "visited":5,
        "cities":["berlin","hamburg","stuttgart"]
    }
]


def add_new_country(name,visited_number,cities_names):
    country_to_add={}
    country_to_add["country"] = name
    country_to_add["visited"] = visited_number
    country_to_add["cities"] = cities_names
    visited_log.append(country_to_add)

add_new_country("Russia",2,["Moscow","saint petesburg"])

print(visited_log)