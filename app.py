from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dummy data for recommendations
RECOMMENDATIONS = {
    "default": {
        "hotels": ["Hotel A", "Hotel B", "Hotel C"],
        "destinations": ["Beach X", "Park Y", "Museum Z"],
        "gallery": [
            "https://via.placeholder.com/150",
            "https://via.placeholder.com/150",
            "https://via.placeholder.com/150"
        ],
        "map_url": "https://www.google.com/maps"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(request.url)

    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        result = RECOMMENDATIONS["default"]

        return render_template(
            'result.html',
            filename=filename,
            hotels=result['hotels'],
            destinations=result['destinations'],
            gallery=result['gallery'],
            map_url=result['map_url']
        )

    return redirect('/')

@app.route('/gallery')
def gallery():
    image_files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=image_files)

if __name__ == '__main__':
    app.run(debug=True)
