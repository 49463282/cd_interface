import os
import pandas as pd
import json
import app
from tools.PyMysql_cd import DBUtil
import datetime


class Excel:
    def excel_reade(self, io, sheet_name=None):
        # io = r"../data/员工导入模板 (1213).xlsx"
        df = pd.read_excel(io, sheet_name=sheet_name)
        # df = excel_file.to_dict(orient='record')
        # 遍历字典
        # data = [row for row in zip(df["员工姓名"], df["员工手机号码"])]
        # for store_code, mobile in data:
        #     # data("员工姓名", "员工手机号码")
        #     print(store_code)
        #     print(mobile)

        # return data
        # 效率更高的遍历方法
        return df
        # for row in zip(df["员工姓名"], df["员工手机号码"]):
        #     yield row

        # for i in data:
        #     param = json.dumps(i, ensure_ascii=False)
        #     print(param)

    def excel_writer(self, sql, filename, conn):
        curr_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
        data = pd.read_sql(sql, conn)
        df = pd.DataFrame(data)
        DBUtil.close_res(conn)
        file_name = f"{filename}_{time_str}.xlsx"
        file_path = os.path.join(app.ABS_DIR, "report", file_name)
        df.to_excel(file_path, index=False, engine="xlsxwriter")


if __name__ == '__main__':
    excel = Excel()
    # Excel.excel_writer()
    data = excel.excel_reade()
    for name, mobile in data:
        print(name, mobile)
