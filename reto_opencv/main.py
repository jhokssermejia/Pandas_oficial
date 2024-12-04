import cv2
import numpy as np

# Ejercicio 1: Cargar y mostrar imágenes
# Cargar imagen en color y en escala de grises
color_image = cv2.imread('black_car.jpg')
gray_image = cv2.imread('red_car.jpg', cv2.IMREAD_GRAYSCALE)

# Mostrar ambas imágenes en ventanas separadas
cv2.imshow('Imagen en Color', color_image)
cv2.imshow('Imagen en Escala de Grises', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ejercicio 2: Rotar y escalar imagen
# Rotar la imagen 90 grados en sentido horario
(h, w) = color_image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated_image = cv2.warpAffine(color_image, rotation_matrix, (w, h))

# Escalar la imagen al doble de su tamaño original
scaled_image = cv2.resize(color_image, (0, 0), fx=2, fy=2)

# Mostrar imágenes resultantes
cv2.imshow('Imagen Rotada', rotated_image)
cv2.imshow('Imagen Escalada', scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ejercicio 3: Filtrado
# Cargar imagen en escala de grises
gray_image_2 = cv2.imread('red_car.jpg')

# Aplicar filtro Gaussiano
blurred_image = cv2.GaussianBlur(gray_image_2, (5, 5), 0)

# Aplicar filtro de realce
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])
sharpened_image = cv2.filter2D(gray_image_2, -1, kernel)

# Mostrar imágenes resultantes
cv2.imshow('Imagen Suavizada', blurred_image)
cv2.imshow('Imagen Realzada', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Ejercicio 4: Detección de bordes
# Cargar la imagen en escala de grises 
image = cv2.imread('red_car.jpg', cv2.IMREAD_GRAYSCALE)
# Aplicar el operador Sobel para detectar los bordes
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
#Combinar las respuestas en magnitud
edges = cv2.magnitude(sobelx, sobely) 
#Normalizar los valores para mostrar la imagen correctamente
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
#Mostrar la imagen con los bordes detectados
cv2.imshow('Imagen con deteccion de bordes: ', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()