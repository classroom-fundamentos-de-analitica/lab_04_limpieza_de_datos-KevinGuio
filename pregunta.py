"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd



def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    df = df.replace("-", " ", regex=True).replace("_", " ", regex=True)

    # QUITAR LOS NAN


    # LIMPIEZA COLUMNA SEXO
    df.sexo = df.sexo.str.lower()

    #LIMPIEZA COLUMNA TIPO_DE_EMPRENDIMIENTO
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    # QUITAR COLUMNA UNNAMED


    # LIMPIEZA COLUMNA idea_negocio
    df.idea_negocio = (df.idea_negocio.str.lower().str.replace("_"," ").
                       str.replace("-"," ").str.strip())

    #LIMPIEZA COLUMNA BARRIO
    df.barrio = df.barrio.str.lower()

    #LIMPIEZA COLUMNA ESTRATO

    #LIMPIEZA COLUMNA comuna_ciudadano

    df.comuna_ciudadano = df.comuna_ciudadano.map(int)

    #LIMPIEZA COLUMNA FECHA DE BENEFICIO

    df.fecha_de_beneficio = (pd.to_datetime(df.fecha_de_beneficio, format="%d/%m/%Y", errors = "coerce").
                             fillna(pd.to_datetime(df.fecha_de_beneficio, format="%Y/%m/%d", errors="coerce")))

    #LIMPIEZA COLUMNA MONTO DEL CRÉDITO

    df.monto_del_credito = (df.monto_del_credito.str.replace("$","").str.strip().str.replace(",","").
                            map(lambda x: float(x.split(".")[0])))

    #LIMPIEZA LÍNEA CRÉDITO
    df.línea_credito = df.línea_credito.str.lower()

    df = df.drop_duplicates().dropna()

    #
    # Inserte su código aquí



    return df

