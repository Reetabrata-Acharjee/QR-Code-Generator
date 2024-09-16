# QR Code Generator Flask App
 # Overview
This is a simple Flask web application that generates QR codes based on user input. The application takes a URL as input, creates a QR code, and displays it on the webpage.

# Features
* Generates QR codes based on user input URL
* Displays the generated QR code on the webpage
* Uses the qrcode library to create QR codes
* Uses the Pillow library to handle image processing
* Uses base64 encoding to display the QR code on the webpage
# Requirements
* Python 3.x
* Flask
* qrcode
* Pillow
* base64
# Usage
* Run the application: python app.py
*  * Open a web browser and navigate to http://localhost:5000
* Enter a URL in the input field and submit the form
* The generated QR code will be displayed on the webpage
# Code Structure
* app.py: The main application file that defines the Flask routes and handles user input
* templates/index.html: The HTML template for the main page
* templates/qr_code.html: The HTML template for displaying the generated QR code
* static/: Directory for static files (e.g., CSS, JavaScript)
 
# Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

# Acknowledgments
* This project uses the qrcode library to generate QR codes.
* This project uses the Pillow library to handle image processing.
