# Análisis de la Ejecución de Ingresos Públicos en Brasil

## 📖 Descripción

En este proyecto analizamos los datos históricos de la ejecución de ingresos entre 2013 y 2021 del gobierno de Brasil.

Para ello hemos realizado una limpieza de datos y un análisis exhaustivo para poder trabajar con todos los datos de todos los años a estudiar.

Los principales problemas a resolver son: 
1.	**Desviaciones entre lo previsto y lo recaudado**: Determinar en qué categorías económicas o tipos de ingresos las diferencias son más pronunciadas.

2.	**Evolución temporal de la recaudación**: Identificar cómo han cambiado las previsiones y recaudaciones año a año, y si existen patrones temporales, como meses específicos donde hay mayores discrepancias.

3.	**Rendimiento por órgano y unidad gestora**: Evaluar qué órganos o unidades gestoras son más eficientes en términos de alcanzar las metas de recaudación y cuáles presentan consistentemente una baja ejecución.

Aunque carecemos de información para poder sacar conclusiones 100% fiables, hemos podido sacar información muy valiosa para poder analizar e intentar optimizar de cara al futuro.

## 🗂️ Estructura del Proyecto

├── Data/                      # Enlace a google Drive con todos los datos en csv: https://drive.google.com/drive/folders/1na4t8B6wNNNnVZuuJK9elX4NOwziGcli?usp=sharing

├──1PROYECTO2_limpiezadatos/                       # archivo ipynb donde se han limpiado los datos de las bases de datos de cada año por separado.

├──2.PROYECTO2_union                      # Archico ipynb con la unión de todos los años en un único dataframe.

├──3.PROYECTO2_EDA y visualizacion                      # Archivo ipynb con el análisis EDA y visualización de gráficos del estudio realizado.

## 🛠️ Instalación y Requisitos
Este proyecto usa Python 3.9.6 y se han utilizado las siguientes librerías: 
- Pandas
- Numpy
- Matplotlib
- Seaborn

## 📊 Resultados y Conclusiones

> Resumen de hallazgos:

Las categorías con mayor discrepancia entre lo previsto y lo realizado son: Receitas de capital y Receitas corriendes, donde podemos ver que hay una mayor cantidad de ingresos frente al resto de categorías y donde, además, vemos que la diferencia entre los ingresos previstos y realizados es de 640183814296.71 y 2078616751140.80 respectivamente. Lo cuál quiere decir que hay mucho dinero que se preveía ingresar por parte del gobierno y, o bien no se ha ingresado por algún motivo, o bien no se ha demostrado.

En cuanto a los periodos temporales, podemos decir que, excepto el año 2020, que se superó el total de ingresos frente a lo previsto, el resto de años hay una gran diferencia entre lo previsto y lo recaudado. Destacando sobre todo los años 2017 y 2018 que es donde más diferencia hay entre unos ingresos y otros. 

Como hemos comentado anteriormente, estas consecuencias pueden venir dadas por numerosas causas, como pueden ser, alguna crisis económica en el país, alguna catástrofe que haya afectado al pais o, incluso, motivos de fraude fiscal, donde los integrantes del gobierno de Brasil se hayan quedado con ese dinero que, supuestamente, se preveía recibir.

También puede darse por un error a la hora de hacer las previsiones, ya que es un error bastante grande y no se ha conseguido lo previsto en prácticamente ningún año del estudio. Es cierto que no es fácil acertar al 100% pero seguramente la diferencia podría ser menor de lo que realmente es.

## 🔄 Próximos Pasos

En primer lugar, una propuesta de mejora de cara al futuro es intentar controlar las fechas en las que se realizan los ingresos, ya que, como hemos comentado en el análisis temporal, no podemos sacar muchas conclusiones por meses, ya que las fechas que aparecen se concenctran todas en un día y mes del año. Sería bueno, intentar tener información lo más real posible para poder analizar la situación de los ingresos a lo largo de los meses de cada año y así poder sacar conclusiones más fiables. 

Por otro lado, habría que hacer un gran hincapié en la manera de calcular los ingresos previstos ya que, en el caso de no ser un fraude fiscal, está claro que se lleva haciendo mal muchos años y es algo bastante importante para el gobierno del país.

## ✒️ Autor
- **Gonzalo Julián** - [@gonzalo8julian](https://github.com/Gonzalo8julian)


