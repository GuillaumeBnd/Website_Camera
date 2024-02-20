import asyncio
from aiohttp import web
import cv2

async def video_feed(request):
    response = web.StreamResponse(
        headers={"Content-Type": "multipart/x-mixed-replace; boundary=frame"}
    )
    await response.prepare(request)

    camera = cv2.VideoCapture(0, cv2.CAP_V4L2)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    try:
        while True:
            ret, frame = camera.read()
            if not ret:
                break

            _, jpeg = cv2.imencode('.jpg', frame)
            await response.write(
                f"--frame\r\nContent-Type: image/jpeg\r\nContent-Length: {len(jpeg)}\r\n\r\n".encode() + jpeg.tobytes() + b"\r\n"
            )

            await asyncio.sleep(0.1)  # Adjust the delay as needed for desired frame rate
    finally:
        camera.release()

    return response

app = web.Application()
app.router.add_route('GET', '/video_feed', video_feed)

if __name__ == '__main__':
    web.run_app(app, port=5000)
