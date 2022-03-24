from flask import Flask , render_template, request

app = Flask('app')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/calc', methods=['POST'])
def calc():
  num1 = request.form.get('num1')
  num2 = request.form.get('num2')
  operador = request.form.get('operador')

  if operador =="+":
    resultado = float(num1) + float(num2)

  if operador =="-":
    resultado = float(num1) - float(num2)

  if operador =="*":
    resultado = float(num1) * float(num2)

  if operador =="/":
    resultado = float(num1) / float(num2)

  return f'{resultado}' 

  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)