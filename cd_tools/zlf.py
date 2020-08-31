import pandas


io = "C:\\Users\\dell\\Desktop\\1.txt"
df = pandas.read_table(io, sep=",")
print(df)
data = df.to_dict(orient='record')
print(data)
url = "https://ir.zlf.cn/openapi/store/update_account_id"
data = {"accountId": 1, "storeId": 1, "tenantId": 1}
headers = {
    "token": "954f85f6-f095-491a-ba3a-c397eb93b6c3",
    "Content-Type": "application/json;charset=UTF-8"
}
# response = requests.post(url, json.dumps(data), headers=headers)



