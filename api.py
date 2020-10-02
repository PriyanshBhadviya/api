from flask import Flask, request
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()
# mysql configuratoin
app.config['MYSQL_DATABASE_HOST']       = 'localhost'
app.config['MYSQL_DATABASE_USER']       = 'root'
app.config['MYSQL_DATABASE_PASSWORD']   = 'monika@8872'
app.config['MYSQL_DATABASE_DB']         = 'customer'
mysql.init_app(app)

@app.route('/', methods = ['GET'])
def index():
    return "Password saving for website"

@app.route('/app/user', methods = ['POST'])
def register():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO account (
                username,
                password
            ) 
            VALUES (%s,%s)""", (user, password))
    conn.commit()
    conn.close()
    content = request.get_json()
    return content

@app.route('/app/user/auth', methods = ['POST'])
def login():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM account")
    data = cursor.fetchall()
    dataList = []
    if data is not None:
        for item in data:
            dataTempObj = {
                'name': item[1],
                'password': item[2]
            }
            dataList.append(dataTempObj)
        return json.dumps(dataList)
    else:
        return 'data kosong'
    content = request.get_json()
    return content

@app.route('/app/sites/list', methods = ['GET'])
def getnoteInfo():
    userId = request.args.get('user_id')
    return request.args.get('user_id')

@app.route('/app/sites', methods = ['POST'])
def addWebsiteInfo():
    userId = request.args.get('user')
    content = request.get_json()
    return userId, content

if __name__ == '__main__':
    app.run()
