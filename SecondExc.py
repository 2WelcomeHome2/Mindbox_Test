
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

# Создание SparkSession
spark = SparkSession.builder.getOrCreate()

# Создание датафрейма product_df
product_data = [('product1',),
               ('product2',),
               ('product3',),
               ('product4',),
               ('product5',)]
product_schema = ['product_name']
product_df = spark.createDataFrame(product_data, product_schema)

# Создание датафрейма category_df
category_data = [('category1',),
                 ('category2',),
                 ('category3',)]
category_schema = ['category_name']
category_df = spark.createDataFrame(category_data, category_schema)

# Добавление колонки 'product_name' в category_df (Необязательно, но позволит создать продукты без категорий)
category_df = category_df.withColumn('product_name', lit(None))

# Проверка создания датафреймов
print("product_df:")
product_df.show()
print("category_df:")
category_df.show()


result_df = product_df.join(category_df, product_df.product_name == category_df.product_name, "left_outer")
result_df = result_df.select(product_df.product_name, category_df.category_name)
result_df.show()
