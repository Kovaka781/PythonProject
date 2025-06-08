import cv2
from PIL import Image

image_path = 'cot2.jpeg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)
cat = Image.open(image_path)
glasses = Image.open('1112.png')
glasses2 = Image.open('glasses.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
for (x, y, w, h) in cat_face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
    glasses = glasses.resize((w, int(h / 2)))
    cat.paste(glasses, (x + 1, y - 30), glasses)
    glasses2 = glasses2.resize((w, int(h / 3)))
    cat.paste(glasses2, (x + 5, int(y + h / 3)), glasses2)
    cat.save("cat_with_glasses.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("Cat_with_glasses", cat_with_glasses)
    cv2.waitKey()
cv2.imshow("Cat", image)
cv2.waitKey()
