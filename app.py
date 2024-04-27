import os
from flask import Flask, render_template, redirect, request, url_for, Response

app = Flask(__name__)
DUMMY_FILE_NAME = 'dummy_file'


class Config:
    default_number_of_masks = 1


@app.route('/')
def index():
    return render_template("index.html", number_of_masks=get_number_of_masks(request))


@app.route('/add-mask', methods=['POST'])
def add_mask():
    Config.default_number_of_masks += 1
    return redirect(url_for('index'))


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    number_of_masks = get_number_of_masks_from_form(request)

    for i in range(number_of_masks):
        save_file(request, f'file{i}')

    save_file(request, DUMMY_FILE_NAME)

    prompts = get_prompts(request)
    generate_result_image(prompts)

    return redirect(url_for('result_image'))


@app.route('/result', methods=['GET'])
def result_image():
    return render_template('result.html')


def generate_result_image(prompts):
    # TODO generating image
    return


def save_file(req, request_filename):
    f = req.files[request_filename]
    f.save(request_filename + os.path.splitext(f.filename)[1])


def get_prompts(req):
    return [req.form.get(f'prompt{i}') for i in range(get_number_of_masks_from_form(req))]


def get_number_of_masks(req):
    number_of_masks = req.args.get('number_of_masks', type=int)
    return Config.default_number_of_masks if number_of_masks is None else number_of_masks


def get_number_of_masks_from_form(req):
    return req.form.get('number_of_masks', type=int)


if __name__ == '__main__':
    app.run()
