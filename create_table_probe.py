import psycopg2

conn = psycopg2.connect("host=52.34.68.83 dbname=ict_demo user=postgres password=$ViTrox$")
cur = conn.cursor()

tracenum = "probe"

cur.execute("""
    CREATE TABLE {}(
    probe_id serial PRIMARY KEY,
    failure_type varchar,
    probe varchar,
    usage integer,
    node_name varchar,
    device_name varchar,
    datetime timestamp
    
)
""" .format(tracenum))

conn.commit()