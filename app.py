from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, complexity):
    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
        
    return ''.join(random.choice(characters) for i in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form['length'])
        complexity = request.form['complexity']
        password = generate_password(length, complexity)
        return render_template('index.html', password=password)
    return render_template('index.html', password=None)

if __name__ == "__main__":
    app.run(debug=True)

