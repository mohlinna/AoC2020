
def get_seat_id(boarding_pass):
    binary_rep = boarding_pass.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
    return int(binary_rep, 2)


def find_max_seat_id(boarding_passes):
    seat_ids = map(get_seat_id, boarding_passes)
    return max(seat_ids)


if __name__ == '__main__':
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    max_seat = find_max_seat_id(lines)
    print("Max Seat Number:  {}".format(max_seat))
