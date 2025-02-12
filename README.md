# Raspberry Pi Video Streaming

This project implements a simple video streaming server using a Raspberry Pi camera, Flask, and OpenCV. It uses [Picamera2](https://github.com/raspberrypi/picamera2) for capturing video and Flask for serving the video feed with basic authentication.

## Features

- **Live video streaming** from the Raspberry Pi camera.
- **Basic authentication** to secure the video stream.

## Prerequisites

- A Raspberry Pi with a camera module configured.
- Raspberry Pi OS (Bullseye or later is recommended).
- Python 3.x installed.
- [Picamera2](https://github.com/raspberrypi/picamera2) installed (check Raspberry Pi documentation for installation details).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kabhishek3001/raspberrypi-video-stream.git
   cd raspberrypi-video-stream
