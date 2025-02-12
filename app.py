from flask import Flask, Response
from picamera2 import Picamera2
import cv2
import time
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'pi'
app.config['BASIC_AUTH_PASSWORD'] = 'pi'
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)
last_epoch = 0

picam2 = Picamera2()
config = picam2.create_video_configuration(
    main={"format": "RGB888", "size": (640, 480)}
)
picam2.configure(config)
picam2.start()


def generate_frames():
    while True:
        # Capture a frame as a NumPy array
        frame = picam2.capture_array()

        if frame is not None:
            # Convert BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Encode frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            # Yield frame as part of HTTP response
            yield (
                b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
            )
        else:
            print("No frame available!")
        time.sleep(0.1)  # Simulate a frame rate


@app.route('/video_feed')
def video_feed():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
