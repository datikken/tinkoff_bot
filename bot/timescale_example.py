import psycopg2

CONNECTION = "postgres://postgres:password@127.0.0.1:5432/postgres"

conn = psycopg2.connect(CONNECTION)

# query_create_sensors_table = """CREATE TABLE sensors (
#                                     id SERIAL PRIMARY KEY,
#                                     type VARCHAR(50),
#                                     location VARCHAR(50)
#                                 );
#                                 """
# # create sensor data hypertable
# query_create_sensordata_table = """CREATE TABLE sensor_data (
#                                         time TIMESTAMPTZ NOT NULL,
#                                         sensor_id INTEGER,
#                                         temperature DOUBLE PRECISION,
#                                         cpu DOUBLE PRECISION,
#                                         FOREIGN KEY (sensor_id) REFERENCES sensors (id)
#                                     );
#                                     """

# query_create_sensordata_hypertable = "SELECT create_hypertable('sensor_data', 'time');"

# cursor = conn.cursor()
# cursor.execute(query_create_sensordata_table)
# cursor.execute(query_create_sensordata_hypertable)

# # commit changes to the database to make changes persistent
# conn.commit()
# cursor.close()

# insert
SQL = "INSERT INTO sensors (type, location) VALUES (%s, %s);"
sensors = [('a', 'floor'), ('a', 'ceiling'), ('b', 'floor'), ('b', 'ceiling')]
cursor = conn.cursor()
for sensor in sensors:
  try:
    data = (sensor[0], sensor[1])
    cursor.execute(SQL, data)
  except (Exception, psycopg2.Error) as error:
    print(error.pgerror)
conn.commit()
cursor.close()

cursor = conn.cursor()
query = "SELECT * FROM sensor_data;"
cursor.execute(query)
for row in cursor.fetchall():
    print(row)
cursor.close()