# FFMPEG-Video-Processing
A python script to create an image template that is overlaid on a Video with an input title. The title is then converted into Google Speech and then added to video with a waveform effect. 

## Overview

This project focuses on converting text into a narrated video with image overlays. It utilizes various Python libraries and the FFmpeg tool to achieve this. The main functionalities include:

1. **Splitting Text into Lines (`split_text_into_lines`):** This function takes a long text input and divides it into lines of a specified maximum length. It's useful for ensuring text fits well within video frames.

2. **Creating an Image with Text (`create_image_with_text`):** Given an image and text, this function overlays the text on the image. It allows you to specify font, font size, text color, position, and more.

3. **Text-to-Speech Conversion (`convert_text_to_speech`):** This function converts text into speech using the Google Text-to-Speech (gTTS) library and saves it as an audio file.

4. **Creating a Video with Overlay (`create_video_with_overlay`):** This function combines an input video, image with text overlay, and audio narration to produce a final video. It includes features like overlay duration and zoom effects.

## Prerequisites

Before using these functions, ensure you have the following prerequisites:

- Python installed on your system.
- FFmpeg tool installed and added to your system's PATH.
- Necessary Python libraries installed (gTTS, subprocess).

## Usage

Each script can be executed individually based on your data processing needs. Ensure that you have the necessary AWS and Redshift credentials and permissions to run these scripts successfully.

## Contributing

If you find issues or have improvements to suggest, feel free to open an issue or submit a pull request to this repository.
