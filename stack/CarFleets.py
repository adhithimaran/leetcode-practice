def carFleet(target, position, speed):
    n = len(position)
    fleet_times = [] # stack DS
    position.sort(reverse=True)
    print(f'this is positions array sorted: \n{position}')

    for i in range(len(position)):
        time_to_target = (target - position[i]) / speed[i]
        print(f'this is time to target: \n{time_to_target}')

        if fleet_times == [] or time_to_target > fleet_times[-1]:
            fleet_times.append(time_to_target)

    return len(fleet_times)


target = 10
position = [4,1,0,7]
speed = [2,2,1,1]
# 3
print(carFleet(target, position, speed))

