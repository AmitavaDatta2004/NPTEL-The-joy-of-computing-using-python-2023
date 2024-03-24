station_dict = {}

n = int(input())

for _ in range(n):
    train_name = input()
    m = int(input())

    compartment_dict = {}
    for _ in range(m):
        compartment_name, num_passengers = input().split(",")
        compartment_dict[compartment_name] = int(num_passengers)

    station_dict[train_name] = compartment_dict
