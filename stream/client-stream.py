import cv2
import socket
import pickle
import zlib



client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cam = cv2.VideoCapture(0)
# cam.set(3, 320)
# cam.set(4, 240)
img_counter = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)
    client_socket.sendto(data, (UDP_IP, UDP_PORT))
    img_counter += 1
