from flask import render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user
from flask_login import login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, mongo
from app.models import User

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({'_id': user_id})

    if user_data:
        return User(user_data['username'], 
                    user_data['password'], 
                    user_data['role'])

    return None  # Return None if user not found


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_data = User.find_by_username(username)

        if user_data and check_password_hash(user_data['password'], password):
            user = User(username, user_data['password'], user_data['role'])
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))

        flash('Invalid username or password', 'danger')
        
    else:
        # Handle other HTTP methods if needed
        return "Method not allowed", 405  

    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)

        # Save file info to MongoDB
        mongo.db.files.insert_one({
            'filename': file.filename,
            'uploader': current_user.username
        })

        return jsonify({'success': 'File uploaded successfully'}), 200


@app.route('/download/<filename>', methods=['GET'])
@login_required
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if os.path.isfile(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({'error': 'File not found'}), 404
