# flask microflameworks necessita de ausiliares para um site completo,
# para algoritimos
# exemplo de site usando 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('lolde.html')

@app.route('/blog')
def blog():
    return'bem vindo ao blog'

if __name__ == '__main__':
    app.run(debug=True)
    app.dump()


