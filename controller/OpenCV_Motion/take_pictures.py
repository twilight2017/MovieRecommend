import cv2
def take_pictures():
   cap = cv2.VideoCapture(0)  # 打开摄像头

   while (1):
    # get a frame
      ret, frame = cap.read()
    # show a frame
      cv2.imshow("capture", frame)  # 生成摄像头窗口

      if cv2.waitKey(1) & 0xFF == ord('q'):  # 如果按下q 就截图保存并退出
          cv2.imwrite("F:/1scshixi/OpenCV-Emotion-Recognition-master/OpenCV-Emotion-Recognition-master/take_pic/tp1.jpg", frame)  # 保存路径
          break

   cap.release()
   cv2.destroyAllWindows()
   return