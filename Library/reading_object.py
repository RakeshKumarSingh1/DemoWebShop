import xlrd
from Library.config import Config


class ReadExcel:

    def read_test_data(self):
        workbook = xlrd.open_workbook(Config.DATA_PATH)
        worksheet = workbook.sheet_by_name(Config.Data_Sheet)
        columns= worksheet.ncols
        rows = worksheet.get_rows()
        header = next(rows)

        list_ = []

        for row in rows:
            # values = ()
            # for j in range(columns):
            #     values +=(row[j].value,)
            #     list_.append(values)
            list_.append((row[0].value,row[1].value, row[2].value,row[3].value,row[4].value,row[5].value,row[6].value))

        return list_


    def read_locators(self,sheetname):
            workbook = xlrd.open_workbook(Config.LOCATOR_PATH)
            worksheet = workbook.sheet_by_name(sheetname)
            columns=worksheet.ncols
            rows = worksheet.get_rows()
            header=next(rows)
            data = {}
            for row in rows:
                data[row[0].value] = (row[1].value,row[2].value)
            return data


n = ReadExcel()
h = n.read_test_data()
print(h)