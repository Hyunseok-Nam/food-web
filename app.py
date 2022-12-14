from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')    #홈페이지 가장 상위 루트 www.aaa.com/
def hello():
    return render_template('index.html')
    # return 'Hello, World!'

@app.route('/naver')    
def naver():
    return '네이버 사이트'

@app.route('/food')    
def food():
    foodlist = ["짜장면", "스시", "피자", "치킨", "커리"]
    foodname = random.choice(foodlist)
    return render_template('food.html', data=foodname)

if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=80)
