from collections import defaultdict

STREET_LOOK_UP = {}


def read_file(input_file):
    file = open(input_file, 'r')
    line = file.readline()
    data = line.split()

    D = int(data[0])  # duration
    I = int(data[1])  # intersection
    S = int(data[2])  # no. of streets
    V = int(data[3])  # no. of cars
    F = int(data[4])  # score

    street_list = []  # list of dict{start_I, end_I, name, time}

    for i in range(S):
        line = file.readline()
        data = line.split()

        street = {}
        street['index'] = i
        street['start_I'] = int(data[0])
        street['end_I'] = int(data[1])
        street['name'] = data[2]
        street['time'] = int(data[3])
        street['has_car'] = []  # list of car index present at the end of the street

        STREET_LOOK_UP[street['name']] = street['index']

        street_list.append(street)

    car_list = []
    for i in range(V):
        line = file.readline()
        data = line.split()

        car = {}
        car['index'] = i
        car['length'] = int(data[0])
        car['roads'] = data[1:]

        car_list.append(car)

    return D, I, S, V, F, street_list, car_list


def get_intersection(street_list, car_list, i):
    current_street = street_list[STREET_LOOK_UP[car_list[i]['roads'][0]]]
    return current_street['end_I']


def simulation(street_list, car_list, intersections):
    K = [[{'intersection': -1, 'score': -1000000} for car in range(V)] for sec in range(D+1)]

    for car in range(V): # car index
        for sec in range(D+1): # sec
            if sec == 0:
                K[car][sec] = {'intersection': get_intersection(street_list, car_list, car), 'score': (-len(car_list[car]['roads'])+1)}
            else:
                # TODO complete this block
                if K[car][sec-1]['intersection'] != -1:
                    # K[car][sec] =
                    pass


def run_simulation(street_list, car_list, intersections):
    for s in street_list:
        for car in s['has_car']: # list of cars at the end of the street
            # first car at the end of the road
            current_street = street_list[STREET_LOOK_UP[car_list[car]['roads'].pop(0)]]
            print(current_street['end_I'])


if __name__ == '__main__':
    input_file = 'C:/Users/safat/Downloads/hash_code_2021/a.txt'

    D, I, S, V, F, streets, cars = read_file(input_file)

    print(f"{D} {I} {S} {V} {F}")

    for street in streets:
        a = street['start_I']
        b = street['end_I']
        c = street['name']
        d = street['time']
        print(f"{a} {b} {c} {d}")

    for car in cars:
        a = car['length']
        b = car['roads']
        print(f"{a} " + " ".join(b))

    print(STREET_LOOK_UP)

    intersection_dict = defaultdict(list)

    for s in streets:
        intersection_dict[int(s['end_I'])].append(s['name'])

    for car in cars:
        streets[STREET_LOOK_UP[car['roads'][0]]]['has_car'].append(car['index'])

    print(intersection_dict)
    # run_simulation(streets, cars, intersection_dict)
    print(get_intersection(streets, cars, 1))



