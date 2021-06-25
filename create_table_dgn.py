import psycopg2

conn = psycopg2.connect("host=52.34.68.83 dbname=ict_demo user=postgres password=$ViTrox$")
cur = conn.cursor()

tracenum = "dgn"

cur.execute("""
    CREATE TABLE {}(
    dgn_id serial PRIMARY KEY,
    mc_id integer,
    test integer,
    subtest integer,
    module integer,
    slot varchar,
    status varchar

)
""" .format(tracenum))

conn.commit()