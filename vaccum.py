
room = {}
room['A'] = input("Enter status of Room A (Dirty/Clean): ")
room['B'] = input("Enter status of Room B (Dirty/Clean): ")
position = input("Enter vacuum position (A/B): ")
print("\nInitial State:", (position, room['A'], room['B']))
while room['A'] == 'Dirty' or room['B'] == 'Dirty':

    if room[position] == 'Dirty':
        print("Action: Suck")
        room[position] = 'Clean'

    else:
        if position == 'A':
            print("Action: Move Right")
            position = 'B'
        else:
            print("Action: Move Left")
            position = 'A'

    print("Current State:", (position, room['A'], room['B']))

print("\nGoal State:", (position, room['A'], room['B']))
print("Both rooms are clean.")