from PIL import Image
import os
import face_recognition


path = "C://Users//abhishek kushwaha//Desktop//mark attendance//traningData//actualData"
dir_list = os.listdir(path)

for filename in dir_list:



    image = face_recognition.load_image_file(path+"//"+filename)
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

    for face_location in face_locations:

    # Print the location of each face in this image
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save("C://Users//abhishek kushwaha//Desktop//mark attendance//traningData//data"+"//"+filename)

