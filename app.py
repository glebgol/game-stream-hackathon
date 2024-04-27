from distutils.log import debug
from fileinput import filename
from flask import *

app = Flask(__name__)


@app.route('/')
def main():
    number_of_masks = request.args.get('number_of_masks', type=int)
    return render_template("index.html", number_of_masks=3 if number_of_masks is None else number_of_masks)


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        number_of_masks = request.args.get('number_of_masks', type=int)

        for i in range(number_of_masks):
            f = request.files[f'file{i}']
            f.save(f.filename)

        dummy_file = request.files['dummy_file']
        dummy_file.save(dummy_file.filename)

        return render_template("Acknowledgement.html", name=f.filename)


if __name__ == '__main__':
    app.run()
