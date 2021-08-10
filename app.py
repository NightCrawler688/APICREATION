from flask import Flask,jsonify,request

app = Flask(__name__)
tasks = [
    {
        'Id':1,
        'Title':u'Buy Groceries',
        'Description':u'Milk,Cheese,Pizza',
        'Done':False
    },
    {
        'Id':2,
        'Title':u'Learn Python',
        'Description':u'Find new codes online',
        'Done':False
    }
]
@app.route('/add-data',methods = ['POST'])
def add_task():
    if not request.json:
            return jsonify({
                'status':'Error',
                'message':'Please provide the data'
            })
    task = {
        'Id':tasks[-1]['Id'] + 1,
        'Title':request.json['Title'],
        'Description':request.json.get('Description',''),
        'Done':False
    }
    tasks.append(task)
    return jsonify({
        'status':'Succes',
        'message':'Task added successfully'
    })
@app.route('/get-data')
def get_task():
    return jsonify({
        'data':tasks
    })
if(__name__ == '__main__'):
    app.run(debug = True)
