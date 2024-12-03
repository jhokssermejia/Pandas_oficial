import cv2
import numpy as np
#cargamos imagen
image = cv2.imread('shutterstock_335609012.jpg')

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#obtener dimensiones de la imagen
hight, width = image.shape[:2]
center = (width/2, hight/2)
#rotar la imagen
angulo = 45
matrix = cv2.getRotationMatrix2D(center, angulo, 1.0)
rotated = cv2.warpAffine(image, matrix, (width, hight))
cv2.imshow('Image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

tx, ty = 100, 50
M =np.float32([[1, 0, tx], [0, 1, ty]])

#Matriz de traslacion de Imagen
translated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Image', translated)
cv2.waitKey(0)
cv2.destroyAllWindows()


new_height, new_width = 500 , 350

scaled = cv2.resize(image, (new_height, new_width))
#Definir la nueva altura de la imagen
cv2.imshow('Image', scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Recorte
# Definir las coordenadas del área de interés ROI
x, y, w, h = 100, 100, 200, 150
#Recortar la región de interés ROI
cropped = image[y:y+h, x:x+w]
#Mostrar la imagen recortada
cv2.imshow('Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Suavizado
# Aplicar el filtro Gaussiano para suavisar la imagen
smoothed = cv2.GaussianBlur(image, (5, 5), 0)
#Mostrar la imagen suavisada
cv2.imshow('Image', smoothed)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Realce
# Definir el kernel para el filtro de afilado
kernel = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])
#Aplicar el filtro de afilado para realzar los detalles
sharpened = cv2.filter2D(image, -1, kernel)
#Mostrar la imagen realzada
cv2.imshow('Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Detección de bordes
# Cargar la imagen en escala de grises 
image = cv2.imread('shutterstock_335609012.jpg', cv2.IMREAD_GRAYSCALE)
# Aplicar el operador Sobel para detectar los bordes
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
#Combinar las respuestas en magnitud
edges = cv2.magnitude(sobelx, sobely) 
#Normalizar los valores para mostrar la imagen correctamente
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
#Mostrar la imagen con los bordes detectados
cv2.imshow('Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()