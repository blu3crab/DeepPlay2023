import datetime
import numpy as np
from tuner import *
from icecream import ic



def hex_to_int(hex_string):
    return int(hex_string, 16)


def int_to_hex(number):
    hex_string = hex(number)
    # Remove the leading '0x' from the hexadecimal string.
    hex_string = hex_string[2:]
    ic(len(hex_string))
    # if less than 12 chars, insert leading zeros
    leading_zero_count = 12 - len(hex_string)
    if leading_zero_count == 1:
        hex_string = "0" + hex_string
    return hex_string


def remove_rows_with_nan(row):
    """Removes rows with NaN.

    Args:
    row: A Pandas Series object representing the current row of the CSV file.

    Returns:
    None if the row contains NaN, otherwise the row.
    """
    if row.isna().any():
        return None
    else:
        return row

def convert_to_seconds_after_midnight(date_string):
    """Converts a date string to seconds past midnight.

    Args:
    date_string: A string in the format YYYY-MM-DDTHH:MM:SS-TZ.

    Returns:
    An integer representing the number of seconds since midnight.
    """
    # print(f"date_string->,{date_string}")
    if len(date_string) == 0:
        return None  # NAN_TIME

    # 2018-08-14T22:26:00-0400
    date_time = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S-%f")
    #print(date_time)
    date_midnight = date_time.replace(hour=0, minute=0, second=0, microsecond=0)
    #print(date_midnight)

    time_in_seconds = np.int32((date_time - date_midnight).total_seconds())
    # print(time_in_seconds)
    return time_in_seconds

def convert_to_seconds(date_string, ref_year=1970, ref_month=1, ref_day=1):
    """Converts a date string to seconds past 1970-01-01 or ref_year,ref_month,ref_day.

    Args:
    date_string: A string in the format YYYY-MM-DDTHH:MM:SS-TZ.

    Returns:
    An integer representing the number of seconds since 1970-01-01 or ref_year,ref_month,ref_day.
    """
    # print(f"date_string->,{date_string}")
    if len(date_string) == 0:
        return None  # NAN_TIME

    # 2018-08-14T22:26:00-0400
    date_time = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S-%f")
    time_in_seconds = np.int32((date_time - datetime.datetime(ref_year, ref_month, ref_day)).total_seconds())
    # print(time_in_minutes)
    return time_in_seconds

def convert_to_minutes(date_string, ref_year=1970, ref_month=1, ref_day=1):
    """Converts a date string to seconds past 1970-01-01 or ref_year,ref_month,ref_day.

    Args:
    date_string: A string in the format YYYY-MM-DDTHH:MM:SS-TZ.

    Returns:
    An integer representing the number of seconds since 1970-01-01 or ref_year,ref_month,ref_day.
    """
    # print(f"date_string->,{date_string}")
    if len(date_string) == 0:
        return None  # NAN_TIME

    # 2018-08-14T22:26:00-0400
    date_time = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S-%f")
    # return (date_time - datetime.datetime(2018, 1, 1)).total_seconds() // 60
    # return np.int32((date_time - datetime.datetime(2017, 1, 1)).total_seconds() // 60)
    time_in_minutes = np.int32((date_time - datetime.datetime(ref_year, ref_month, ref_day)).total_seconds() // 60)
    # print(time_in_minutes)
    return time_in_minutes


def convert_event_enumeration(event_string):
    if event_string == tuner.ONSET_EVENT_LABEL:
        return tuner.ONSET_EVENT
    elif event_string == tuner.WAKEUP_EVENT_LABEL:
        return tuner.WAKEUP_EVENT
    return tuner.NAN_EVENT


def convert_zangle(zangle_string):
    zangle_float = np.float32(zangle_string)
    zangle = np.int16(zangle_float)

    return zangle


def convert_enmo(enmo_string):
    enmo_float = np.float32(enmo_string)
    enmo = np.uint16(enmo_float * 1000)

    return enmo