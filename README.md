# youtube
# YouTube Video Downloader

A simple web application to download YouTube videos using Flask and yt-dlp.

## Features
- Download YouTube videos in the best available quality.
- User-friendly interface for video downloading.
- Backend powered by Flask.
- Cross-Origin Resource Sharing (CORS) enabled for API access.
- Option to serve downloaded files via the web.

## Technologies Used
- **Flask**: For the backend API.
- **yt-dlp**: To handle YouTube video downloads.
- **HTML/CSS/JavaScript**: For the frontend interface.
- **Flask-CORS**: To enable cross-origin requests.

## Requirements
- Python 3.7+
- yt-dlp
- Flask
- Flask-CORS

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   > Ensure you have `yt-dlp` installed. If not, install it using:
   ```bash
   pip install yt-dlp
   ```

3. **Run the Flask Application**:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Enter the YouTube video link in the input box on the frontend.
2. Click the "Download" button.
3. Once the download is complete, a link will appear to download the video file.

## Project Structure
```
.
├── app.py                  # Flask backend code
├── templates
│   └── index.html          # Frontend HTML file
├── static                  # Static assets (if any)
├── downloads               # Directory to store downloaded files
└── README.md               # Project documentation
```

## Notes
- Ensure that the `downloads` directory exists or is created during runtime.
- This application is for educational purposes and adheres to YouTube's Terms of Service.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or bug fixes.

