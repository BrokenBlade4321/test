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


def check_excel_document_is_right(data) -> bool:
    for row in data.iloc[0:, 0:].itertuples():
        for i in range(2, len(row)):
            if not CONST[row[1]](row[i]):
                return False
    return True


def main(file):
    df = pd.read_excel(file)
    if (set(df.iloc[0:, 0]) - set(CONST.keys())):
        print("неверного формата")
    elif check_excel_document_is_right(df):
        print("верного формата")
    else:
        print("неверного формата")


CONST = {'Имя': check_is_string, 'Фамилия': check_is_string, 'Возраст': check_is_decimal}
file = "data"

if __name__ == '__main__':
    main(file)
