def rename_columns(df, columns):
    if not isinstance(columns, dict):
        raise ValueError("'columns' should be a dict, like {'old_name_1':'new_name_1', 'old_name_2':'new_name_2'}")

    for old_name, new_name in columns.items():
        df = df.withColumnRenamed(old_name, new_name)

    return df


def word_count(rdd):
    return rdd.map(lambda x : (x,1)).reduceByKey(lambda a, b : a + b)