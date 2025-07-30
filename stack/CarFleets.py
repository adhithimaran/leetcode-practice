def carFleet(target, position, speed):
    n = len(position)
    
    # Create pairs of (position, speed) and sort by position in descending order
    cars = list(zip(position, speed))
    cars.sort(reverse=True)  # Sort by position (descending)
    
    print(f'Cars sorted by position (desc): {cars}')
    
    fleet_times = []  # stack to track fleet arrival times
    
    for pos, spd in cars:
        time_to_target = (target - pos) / spd
        print(f'Car at position {pos} with speed {spd}: time = {time_to_target}')
        
        # If this car takes longer than the previous fleet, it forms a new fleet
        if not fleet_times or time_to_target > fleet_times[-1]:
            fleet_times.append(time_to_target)
            print(f'New fleet formed. Fleet times: {fleet_times}')
        else:
            print(f'Car joins existing fleet (time {time_to_target} <= {fleet_times[-1]})')
    
    return len(fleet_times)


target = 10
position = [4,1,0,7]
speed = [2,2,1,1]
# 3
print(carFleet(target, position, speed))

