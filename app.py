from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
DEFAULT_NUMBER_OF_MASKS = 3
DUMMY_FILE_NAME = 'dummy_file'


@app.route('/')
def index():
    return render_template("index.html", number_of_masks=get_number_of_masks(request))


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    number_of_masks = get_number_of_masks_from_form(request)

    for i in range(number_of_masks):
        save_file(request, f'file{i}')

    save_file(request, DUMMY_FILE_NAME)
    generate_result_image(number_of_masks)

    return redirect(url_for('result'))


@app.route('/result', methods=['GET'])
def result_image():
    return render_template('result.html')


def generate_result_image(number_of_masks):
    # TODO generating image
    return


def save_file(req, request_filename):
    f = req.files[request_filename]
    f.save(f.filename)


def get_number_of_masks(req):
    number_of_masks = req.args.get('number_of_masks', type=int)
    return DEFAULT_NUMBER_OF_MASKS if number_of_masks is None else number_of_masks


def get_number_of_masks_from_form(req):
    return req.form.get('number_of_masks', type=int)


if __name__ == '__main__':
    app.run()
