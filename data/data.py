# 所有和数据库有关的函数方法
import pymysql
# 定义和数据库的连接
conn = pymysql.connect(
    host="rm-2ze51nk5jjx619v0hfo.mysql.rds.aliyuncs.com",
    port=3306,
    user="root",
    passwd="Root123123",
    db="demo",
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

# 1、根据用户名查询用户的函数
def query_user_by_username(username):
    sql = "select * from sys_user where username = %s"
    cur = conn.cursor()
    cur.execute(sql, [username])
    result = cur.fetchone()
    # result是从数据库查询回来的用户信息
    # result有两种结果：1、None  2、{"user_id":1,"username":xxx,"password":"111"}
    return result

# 2、根据用户名和密码添加数据的函数
def add_user(username,password):
    sql = "insert into sys_user (username,password) values (%s,%s)"
    cur = conn.cursor()
    cur.execute(sql, [username,password])
    conn.commit()

# 3、根据用户id查询当前用户的AI助手聊天信息的函数
def query_user_by_username(username):
    sql = "Select * from sys_user where username = %s"
    cur = conn.cursor()
    cur.execute(sql,[username])
    result = cur.fetchone()
    return result

def add_user(username,password):
    sql = "insert into sys_user (username,password) values (%s,%s)"
    cur = conn.cursor()
    cur.execute(sql,[username,password])
    conn.commit()

def query_message_by_id(user_id):
    sql = "Select * from chat_message where user_id = %s"
    cur = conn.cursor()
#根据用户id查询当前用户的AI助手的聊天的函数
    result = cur.execute(sql,[user_id])
    result = cur.fetchall()
    return result

def add_chat_message(user_id,message,role,message_time):
    sql = "insert into chat_message (user_id,message,role,message_time) values (%s,%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(sql,[user_id,message,role,message_time])
    conn.commit()