"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd



def limpieza_columna_sexo(df):
    df = df.copy()
    df.sexo = (df.sexo
               .str.lower()
               .str.replace("femenino", "f")
               .str.replace("masculino", "m"))
    
    return df

def limpieza_columna_tipo_de_emprendimiento(df):
    df = df.copy()
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()
    
    return df

def limpieza_columna_idea_negocio(df):
    df = df.copy()
    df.idea_negocio = (df.idea_negocio
                       .str.lower()
                       .str.replace('_', ' ')
                       .str.replace('-', ' ')
                       .str.replace('.', ''))
    return df

def limpieza_columna_barrio(df):
    df = df.copy()
    df.barrio = (df.barrio
                 .str.lower()
                 .str.replace('_', ' ')
                 .str.replace('-', ' '))
    return df

def limpieza_columna_estrato(df):
    df = df.copy()
    df.estrato = df.estrato.map(int)
    return df

def limpieza_columna_comuna_ciudadano(df):
    df = df.copy()
    df.comuna_ciudadano = df.comuna_ciudadano.map(int)
    return df

def limpieza_columna_fecha_de_beneficio(df):
    df = df.copy()
    df.fecha_de_beneficio = (pd.to_datetime(df.fecha_de_beneficio, format="%d/%m/%Y", errors = "coerce")
                             .fillna(pd.to_datetime(df.fecha_de_beneficio, format="%Y/%m/%d", errors="coerce")))
    return df

def limpieza_columna_monto_del_credito(df):
    df = df.copy()
    df.monto_del_credito = (df.monto_del_credito
                            .str.replace("$", "")
                            .str.strip()
                            .str.replace(",", "")
                            .map(lambda x: int(x.split(".")[0])))
    return df

def limpieza_columna_línea_credito(df):
    df = df.copy()
    df.línea_credito = (df.línea_credito
                        .str.lower()
                        .str.replace('_', ' ')
                        .str.replace('-', ' ')
                        .str.replace('.', ''))
    return df



def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    df_limpio = df.copy()

    
    df_limpio = limpieza_columna_sexo(df_limpio)
    df_limpio = limpieza_columna_tipo_de_emprendimiento(df_limpio)
    df_limpio = limpieza_columna_idea_negocio(df_limpio)
    df_limpio = limpieza_columna_barrio(df_limpio)
    df_limpio = limpieza_columna_estrato(df_limpio)
    df_limpio = limpieza_columna_comuna_ciudadano(df_limpio)
    df_limpio = limpieza_columna_fecha_de_beneficio(df_limpio)
    df_limpio = limpieza_columna_monto_del_credito(df_limpio)
    df_limpio = limpieza_columna_línea_credito(df_limpio)

    # Eliminar duplicados
    df_limpio = df_limpio.drop_duplicates()

    # Eliminar filas con datos faltantes
    df_limpio = df_limpio.dropna()

    return(df_limpio)

#print(clean_data())
