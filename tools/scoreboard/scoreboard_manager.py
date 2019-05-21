from google_api_connector import get_sheet_data, set_sheet_data

SPREADSHEET_ID = '1iyS40VZfcHgirbZSmfjvhTeR4B0xCerU2-bvO6iekZc'
RANGE_NAME = 'F2:F175'
UPDATE_RANGE_NAME = 'G2:G175'
SAMPLE_DATA = {'Braxiatel': 45, 'andreyDemidenko': 30, 'DennySoul': 25}


def main():
    users_list = get_sheet_data(SPREADSHEET_ID, RANGE_NAME)

    data = get_data_for_update()
    cells_values = []
    for user_data in users_list:
        cells_values.append(data[user_data[0]] if len(user_data) > 0 and user_data[0] in data else '')

    set_sheet_data(SPREADSHEET_ID, UPDATE_RANGE_NAME, cells_values)


def get_data_for_update():
    """ ToDo Replace Mock with real data provider
    """
    return SAMPLE_DATA


if __name__ == '__main__':
    main()
