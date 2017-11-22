from pyspark import SparkContext
from math import sqrt
from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.clustering import KMeans
from pyspark.ml.feature import StopWordsRemover
import sys

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("USAGE: python proyecto04.py <filesPath> <outputPath> <k> <maxIterations>")
        sys.exit(1)
    ruta = sys.argv[1]
    rutaOut = sys.argv[2]
    k = int(sys.argv[3])
    maxIt = int(sys.argv[4])
    #Spark Context
    sc = SparkContext(appName="Practica4")
    #Leer archivos de la ruta especificada
    archivos = sc.wholeTextFiles(ruta)
    #Extraer la lista de los nombres de los archivos del RDD
    nombreArchivos = archivos.keys().collect()
    #Separar los archivos por palabras
    documentos = archivos.values().map(lambda documento: documento.split(" "))
    #Se intancia un objeto HashingTF para hacer un TF
    hashingTF = HashingTF()
    #Calcula la frecuencia de los terminos en los documentos
    tf = hashingTF.transform(documentos)
    #Calcula la importancia de los terminos en el cluster
    idf = IDF(minDocFreq=10).fit(tf)
    #Calcula el valor final al multiplicar tf e idf
    tfidf = idf.transform(tf)
    #Se ejecuta KMeans y se obtiene el modelo
    clusters = KMeans.train(tfidf, k, maxIterations=maxIt)
    #Se obtiene la lista de las agrupaciones resultantes
    clusterid = clusters.predict(tfidf).collect()
    #Se crea un diccionario que tiene como clave el nombre del documento
    # y como valor el cluster al que pertenece
    dictionary = dict(zip(nombreArchivos, clusterid))

    #Guardar en el archivo la salida
    d = sc.parallelize(dictionary.items())
    #Almacena en un solo archivo
    d.coalesce(1).saveAsTextFile(rutaOut)
    #Cada RDD almacena en un archivo
    #d.saveAsTextFile(rutaOut)

    #Se cierra el Spark Context
    sc.stop()
