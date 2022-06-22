from flask import Flask, request, jsonify, redirect, url_for, make_response, render_template


app = Flask(__name__)

# @app.route('/<name>/<int:age>',methods=['POST'])
# def main_with_params(name,age):
#     return 'Hello %s mmy age is %s' % (name,age) , 200

# @app.route('/redirected', methods=['GET'])
# def redirected():
#     return 'Redirected', 200

# @app.route('/request', methods=['POST'])
# def request_data():
    
#     print (request.args)
#     person = request.args.get('person')
#     print (request.method)
#     print (request.headers.get('User-Agent'))
#     print (request.headers)
#     print(request.path)
#     return 'Hello my name is %s and I have %s years old.' % (request.form['name'], request.form['age']), 200
#     #request.form['name']

# @app.route('/response', methods=['POST'])
# def response_data():
#     obj = {
#         'username':'evertonkrystian',
#         'facebook':'https://fb.me/evertonkrystian',
#         'github'  : 'https://github.com/evertonkrytian'
#     }

#     resp = make_response(jsonify(data = request.form), 201)
#     resp.headers['Couse-Powered-By'] = "BLKSolutions"

#     return resp

#     #return jsonify(data = request.form), 201
#     #return redirect(url_for('redirected'))
#     #return redirect('/redirected', code = 302)





@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        return redirect(url_for('result', name = request.form['name']))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error = error), 404

@app.route('/result/<name>', methods=['GET'])
def result(name):
    return render_template('main.html',name = name)


if __name__ == '__main__':
    app.run(debug=True)