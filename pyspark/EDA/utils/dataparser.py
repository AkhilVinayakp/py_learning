# various data transformation and parsing functions
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyspark.sql import SparkSession, DataFrame


def parse_continuous_fields(df: DataFrame, distinct_count: int) -> list:
    """Generate the list of all continuous fields in a given dataframe
    :param df: input Dataframe
    :param distinct_count: Minimum number of distinct values required to consider as a continuous field.
    :return: List of columns name.
    """
    numeric_cols = []
    columns: list = df.schema.fields
    for col in columns:
        if col.dataType.simpleString() in ['int', 'double']:
            d_count = df.select(col.name).distinct().count()
            if d_count >= distinct_count:
                numeric_cols.append(col.name)
    return numeric_cols


if __name__ == "__main__":
    # pass
    from initializer import init_spark_objs
    from data_loader import file_loader

    spark, sc = init_spark_objs(appname="OLD")
    df = file_loader(spark, path="../../Data/Iris.csv")
    df.show(5, truncate=False)
    print(parse_continuous_fields(df, distinct_count=20))
