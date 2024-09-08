# Video Metadata Extraction Tool

This tool extracts metadata from video files in various formats, such as MP4, MOV, AVI, WMV, and MKV. The metadata can be saved as text files and displayed within the app.

## Features

- **Single Video File Processing**: Extract metadata from a single video file.
- **Supports Multiple Video Formats**: Compatible with MP4, MOV, AVI, WMV, and MKV.
- **Display Metadata**: View the metadata in a scrollable window.
- **Save Metadata**: Export metadata to a .txt file.

## Requirements

- Python 3.x
- Tkinter: For GUI components.
- pymediainfo: For metadata extraction.
- MediaInfo CLI Tool: Download from MediaInfo.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/matsunosan/video-metadata-extraction-tool.git
    cd video-metadata-extraction-tool
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure MediaInfo CLI tool is installed and added to your system’s PATH.

## Usage

1. Open the GUI by running:

    ```bash
    python main.py
    ```

2. Select a video file using the "Open Video File" button.

3. View the extracted metadata in the window.

4. Optionally, save the metadata to a text file.

## Supported Formats

- MP4
- MOV
- AVI
- WMV
- MKV

## Authors

- Nazar
- Danylo
- Vilnius University Šiauliai Academy

