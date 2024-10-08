from flask import Flask, render_template, request, send_file, jsonify
import cairosvg
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    svg_code = request.form['svg_code']
    output = io.BytesIO()

    # Convert SVG to PNG and save to the BytesIO object
    try:
        cairosvg.svg2png(bytestring=svg_code.encode('utf-8'), write_to=output)
        output.seek(0)

        # Convert the PNG to base64 for preview in the frontend
        encoded_img = base64.b64encode(output.getvalue()).decode('utf-8')
        img_data = f"data:image/png;base64,{encoded_img}"

        return jsonify({'image': img_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/download', methods=['POST'])
def download():
    svg_code = request.form['svg_code']
    output = io.BytesIO()

    # Convert SVG to PNG and save to the BytesIO object
    try:
        cairosvg.svg2png(bytestring=svg_code.encode('utf-8'), write_to=output)
        output.seek(0)

        # Return the PNG image for download
        return send_file(output, mimetype='image/png', as_attachment=True, download_name='output.png')
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
