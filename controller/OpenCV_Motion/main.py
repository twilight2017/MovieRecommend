# from prepare_training_data import prepare_training_data
import cv2
from .take_pictures import take_pictures
from .face_api_rec import face_rec_start
if __name__ == '__main__':
    # print("Preparing data...")
    # #调用之前写的函数，得到包含多个人脸矩阵的序列和它们对于的标签
    # faces, labels = prepare_training_data()
    # print("Data prepared")
    #
    # print("Total faces: ", len(faces))
    # print("Total labels: ", len(labels))
    #
    # #得到（LBPH）人脸识别器
    # face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    # #应用数据，进行训练
    # face_recognizer.train(faces, np.array(labels))
    # print("Predicting images...")
    # take_pictures()
    # 加载预测图像，这里我图简单，就直接把路径写上去了
    # test_img1 = cv2.imread(r"./take_pic/tp1.jpg",0)
    # test_img2 = cv2.imread(r"./img_predict/sad1.jpg",0)
    # face_rec_start()
    # 进行预测
    # predicted_img1_label1 = predict(test_img1, facerecg_train())
    # predicted_img2_label2 = predict(test_img2, facerecg_train())
    # print("Prediction complete", predicted_img1_label1)
    # print(predicted_img1_label1,predicted_img2_label2)
    # 显示预测结果
    # cv2.imshow(predicted_img1_label1,test_img1)
    # if predicted_img1_label1 == 'Happy':
    #   recommend('Godfather')
    # if predicted_img1_label1 == 'Sad':
    #   recommend('Toy Story 3')
    # if predicted_img1_label1 == 'Calm':
    #   recommend('Superman Returns')
    # cv2.imshow(predicted_img2_label2,test_img2)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # if predicted_img1_label1 == 'happy':
    # recommend('Godfather')
    take_pictures()
    # 加载预测图像
    test_img1 = cv2.imread(r"./take_pic/tp1.jpg",0)
    # test_img2 = cv2.imread(r"./img_predict/sad1.jpg",0)
    face_rec_start()
    # if json1=="sad":
    #     recommend('1')

