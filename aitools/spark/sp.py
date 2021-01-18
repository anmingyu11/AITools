def rename_columns(df, columns):
    if not isinstance(columns, dict):
        raise ValueError("'columns' should be a dict, like {'old_name_1':'new_name_1', 'old_name_2':'new_name_2'}")

    for old_name, new_name in columns.items():
        df = df.withColumnRenamed(old_name, new_name)

    return df


def word_count(rdd):
    return rdd.map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)


def get_partitions(sql, table_name):
    partitions = sql('show partitions {}'.format(table_name)).collect()
    partitions = [pt['partition'] for pt in partitions]
    partitions = [pt.split('=')[1] for pt in partitions]
    return partitions


def get_partitions2(tb):
    partitions = f.sql('show partitions {}'.format(tb)).collect()
    partitions = [pt['partition'] for pt in partitions]
    partitions = [pt.split('=')[1] for pt in partitions]
    partitions = sorted(partitions)
    partitions.reverse()
    return partitions


def show_null(df):
    df.select(*(functions.sum(functions.col(c).isNull().cast("int")).alias(c) for c in df.columns)).show()

def table_exists(tb):
    return f.sql("SHOW TABLES LIKE '{}'".format(tb)).count() == 1

def split_vector(df,vec_col_name):
    df\
        .withColumn("vecs", vector_to_array(vec_col_name))\
        .select(["word"] + [col("vecs")[i] for i in range(3)])