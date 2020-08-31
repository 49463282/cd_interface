from tools.Redis import DBRedis
from tools.PyMysql_cd import DBUtil
import app

sql = 'select id from t_user where mobile = 15856732315 and type = 0 and status = 1 and tenant_id = 10310'
re = DBUtil.cursor(sql, app.userDB)
userID = DBUtil.fetch(re, 'fetchone')
r = DBRedis.get_connect()
user = 'user:security:userId:10310:%d' % int(userID[0])
token = r.get(user)
print(token)
