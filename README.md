# Proyecto Big Data

#### EJECUCIÓN

Cuando se requiera ejecutar el programa se debe estar en la carpeta donde se encuentra y se debe poner la siguiente línea,
$ /bin/spark-submit practica04.py /{Carpeta donde se encuentran los documentos}/ {K= k de Kmeans} {Iteraciones del Kmeans}
Ejp: /bin/spark-submit practica4.py /datasets/gutenberg-txt-es/ 10 450


# 1. Realizado por:
1. Dillan Alexis Muñeton Avendaño - dmuneto1@eafit.edu.co
2. Juan Fernando Ossa Vásquez - jossava@eafit.edu.co
3. Daniel Rendon Montaño - drendon9@eafit.edu.co
4. Laura Mejía Vásquez - lmejiav6@eafit.edu.co

# 2. Introducción:

*Aquí se pueden encontrar un archivo .py llamando proyecto04 , el cual contiene el código  de la aplicación, estos sirven para encontrar similitudes entre documentos, utilizando algoritmos de frecuencia y agrupamiento, tales como tfidf y Kmeans respectivamente.
El dataset se obtuvo de Gutenberg por medio del siguiente link, https://goo.gl/LL4CgA, en este dataset se encuentran alrededor de 3000 documentos con los cuales se puede correr este programa.*

# 3. Palabras clave:

Kmeans: es un método de agrupamiento, que tiene como objetivo la partición de un conjunto de n observaciones en k grupos.

TFIDF: frecuencia de término – frecuencia inversa de documento.

Spark: Apache Spark combina un sistema de computación distribuida a través de clusters de ordenadores con una manera sencilla y elegante de escribir programas. Fue creado en la Universidad de Berkeley en California y es considerado el primer software de código abierto que hace la programación distribuida realmente accesible a los científicos de datos.

PySpark: Utilizar spark en el lenguaje de programación python.

# 4. Análisis y Diseño de algoritmos:
El análisis de los algoritmos fue posible gracias a la lectura de documentación sobre pyspark y unos videos recomendados por el orientador de la materia.

Se utilizaron algoritmos tales como:


#### TFIDF: 
Frecuencia de término – frecuencia inversa de documento (o sea, la frecuencia de ocurrencia del término en la colección de documentos), es una medida numérica que expresa cuán relevante es una palabra para un documento en una colección. Esta medida se utiliza a menudo como un factor de ponderación en la recuperación de información y la minería de texto. El valor tf-idf aumenta proporcionalmente al número de veces que una palabra aparece en el documento, pero es compensada por la frecuencia de la palabra en la colección de documentos, lo que permite manejar el hecho de que algunas palabras son generalmente más comunes que otras.


#### KMeans:
K-means es un método de agrupamiento, que tiene como objetivo la partición de un conjunto de n observaciones en k grupos en el que cada observación pertenece al grupo cuyo valor medio es más cercano. Es un método utilizado en minería de datos. El código para el Kmeans se obtuvo de varios links y repositorios de dónde se trató de entender su funcionamiento y gracias a los cuáles se pudo realizar el KMeans que se encuentra en los programas realizados.

#### Esquema de implementación:
En la siguiente figura, las líneas rojas representan transformación y las verdes operación.

![alt text](https://image.ibb.co/gFSRHm/diagrama_BD.png)

# 5. Análisis de solución:

La solución fue pensanda en ambientes de pyspark, en la cúal se utilizó la biblioteca mllib de las cuales se utilizo Kmeans, IDF y HashingTF, que se utilizan para el agrupamiento y hallar las frecuencias de las palabras en los textos. 

Algunos ejemplos fueron tomados de: https://github.com/apache/spark

#### Resultados:
Esto se realizó con datasets de diferentes tamaños, al igual que con distintas k. Los resultados se muestran en la siguiente tabla.
![alt text](https://image.ibb.co/eXHAcm/resultados_B.png)

# 6.Bibliografía:

1. https://es.wikipedia.org/wiki/K-means
2. https://es.wikipedia.org/wiki/Tf-idf
3. https://goo.gl/LL4CgA
4. https://geekytheory.com/apache-spark-que-es-y-como-funciona
5. https://github.com/apache/spark
