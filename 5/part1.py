import sys

def parse_map(input_file):
    f.readline()
    source_to_dest_map = []
    line = input_file.readline().strip()

    while line:
        source_to_dest_map.append([int(x) for x in line.split()])
        line = input_file.readline().strip()

    return source_to_dest_map

def lookup(value, lookup_map):
    for destination, source, lookup_range in lookup_map:
        if source <= value <= source + lookup_range - 1:
            return (value - source) + destination

    # Did not find in map, default to original value
    return value


def get_location_for_seed(
        seed, 
        soil_map, 
        fertilizer_map,
        water_map,
        light_map,
        temp_map,
        humidity_map,
        location_map):

    soil = lookup(seed, soil_map)
    fertilizer = lookup(soil, fertilizer_map)
    water = lookup(fertilizer, water_map)
    light = lookup(water, light_map)
    temp = lookup(light, temp_map)
    humidity = lookup(temp, humidity_map)
    location = lookup(humidity, location_map)

    return location


with open(sys.argv[1]) as f:
    seeds = [int(num) for num in f.readline().split(':')[1].split()]

    f.readline()

    soil_map = parse_map(f)
    fertilizer_map = parse_map(f)
    water_map = parse_map(f)
    light_map = parse_map(f)
    temp_map = parse_map(f)
    humidity_map = parse_map(f)
    location_map = parse_map(f)

locations = (get_location_for_seed(seed, soil_map, fertilizer_map, water_map, 
                                   light_map, temp_map, humidity_map, location_map)
                for seed in seeds)

print(min(locations))








        

    
