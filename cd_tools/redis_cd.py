from tools.Redis import DBRedis
from tools.PyMysql_cd import DBUtil
import app

sql = 'select id from t_user where mobile = 13627840350 and type = 1 and status = 1 and tenant_id = 508'
re = DBUtil.product(sql, app.userDB)
userID = DBUtil.fetch(re, 'fetchone')
r = DBRedis.get_connect()
user = 'user:security:userId:508:%d' % int(userID[0])
token = r.get(user)
print(token)
