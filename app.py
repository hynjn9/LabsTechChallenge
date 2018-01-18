from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/hk2827', methods=['GET'])
def my_page():
    return render_template('mypage.html')


if __name__ == '__main__':
    app.run()
