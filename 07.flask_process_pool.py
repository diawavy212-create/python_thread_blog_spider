import json

import flask
import math
from concurrent.futures import ProcessPoolExecutor
def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    sqrt_n=int(math.floor(math.sqrt(n)))
    for i in range(3,sqrt_n+1,2):
        if n%i==0:
            return False
    return True
app = flask.Flask(__name__)

@app.route('/is_prime/<numbers>')
def api_is_prime(numbers):
    number_list=[int(x) for x in numbers.split(',')]
    results=process_pool.map(is_prime,number_list) #返回是TRUE/FALSe
    return json.dumps(dict(zip(number_list,results)))

if __name__ == '__main__':
    #processpool必须放在下面 而且要在main函数里
    process_pool = ProcessPoolExecutor()
    app.run()