from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hk2827', methods=['GET'])
def main():
    return render_template('mypage.html')


if __name__ == '__main__':
    app.run()
