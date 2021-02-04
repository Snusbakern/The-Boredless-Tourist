destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index
get_destination_index('Los Angeles, USA')
def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index
test_destination_index = get_traveler_location(test_traveler)
attractions = [[] for i in destinations]
def add_attraction(destination, attraction):
    try:
        destination_index = get_destination_index(destination)
    except:
        return
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for i in attractions_in_city:
        possible_attraction = i
        attraction_tags = possible_attraction[1]
        for n in interests:
            if n in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest
la_arts = find_attractions('Los Angeles, USA', ['art'])
def get_attraction_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = 'Hi '
    interests_string += traveler[0]
    interests_string += ", we think you'll like these places around "
    interests_string += traveler_destination
    interests_string += ': '
    def list_to_string(s):
        str1 = ''
        for i in s:
            str1 += i + '"'
            if i != s[-1]:
                str1 += ', '
        return str1
    interests_string += list_to_string(traveler_attractions)
    return interests_string
smills_france = get_attraction_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
