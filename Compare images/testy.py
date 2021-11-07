import face_recognition
#  مقایسه دو چهره
shajarian_img = face_recognition.load_image_file('./Compare images/known/image.jpg')
shajarian_encoding = face_recognition.face_encodings(shajarian_img)[0]

unknown_img = face_recognition.load_image_file('./Compare images/unknown/image2.jpg')
unknown_encoding = face_recognition.face_encodings(unknown_img)[0]

unknown_img1 = face_recognition.load_image_file('./Compare images/unknown/unnamed.jpg')
unknown_encoding1 = face_recognition.face_encodings(unknown_img1)[0]

result = face_recognition.compare_faces([shajarian_encoding],unknown_encoding)
result1 = face_recognition.compare_faces([shajarian_encoding],unknown_encoding1)
print(result,result1)

