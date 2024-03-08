# save this as app.py, use . fl_venv/bin/activate to run
from flask import Flask, request, render_template_string, redirect, url_for
import validators

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template_string("""
        <form method="POST" action="{{ url_for('submit_domain') }}">
            <input type="text" name="domain" placeholder="Enter website (google.com)">
            <input type="submit" value="Submit">
        </form>
    """)

@app.route("/submit", methods=['POST'])
def submit_domain():
    domain = request.form.get('domain')

    if not validators.domain(domain):
        return "Invalid domain. Please enter a valid domain."

    favicon_url = f"http://www.google.com/s2/favicons?sz=64&domain_url={domain}"

    return f'<img src="{favicon_url}" alt="Favicon"><br><a href="{favicon_url}">Click here to get favicon</a>'