from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

USERNAME = 'admin'
PASSWORD = 'S3cr3TP4ssw0rd1@'
TERMINAL_PASSWORD = 'xxxxxxxxx'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials. Please try again.')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('admin.html')

@app.route('/admin/BhGBgUi8333')
def flag():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('flag.html')

@app.route('/admin/location')
def location():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    images = [
        'xxxx',
        'xxxx',
        'xxxx',
        'xxxx'
    ]
    return render_template('location.html', images=images)

@app.route('/admin/terminal', methods=['GET', 'POST'])
def terminal():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        terminal_password = request.form['terminal_password']
        if terminal_password == TERMINAL_PASSWORD:
            session['terminal_access'] = True
            return redirect(url_for('terminal_page'))
        else:
            flash('Invalid terminal password. Please try again.')
            return redirect(url_for('terminal'))
    return render_template('terminal_protected.html')

@app.route('/admin/terminal_page')
def terminal_page():
    if not session.get('logged_in') or not session.get('terminal_access'):
        return redirect(url_for('terminal'))
    return render_template('terminal.html')

@app.route('/secrets')
def secrets():
    return render_template('secrets.html')

@app.route('/RARE')
def rare():
    return render_template('rare.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
#http://66.11.105.128:50059/
