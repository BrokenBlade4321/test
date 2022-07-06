import numpy as np
import pandas as pd


def check_is_string(text) -> bool:
    if not isinstance(text, str):
        return False
    if not text.isalpha():
        return False
    return text[0].isupper()


def check_is_decimal(text) -> bool:
    if isinstance(text, (float, int)):
        return text > 0
    if isinstance(text, str):
        return text.isdecimal()
    return False


def check_is_nan(text) -> bool:
    return text is np.nan


def check_excel_document_is_right(data) -> bool:
    for row in data.iloc.itertuples():
        for i in range(2, len(row)):
            if not check_cell_by_template[row[1]](row[i]):
                return False
    return True


def main(file_name):
    df = pd.read_excel(file_name, header=None)
    if df.shape[1] < 2:
        return False
    if set(df.iloc[0:, 0]) - check_cell_by_template.keys():
        return False
    if check_cell_by_template.keys() - set(df.iloc[0:, 0]) - {np.nan}:
        return False
    if check_excel_document_is_right(df):
        return True
    return False


check_cell_by_template = {'Имя': check_is_string, 'Фамилия': check_is_string, 'Возраст': check_is_decimal, np.nan: check_is_nan}
file = "data1"

if __name__ == '__main__':
    main(f'{file}.xlsx')
