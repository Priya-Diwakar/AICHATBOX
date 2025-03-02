from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__, template_folder="templates")  # Make sure 'templates' folder is used

@app.route('/')
def home():
    return render_template('box.html')  # Flask will look inside the 'templates/' folder

@app.route('/start/<string:conversation_type>')
def start_chat(conversation_type):
    """Starts a client chat based on conversation type."""
    chat_types = ["teacher-student", "ai-client", "group-discussion"]
    
    if conversation_type in chat_types:
        subprocess.Popen(['python', 'client.py', conversation_type])

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
