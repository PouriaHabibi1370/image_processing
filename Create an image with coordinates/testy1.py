#    ایجاد تصویر و ذخیره کردن با استفاده از مختصات 
import face_recognition
from numpy import imag
import uuid # ایجاد ای دی مختص هر تصویر برای ذخیر


img = face_recognition.load_image_file('image.jpg')

image_location = face_recognition.face_locations(img)

#print(image_location)


from PIL import Image

for face_location in image_location:

    top,right,bottom,left = face_location

    face_img = img[top:bottom,left:right]

    pil_img = Image.fromarray(face_img)
    pil_img.show()

    pil_img.save('%s.jpg'%(uuid.uuid1()))
