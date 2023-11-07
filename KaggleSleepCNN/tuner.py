####################################################################
from types import SimpleNamespace
tuner = SimpleNamespace(
    # column labels
    SERIES_ID_COLUMN = 'series_id',
    NIGHT_COLUMN = 'night',
    EVENT_COLUMN = 'event',
    STEP_COLUMN = 'step',
    TIME_COLUMN = 'timestamp',

    NAN_TIME = 0,

    ANGLEZ_COLUMN = 'anglez',
    ENMO_COLUMN = 'enmo',

    # event labels
    ONSET_EVENT_LABEL = 'onset',
    WAKEUP_EVENT_LABEL = 'wakeup',

    # event enumeration
    NAN_EVENT = 0,
    ONSET_EVENT = 1,
    SLEEP_EVENT = 2,
    WAKEUP_EVENT = 3,
    WAKE_EVENT = 4
)
####################################################################