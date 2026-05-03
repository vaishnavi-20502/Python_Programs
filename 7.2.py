def process_cities(file_name):
    with open(file_name, 'r') as file:
        cities = [line.strip().split() for line in file]

    for city in cities:
        city_name, population, area = city
        population = float(population.replace(',', ''))
        area = float(area)
        print(f"City: {city_name}, Population: {population} Lakhs, Area: {area} sq KM")

    cities_with_population_more_than_10 = [city[0] for city in cities if float(city[1].replace(',', '')) > 10]
    print(f"City names with population more than 10 Lakhs: {cities_with_population_more_than_10}")

    total_area = sum(float(city[2]) for city in cities)
    print(f"Sum of areas of all cities: {total_area} sq KM")

process_cities('city.txt')