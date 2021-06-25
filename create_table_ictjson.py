import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=$ViTrox$")
cur = conn.cursor()

tracenum = "test_json"

cur.execute("""
    CREATE TABLE {}(
    id serial PRIMARY KEY,
    json_data jsonb,
    date_insert timestamp default now()
)
""" .format(tracenum))

conn.commit()