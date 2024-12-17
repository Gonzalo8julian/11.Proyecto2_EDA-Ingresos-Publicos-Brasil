import pandas as pd
import numpy as np

def reporte(df):
    """
    Genera un reporte con información sobre los valores nulos y los tipos de variables 
    en un DataFrame de pandas.

    Parámetros:
    df (pd.DataFrame): El DataFrame de pandas que se quiere analizar.

    Devuelve:
    pd.DataFrame: Un nuevo DataFrame con las siguientes columnas:
        - "numero_nulos": Número total de valores nulos por columna.
        - "porcentaje_nulos": Porcentaje de valores nulos respecto al total de filas.
        - "tipo_variables": Tipo de datos de cada columna.

    Ejemplo de uso:
    >>> import pandas as pd
    >>> data = {"col1": [1, 2, None], "col2": ["a", None, "c"]}
    >>> df = pd.DataFrame(data)
    >>> reporte(df)
               numero_nulos  porcentaje_nulos tipo_variables
    col1                 1              33.33        float64
    col2                 1              33.33         object
    """
    df_report = pd.DataFrame()
    df_report["numero_nulos"] = df.isnull().sum()
    df_report["porcentaje_nulos"]= round((df.isnull().sum()/df.shape[0])*100,2)
    df_report["tipo_variables"] = pd.DataFrame(df.dtypes)
    
    return df_report

