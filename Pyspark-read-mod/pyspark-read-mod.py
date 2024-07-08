from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Read PostgreSQL Data into PySpark") \
    .config("spark.driver.extraClassPath", "/path/to/postgresql-jdbc-driver.jar") \
    .getOrCreate()

# PostgreSQL connection parameters
postgres_url = "jdbc:postgresql://ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb"
table_name = "Bank-full-s"
properties = {
    "user": "consultants",
    "password": "WelcomeItc@2022",
    "driver": "org.postgresql.Driver"

}

# Read data from PostgreSQL into PySpark DataFrame
df = spark.read.jdbc(url=postgres_url, table=table_name, properties=properties)

# Show DataFrame schema and preview data
df.printSchema()
df.show()

# Stop Spark session
spark.stop()