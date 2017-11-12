from pyspark import SparkContext
from math import sqrt
from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.clustering import KMeans
import sys

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("USAGE: python proyecto04.py <pathFiles> <k> <maxIterations>")
        sys.exit(1)
    ruta = sys.argv[1]
    k = int(sys.argv[2])
    maxIt = int(sys.argv[3])
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
    idf = IDF().fit(tf)
    #Calcula el valor final al multiplicar tf e idf
    tfidf = idf.transform(tf)
    #Se ejecuta KMeans y se obtiene el modelo
    clusters = KMeans.train(tfidf, k, maxIterations=maxIt)
    #Se obtiene la lista de las agrupaciones resultantes
    clusterid = clusters.predict(tfidf).collect()
    #Se crea un diccionario que tiene como clave el nombre del documento
    # y como valor el cluster al que pertenece
    dictionary = dict(zip(nombreArchivos, clusterid))

    #Se calcula el error del clustering con el algoritmo Within Set Sum of Squared Errors
    #Se utiliza para calcular el K optimo
    def error(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x**2 for x in (point - center)]))
    WSSSE = tfidf.map(lambda point: error(point)).reduce(lambda x, y: x + y)

    #Almaceno en un archivo los resultados
    file = open("resultadoP4.txt","w")
    file.write("Clusters: \n")
    file.write(str(dictionary))
    file.write("\nTotal Cost: \n" +str(clusters.computeCost(tfidf))+'\n')
    file.write("Within Set Sum of Squared Error = " + str(WSSSE)+'\n')

    #Se cierra el Spark Context
    sc.stop()