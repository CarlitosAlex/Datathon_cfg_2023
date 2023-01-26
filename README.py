El proyecto propuesto puede verse en su totalidad en el siguiente link: https://github.com/CarlitosAlex/Datathon_cfg_2023.git 

Se nos entregó un dataset en formato parquet con 346.000 registros, correspondientes a avisos de propiedades en venta en Estados Unidos, a los efectos del proyecto, tomaríamos el valor del venta; separaríamos los registros en dos clases, propiedades de valor "alto" y propiedades de valor "bajo".


## Librerias utilizadas
* [Pandas](https://pandas.pydata.org/) y [Numpy](https://numpy.org/) para la exploración, transformación y manipulación de los datos
* [Seaborn](https://seaborn.pydata.org/) y [Matplotlib](https://matplotlib.org/) para las visualizaciones
* [Sklearn](https://scikit-learn.org/stable/) para utilizar sus modelos de Machine Learning, escalado de datos, validación cruzada, división del set en entrenamiento y testeo y métricas para evaluar los modelos


## **Tareas Realizadas**

### EDA (Análisis exploratorio de datos)
Luego de cumplir con la primera consigna que consistía en insertar una nueva columna con el número 1 en las propiedades cuyo valor era inferior o igual a 999 dólares y con el número 0 para el resto, y eliminar la columna "price", revisamos la distribución de ambas clases en el conjunto de datos, y comprobamos que se encontraban balanceadas, por lo que no requerían tratamiento en ese aspecto.

Notamos luego que había en el dataset una gran cantidad de anuncios similares, en los cuales podía llegar a haber alguna variación de precio (que podría deberse a la inflación reinante en Estados Unidos), pero en las que generalmente el resto de los datos, e incluso el texto con la descripción eran exactamente iguales. Confirmó nuestras sospechas el hecho de que la URL que direccionaba hacia la imagen de la propiedad, era siempre la misma.

Utilizando la columna que contenía dicha URL, detectamos 178.233 anuncios repetidos que correspondían a las mismas propiedades, prácticamente la mitad del dataset. Considerando que esta repetición afectaría negativamente nuestros modelos, por el hecho de que ciertas características tendrían mas peso en el análisis solo por el hecho de haberse publicado mas veces esas propiedades, decidimos eliminar esa columna, con una salvedad: Pensamos que podría servirnos el dato referente a cuantas veces apareció publicada cada propiedad (tal vez las propiedades de mayor valor tardan mas tiempo en alquilarse), por lo que generamos una nueva columna conteniendo esa información llamada "publicaciones".

* "long"(lonmgitud, coordenada): Encontramos valores en negativo, detectamos 918 valores nulos, los cuales decidimos reemplazar por el valor ‘unknown’.

