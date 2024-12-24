from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import yt_dlp as y
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Directory to store downloads
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    link = data.get('link')

    if not link:
        return jsonify({'error': 'No link provided'}), 400

    try:
        # yt-dlp options
        ydl_opts = {
            'format': 'best/bestvideo+bestaudio',  # Try best available video/audio combo
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')  # Save to downloads directory
        }

        with y.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)  # Download video
            filename = ydl.prepare_filename(info)  # Get the file name

        return jsonify({'message': 'Video downloaded successfully!', 'filename': filename})
    except Exception as e:
        return jsonify({'error': f'Failed to download video: {str(e)}'}), 500

@app.route('/downloads/<path:filename>', methods=['GET'])
def serve_file(filename):
    # Serve the downloaded file
    return send_from_directory(DOWNLOAD_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
