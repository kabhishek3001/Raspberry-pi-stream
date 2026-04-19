# Raspberry Pi Video Streaming

This project implements a simple video streaming server using a Raspberry Pi camera, Flask, and OpenCV. It uses [Picamera2](https://github.com/raspberrypi/picamera2) for capturing video and Flask for serving the video feed with basic authentication.

## Features

- **Live video streaming** from the Raspberry Pi camera.
- **Basic authentication** to secure the video stream.

## Prerequisites

- **Hardware:**  
  - Raspberry Pi 3B+  
  - Arducam 8MP IMX219 camera (ensure it is properly connected and configured)

- **Operating System:**  
  - Bookworm (or Raspberry Pi OS based on Bookworm)

- **Software:**  
  - Python 3.x installed  
  - [Picamera2](https://github.com/raspberrypi/picamera2) installed  
    > **Note:** Installation instructions for Picamera2 and any additional drivers for the Arducam can be found in the official documentation or from the Arducam support pages.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abhiinrobotics/raspberry-pi-stream.git
   cd raspberry-pi-stream
   pip install -r requirements.txt
