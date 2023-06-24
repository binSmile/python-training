def getdate(infn):
    """
    Extracts the date from the file name depending on the source.
    """
    name, ext = infn.split('.')
    match infn[:3]:
        case 'PXL':
            fp = name.split('_')[1]
            y = fp[:4]
            m = fp[4:6]
            d = fp[6:8]
        case 'DCI':
            fp = name.split('-')
            y = fp[1]
            m = fp[2]
            d = fp[3]
        case _:
            fp = name
            y = fp[:4]
            m = fp[4:6]
            d = fp[6:8]

    return '_'.join([y, m, d])


def stat(calendar, lines):
    """
    Counts the number of photos for each day.
    """
    event_counts = {}
    for fname in lines:
        date = getdate(fname)
        event_counts[calendar[date]][1] = event_counts.setdefault(calendar[date], [date, 0])[1] + 1

    return event_counts


def eventselector(events):
    """
    Creates a dictionary of events by dates.
    """
    calendar = {}
    for event in events:
        parts = event.split()
        date = '_'.join(parts[1:])
        calendar[date] = parts[0]
    return calendar


def main():
    from sys import stdin
    lines = [line.rstrip('\n') for line in stdin]

    calendar = eventselector(lines[0:3])
    event_stats = stat(calendar, lines[3:])
    sorted_events = sorted(event_stats.keys())

    for event in sorted_events:
        date, count = event_stats[event]
        for i in range(count):
            print(f'{event}_{date}_{i}.jpg')


if __name__ == '__main__':
    main()



