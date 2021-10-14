'''
a tuple is similar to a list, they are immutable

tuple1 = ("emily", "jack", "joe")
you will get an error if you tried to tuple1[0] = "molly"

you can access them, you just cant change them
'''

tuple1 = ("emily", "jack", "joe")
print(tuple1[1])

#dictionaries /aka maps
#dictionaries are a bunch of keys with a value for each key

d = {}

d[1996] = 'rat'
d[1995] = 'pig'
d[1994] = 'goat'
d[1993] = 'monkey'

print("dictionary:", d) # key: value, key: value, key: value

print("d[1994]:", d[1994])

#keys can also be strings

# d.keys() returns the keys
print(d.keys())

# d.values() returns the values
print(d.values())

# d.items returns the pairs
print(d.items())

#swapi example:
deathStarD = {
	"name": "Death Star",
	"model": "DS-1 Orbital Battle Station",
	"manufacturer": "Imperial Department of Military Research, Sienar Fleet Systems",
	"cost_in_credits": "1000000000000",
	"length": "120000",
	"max_atmosphering_speed": "n/a",
	"crew": "342,953",
	"passengers": "843,342",
	"cargo_capacity": "1000000000000",
	"consumables": "3 years",
	"hyperdrive_rating": "4.0",
	"MGLT": "10",
	"starship_class": "Deep Space Mobile Battlestation",
	"pilots": [],
	"films": [
		"https://swapi.dev/api/films/1/"
	],
	"created": "2014-12-10T16:36:50.509000Z",
	"edited": "2014-12-20T21:26:24.783000Z",
	"url": "https://swapi.dev/api/starships/9/"
    }

print("death star keys:", deathStarD.keys())

print("death star passengers:", deathStarD["passengers"])

#you can delete a whole key
del deathStarD["passengers"]

print(deathStarD.keys())

#you can change the value of a value
print("death star hyperdrive_rating:", deathStarD["hyperdrive_rating"])
deathStarD["hyperdrive_rating"] = "50.0"
print("death star hyperdrive_rating:", deathStarD["hyperdrive_rating"])


if 'manufacturer' in deathStarD:
    print("manufacturer:", deathStarD["manufacturer"])
else:
    print("no manufacturer")

#you can pop a key/value out of a dictionary (returns and removes it)
#you can also push a new key/value into the dictionary
