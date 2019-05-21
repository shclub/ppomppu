from flask import Flask , request
app = Flask(__name__)

from ppomppu_monitor import monitor_start 

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/ppomppu_monitor')
def ppomppu_monitor():
    req_data = request.get_json()
    param_lists = req_data['param_list']
    param_list = param_lists.split(",")  
    monitor_start(param_list[0],param_list[1],param_list[2],param_list[3],param_list[4],param_list[5],param_list[6],param_list[7],param_list[8],param_list[9],param_list[10])
    return 'OK'

#curl -X GET -H 'Content-Type:application/json'  http://localhost:5003/ppomppu_monitor -d '
#{"param_list" : "localhost,5555,/postanal/?post=,1,N,KT,Y,localhost,27017,50026600,676003420:AAH7fq_HZzxbmWurz-IWdeUh6vZN1QTQxsE"}'

if __name__=='__main__':
    app.run(host= '0.0.0.0',port=5003,debug=True)
