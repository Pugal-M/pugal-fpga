
from flask import Flask,request,jsonify # type: ignore

app = Flask (__name__)

@app.route('/api', methods = ['GET'])
 
def returnascii():
    d = {}
    inputchr = str(request.args.get('query'))
    answer = str(ord (inputchr))
    d['output'] = answer
    return d



if __name__== "__main__":
    app.run()