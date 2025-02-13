def max_new_seats(seats):
    """
    Function to calculate the maximum number of new people who can be seated
    while maintaining a gap of at least 2 seats from any occupied seat.
    """
    count = 0  # Count new people seated
    n = len(seats)  # Get total number of seats

    for i in range(n):
        if seats[i] == 0:  # If seat is empty
            # Check if it's safe to sit here
            if (i == 0 or seats[i - 1] == 0) and (i == n - 1 or seats[i + 1] == 0):
                seats[i] = 1  # Seat the new person
                count += 1

    return count
seats = list(map(int, input("Enter seat arrangement (0 for empty, 1 for occupied) separated by space: ").split()))
max_people = max_new_seats(seats)

print("\nMaximum new people who can be seated:", max_people)


