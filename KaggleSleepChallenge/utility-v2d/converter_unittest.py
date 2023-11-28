from converter import *

# unit test converters
def converter_unittest():
    print(hex_to_int('038441c925bb'))
    print(int_to_hex(hex_to_int('038441c925bb')))

    print(convert_to_seconds('2018-08-14T22:26:00-0400'))
    print(convert_to_seconds(''))
    print(convert_to_minutes('2018-08-14T22:26:00-0400'))
    print(convert_to_minutes(''))

    print(convert_to_seconds('2018-09-06T04:59:55-0400'))
    duration = convert_to_seconds('2018-09-06T04:59:55-0400') - convert_to_seconds('2018-08-14T22:26:00-0400')
    print(f"begin-end-trial event duration (seconds)->{duration}")

    print(convert_event_enumeration('onset'))
    print(convert_event_enumeration('wakeup'))
    print(convert_event_enumeration('dunno'))

    print(convert_zangle('2.636700'))
    print(convert_zangle('-90.636700'))

    print(convert_enmo('0.0216'))