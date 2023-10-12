from PIL import Image 
# Importa la imagen dependiendo de como se llama
im = Image.open("messi.jpg")

# Imprime el formato, tamaño y modo de la imagen
print(im.format, im.size, im.mode)

# Se utiliza para recortar la imagen dependiendo los pixeles que contenga
box = (0, 0, 900, 700)
region = im.crop(box)
region.save("recorte.jpg") # Crea una imagen, ya recortada

# Se utiliza para invertir los colores de la imagen
r, g, b = region.split()
region = Image.merge("RGB", (b, g, r))
region.save("cambio_rgb.jpg") # Crea na nueva imagen, ya con los colores invertidos

# Se utiliza para rotar la imagen
out = region.rotate(45)
out.save("giro.jpg") # Crea una imagen, ya rotada



