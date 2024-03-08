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

    favicon_url_16 = f"http://www.google.com/s2/favicons?sz=16&domain_url={domain}"
    favicon_url_64 = f"http://www.google.com/s2/favicons?sz=64&domain_url={domain}"
    favicon_url_256 = f"http://www.google.com/s2/favicons?sz=256&domain_url={domain}"

    return f'''
    <h1>Showing favicons for: {domain}</h1>
    <div>
        <img src="{favicon_url_16}" alt="Favicon 16x16">
        <p>16x16</p>
        <a href="{favicon_url_16}" download>Download 16x16</a>
    </div>
    <div>
        <img src="{favicon_url_64}" alt="Favicon 64x64">
        <p>64x64</p>
        <a href="{favicon_url_64}" download>Download 64x64</a>
    </div>
    <div>
        <img src="{favicon_url_256}" alt="Favicon 256x256">
        <p>256x256</p>
        <a href="{favicon_url_256}" download>Download 256x256</a>
    </div>
    '''