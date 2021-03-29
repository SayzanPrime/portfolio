import csv

from flask import Flask, render_template, send_from_directory, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static',
                               'ironman.png', mimetype='image/vnd.microsoft.icon')


@app.route('/<string:pagename>')
def page_link_render(pagename):
    return render_template(pagename)


def valid_login(param, param1):
    pass


def log_the_user_in(param):
    pass


@app.route('/contact_submit_form', methods=['POST', 'GET'])
def contact_submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect('/contactsucces.html')
        except TypeError as err:
            return redirect('/contactfailed.html')
    else:
        return 'Something went wrong please try again !'
    # the code below is executed if the request method
    # was GET or the credentials were invalid


def write_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


if __name__ == '__main__':
    app.run()
