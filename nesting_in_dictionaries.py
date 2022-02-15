#nesting lists in a dictionary ,dictionary in a dictionary and dictionaries in a list



#nesting lists in a the dictonary
pak_cities={"Country":"Pakistan",
                "big_Cities":["Karachi","Hyderabad","Sukkur","Khairpur"],
                "Sindh_rural":["Khairpur","Noshoro","Larkana"],
                "total_visited":12
        }
print(pak_cities["Sindh_rural"])
print()



#nesting a dictionary in a dictionary
pak_cities={"cities_visited":["Karachi","Hyderabad","Sukkur","Khairpur"]}
print(pak_cities["cities_visited"])
print()



#nesting dictionaries in a list
overall=[{"big_Cities":["Karachi","Hyderabad","Sukkur","Khairpur"],
                "Sindh_rural":["Khairpur","Noshoro","Larkana"]
        },
        {"cities_visited":["Karachi","Hyderabad","Sukkur","Khairpur"]}]
print(overall)