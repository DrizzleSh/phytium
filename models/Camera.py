import cv2
import numpy as np
from jpeg_encoder import *
from jpeg_decoder import *
import time

def camera_cut():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 打开摄像头
    p = 0
    while (1):
        img_path = "../data/test" + str(p) + ".bmp"
        write_path = "../data/result" + str(p) + ".jpg"
        # get a frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)  # 摄像头是和人对立的，将图像左右调换回来正常显示
        # show a frame
        cv2.imshow("capture", frame)  # 生成摄像头窗口
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # 如果按下q 就截图保存并退出
            cv2.imwrite(img_path, frame)  # 保存路径
            time_start = time.time()
            Y_byte_stream, Cb_byte_stream, Cr_byte_stream = jpeg_encode(img_path=img_path, write_path=write_path, alpha=1.0)
            time_end = time.time()
            time_gap = time_end - time_start
            print("此次压缩使用的时间为%.3f毫秒"%(time_gap * 1000))
            p += 1
        elif key == ord('a'):
            break

    cap.release()
    cv2.destroyAllWindows()

def pic_browser():
    while(True):
        path = input("请输入图片名称：(输入exit退出)")
        if(path == "exit"):
            break
        path = "../data/" + path
        jpeg_decode(path)

if __name__ == "__main__":
    while(True):
        choice = input("请输入使用的功能：（1.拍摄图片 2.查看图片 3.退出）")
        if choice == '1':
            camera_cut()
        elif choice == '2':
            pic_browser()
        elif choice == '3':
            break