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
    <table style="border-collapse: collapse; width: 100%;">
        <tr>
            <th style="border: 1px solid black; padding: 10px; text-align: center;">Icon</th>
            <th style="border: 1px solid black; padding: 10px; text-align: center;">Size</th>
            <th style="border: 1px solid black; padding: 10px; text-align: center;">Download</th>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 10px; text-align: center;"><img src="{favicon_url_16}" alt="Favicon 16x16"></td>
            <td style="border: 1px solid black; padding: 10px; text-align: center;">Small: 16x16</td>
            <td style="border: 1px solid black; padding: 10px; text-align: center;"><a href="{favicon_url_16}" download>Download 16x16</a></td>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 10px; text-align: center;"><img src="{favicon_url_64}" alt="Favicon 64x64"></td>
            <td style="border: 1px solid black; padding: 10px; text-align: center;">Medium: 64x64</td>
            <td style="border: 1px solid black; padding: 10px; text-align: center;"><a href="{favicon_url_64}" download>Download 64x64</a></td>
        </tr>
        <tr>
            <td style="border: 1px solid black; padding: 10px; text-align: center;"><img src="{favicon_url_256}" alt="Favicon 256x256"></td>
            <td style="border: 1px solid black; padding: 10px; text-align: center;">Large: 256x256</td>
            <td style="border: 1px solid black; padding: 10px; text-align: center;"><a href="{favicon_url_256}" download>Download 256x256</a></td>
        </tr>
    </table>
    '''