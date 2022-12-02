 def turn_right():
    turn_left()
    turn_left()
    turn_left()
turn_count = 0
while not at_goal():
    if right_is_clear() and turn_count < 4:
        turn_count += 1
        turn_right()
        move()
    elif front_is_clear():
        turn_count = 0
        move()
    else:
        turn_count = 0
        turn_left()
