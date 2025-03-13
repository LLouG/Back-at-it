import cv2
import os


def transform_drawing(arquivo, qtde_filtro):
    img = cv2.imread(f"images/{arquivo}")
    img_pb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_inverted = cv2.bitwise_not(img_pb)
#    qtde_filtro = 15  # precisa ser numero positivo e impar
    img_blur = cv2.GaussianBlur(img_inverted, (qtde_filtro, qtde_filtro), 0)
    img_blur_inverted = cv2.bitwise_not(img_blur)
    img_finished = cv2.divide(img_pb, img_blur_inverted, scale=256.0)

#    cv2.imshow("Seoul", img_finished)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    cv2.imwrite(f"image_finished/{arquivo}", img_finished)


list_files = os.listdir("images")
for file in list_files:
    transform_drawing(file, 55)
