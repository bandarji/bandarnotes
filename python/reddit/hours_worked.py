def time_worked(clocked_in, clocked_out):
    """Return hours and minutes worked.
    Args:
        clocked_in: str, military time
        clocked_out: str, military time
    Returns:
        (
            hours: int, count of hours,
            mins: int, count of minutes
        ): tuple
    """
    section_time = lambda time_str: [int(i) for i in time_str.split(':')]
    conv_time_to_mins = lambda ts: (ts[0] * 60) + ts[1]
    time_in = section_time(clocked_in)
    time_out = section_time(clocked_out)
    minutes_in = conv_time_to_mins(time_in)
    minutes_out = conv_time_to_mins(time_out)
    delta = minutes_out - minutes_in
    hours = delta / 60
    mins = delta % 60
    return (hours, mins)

print(time_worked('8:12', '19:42'))
