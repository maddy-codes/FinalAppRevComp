import pandas as pd
import numpy as np


def MakeSheet(DATE, PATH_OPEN, PATH_SAVE):
    open_sheet = pd.read_excel(PATH_OPEN)
    sheet = open_sheet.copy()
    sheet = sheet.rename(columns=sheet.iloc[3])

    sheet.drop([0, 1, 2, 3], axis=0, inplace=True)

    sheet.shape

    sheet.index = range(sheet.shape[0])

    sheet.drop([sheet.shape[0]-1], axis=0, inplace=True)

    for i in range(len(sheet['Debit - Year to date'])):
        if str(sheet['Debit - Year to date'][i]) == 'nan':
            sheet['Debit - Year to date'][i] = 0.0

    for i in range(len(sheet['Credit - Year to date'])):
        if str(sheet['Credit - Year to date'][i]) == 'nan':
            sheet['Credit - Year to date'][i] = 0.0

    sheet['deb-cred'] = sheet['Debit - Year to date'] - sheet['Credit - Year to date']

    sheet['Manual Entry'] = sheet['Account Code']

    sheet['CombinedAccountCode'] = sheet['Account Code'] + " " + sheet['Account']

    sheet['date'] = sheet.shape[0] * [DATE]

    sheet_new = sheet.copy()[['deb-cred', 'Manual Entry',
                              'CombinedAccountCode', 'date']]

    pd.to_datetime(sheet_new['date']).format = '%d%m%Y'

    return sheet_new
