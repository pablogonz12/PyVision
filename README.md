# Image Launcher Application

This project is a simple image launcher application that allows users to open images from their computer and apply various filters. The application is built using Python and provides a graphical user interface (GUI) for ease of use.

## Features

- Open images from your local filesystem.
- Apply filters such as blur and grayscale to the images.
- View the modified images in the application.

## Project Structure

```
image_launcher
├── src
│   ├── main.py               # Entry point of the application
│   ├── gui
│   │   ├── main_window.py     # Main application window setup
│   │   └── image_viewer.py    # Image display and update logic
│   ├── filters
│   │   ├── blur.py            # Blur filter implementation
│   │   ├── grayscale.py        # Grayscale filter implementation
│   │   └── __init__.py        # Filters package initialization
│   └── utils
│       └── file_utils.py      # Utility functions for file handling
├── README.md                  # Project documentation
├── requirements.txt           # Project dependencies
└── LICENSE                    # Licensing information
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd image_launcher
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```
2. Use the menu options to open an image and apply filters.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.