"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as archivo:
        lines = archivo.readlines()

    columnas = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]

    datos = []
    actual = None
    contador_cluster = 1

    for line in lines[4:]:
        if line.strip():
            if line[:4].strip().isdigit():
                if actual:
                    datos.append(actual)
                cluster = contador_cluster
                contador_cluster += 1
                cantidad = int(line[5:18].strip())
                porcentaje = float(line[19:33].strip().replace(",", ".").replace("%", ""))
                palabras_clave = line[34:].strip()
                actual = [cluster, cantidad, porcentaje, palabras_clave]
            else:
                if actual:
                    actual[-1] += " " + line.strip()
    if actual:
        datos.append(actual)
    df = pd.DataFrame(datos, columns=columnas)
    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace("\s+", " ", regex=True)
        .str.replace(", ", ",")
        .str.replace(",", ", ")
        .str.strip()
        .str.rstrip(".")
    )
    return df