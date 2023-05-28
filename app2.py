from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add_numbers():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = num1 + num2
        return render_template('result2.html', result=result)
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
