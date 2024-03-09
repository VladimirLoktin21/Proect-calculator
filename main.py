from flask import Flask, render_template, request

app = Flask(__name__)

def result_calculate(size, lights, device):
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<size>')
def lights(size):
    return render_template('lights.html', size=size)

@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    result = result_calculate(int(size), int(lights), int(device))
    return render_template('end.html', result=result)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']  
    date = request.form['date']


    with open('form.txt', 'a') as f:
        f.write(f"Name: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Date: {date}\n\n")

    return render_template('form_result.html', name=name, email=email, address=address, date=date)

if __name__ == '__main__':
    app.run(debug=True)
