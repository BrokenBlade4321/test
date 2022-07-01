import numpy as np
import pandas as pd


def check_is_string(text) -> bool:
    if isinstance(text, (int, float)):
        return False
    if not text.isalpha():
        return False
    return text[0].isupper()


def check_is_decimal(text) -> bool:
    if isinstance(text, int):
        return text > 0
    if isinstance(text, float):
        return False
    return text.isdecimal()


def check_is_nan(text) -> bool:
    return text is np.nan


def check_excel_document_is_right(data) -> bool:
    for row in data.iloc[0:, 0:].itertuples():
        for i in range(2, len(row)):
            if not CONST[row[1]](row[i]):
                return False
    return True


def main(file_name):
    df = pd.read_excel(file_name, header=None)
    if df.shape[1]<2:
        print("Таблица не заполнена")
        return
    if output := (set(df.iloc[0:, 0]) - CONST.keys()):
        print(f"{','.join(output)} не являются шаблонами")
        return
    if output := (CONST.keys() - set(df.iloc[0:, 0]) - {np.nan}):
        print(f"{','.join(output)} не были введены")
        return
    if check_excel_document_is_right(df):
        print("верного формата")
        return
    print("неверного формата")


CONST = {'Имя': check_is_string, 'Фамилия': check_is_string, 'Возраст': check_is_decimal, np.nan: check_is_nan}
file = "data1"

if __name__ == '__main__':
    main(f'{file}.xlsx')
