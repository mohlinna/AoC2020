
def get_seat_id(boarding_pass):
    binary_rep = boarding_pass.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
    return int(binary_rep, 2)


def find_my_seat(boarding_passes):
    seat_ids = sorted(map(get_seat_id, boarding_passes))
    print(seat_ids)
    seat_candidate = seat_ids[0]
    for seat in seat_ids:
        if seat != seat_candidate:
            return seat_candidate
        seat_candidate += 1


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    mine = find_my_seat(lines)
    print("My Seat Number:  {}".format(mine))
