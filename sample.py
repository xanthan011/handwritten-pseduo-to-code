
from absl import app, flags
from absl.flags import FLAGS

flags.DEFINE_string('image_path',"./data/demo7.png",'image path')



# import cv2
# import pytesseract

# pytesseract.pytesseract.tesseract_cmd = 'C:\]Program Files\\Tesseract-OCR\\tesseract.exe'
# img = cv2.imread(r"C:\\Users\\Prachi Patel\\ALL PROGRAMS\\PDPU\\AI\\meijieru_crnn_pytorch\\crnn.pytorch\\data\\demo3.png")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow('Result', img)
# cv2.waitKey(0)

from convert import convert_code
from cv2 import cv2
import pytesseract
def main(_argv):

	pytesseract.pytesseract.tesseract_cmd = r'./tesseract/tesseract.exe'
	img = cv2.imread(FLAGS.image_path)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	cv2.imshow('', img)
	cv2.waitKey(0)
	img2char = pytesseract.image_to_string(img)
	print(img2char)
	file1 = open('a.txt', 'w+')
	file1.write((img2char))
	file1.close()
	convert_code()

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
