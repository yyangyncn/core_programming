# name track   format: Last, First
name_list = []
error_count = 0


def print_error(times):
    print('Wrong format... should be Last, First')
    print('You have wrong {times} time(s). Fixing input...'.format(times=times))


def name_track(name):
    if ',' not in name:
        return 0
    Last, First = name.split(',')
    if len(Last.strip()) > 1 and len(First.strip()) > 1:
        name_list.append((Last, First))
        return 1
    else:
        return 0

for i in range(6):
    print('L, F', name_list)
    if name_track(input('Enter name:')) == 0:
        error_count += 1
        print_error(error_count)