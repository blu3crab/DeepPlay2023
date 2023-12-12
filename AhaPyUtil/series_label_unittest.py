
def gen_series_list_equal():
    # series time = onset or wakeup event time
    dummy_series_list = [['038441c925bb', 51031800, 2, 21],\
                    ['038441c925bb', 51031805, 2, 21],\
                    ['038441c925bb', 51056760, 2, 21],\
                    ['038441c925bb', 51057000, 2, 21],\
                    ['038441c925bb', 51067800, 2, 21],\
                    ['038441c925bb', 51086460, 2, 21],\
                    ['038441c925bb', 51087460, 2, 21],\
                    ['038441c925bb', 51088460, 2, 21],\
                    ['038441c925bb', 51133020, 2, 21],\
                    ['038441c925bb', 51143020, 2, 21],\
                    ['038441c925bb', 51153020, 2, 21],\
                   ]
    return dummy_series_list

def gen_series_list_unequal():
    # series time != onset or wakeup event time
    dummy_series_list = [['038441c925bb', 51031800, 2, 21],\
                    ['038441c925bb', 51031805, 2, 21],\
                    ['038441c925bb', 51056761, 2, 21],\
                    ['038441c925bb', 51057000, 2, 21],\
                    ['038441c925bb', 51067800, 2, 21],\
                    ['038441c925bb', 51086461, 2, 21],\
                    ['038441c925bb', 51087460, 2, 21],\
                    ['038441c925bb', 51088460, 2, 21],\
                    ['038441c925bb', 51133021, 2, 21],\
                    ['038441c925bb', 51143020, 2, 21],\
                    ['038441c925bb', 51153020, 2, 21],\
                   ]
    return dummy_series_list

def unittest_label_series():
    #unit test label_series
    column_headers = list(train_series_x.columns.values)
    #generate dummy series
    dummy_series_list = gen_series_list_equal()
    dummy_series_array = np.array(dummy_series_list)
    dummy_series_df = pd.DataFrame(dummy_series_array, columns=column_headers)
    series_label_list = label_series(series_id_list, train_event_x, dummy_series_df)
    ic(series_label_list)
    dummy_series_list = gen_series_list_unequal()
    dummy_series_array = np.array(dummy_series_list)
    dummy_series_df = pd.DataFrame(dummy_series_array, columns=column_headers)
    series_label_list = label_series(series_id_list, train_event_x, dummy_series_df)
    ic(series_label_list)

