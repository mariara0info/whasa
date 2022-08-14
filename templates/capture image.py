img = requests.get('https://'+urlImagen, hearders={"User-Agent" : "Chrome/50.0.2661.94"})

NombreImagen = varia + '.jpg'
with open(NombreImagen, 'wb') as imagen:
    imagen.write(img.content)
