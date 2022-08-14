# Importamos todo lo necesario
# -*- coding: utf-8 -*-
import os
from os import remove
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import requests
from bs4 import BeautifulSoup as bs
from io import open
import numpy as np
import pandas as pd

# instancia del objeto Flask
app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './Archivos'

@app.route("/")
def upload_file():
 # renderiamos la plantilla "formulario.html"
 return render_template('HTML_link.html')

@app.route("/upload", methods=['POST'])
def uploader():
 if request.method == 'POST':
  #Borra el archivo Links.txt
  remove("./Archivos/Whatlinks.txt")      
  # obtenemos el archivo del input "archivo"
  fa = request.files['archivo']
  filename = secure_filename(fa.filename)
  # Guardamos el archivo en el directorio "Archivos PDF"
  fa.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  #RENOMBRA EL ARCHIVO
  os.rename('./Archivos/'+str(filename), './Archivos/Whatlinks.txt')
  # Retornamos una respuesta satisfactoria
  resul12 = resuelvelo()
  return render_template('Result_for_Textbox.html', SName =   ' , '.join(resul12)) 
  #return "<h1>Archivo subido exitosamente</h1>"
  # SName =   '  '.join(resul12))    

def resuelvelo():
     df = pd.read_csv('./Archivos/Whatlinks.txt')
     lola= np.asarray(df)
     #chat= list()
     linder=list()
     #image1=list()
     archivo = open('./Whatgrupos.txt', 'w' , encoding='UTF8')

     for s in lola:
          listToStr = ' '.join([str(elem) for elem in s]) 
          #print(listToStr)
          r = requests.get(listToStr)
          soup = bs(r.content, 'html.parser')

          # Locate the box that contains title and transcript
          box = soup.find('div', class_='_9vd6 _9t33 _9bir _9bj3 _9bhj _9v12 _9tau _9tay _9u6w _9se- _9u5y')
          # Locate title and transcript
          first_header = box.find('h3').get_text( )
     
          if len(first_header) != 0:
           #linder.append(listToStr.strip(' '))          
           linder.append(listToStr)
           archivo.write(first_header +'\n')
           archivo.write(listToStr +'\n')
  
     archivo.close()
     return linder
    
if __name__ == '__main__':
 # Iniciamos la aplicación
 app.run(debug=True)