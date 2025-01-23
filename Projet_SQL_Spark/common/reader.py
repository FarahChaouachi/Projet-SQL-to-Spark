# Ce fichier contient les fonctions commun pour la lecture des fichiers à utiliser 

from context.context import get_spark_session
from data.schema import schema_data


def read_from_csv(csv_file_path: str, header: bool = True, delimiter: str = ","):
    
    spark = get_spark_session()
    return spark.read.csv(csv_file_path, header=header, sep=delimiter, inferSchema=True,schema=schema_data)