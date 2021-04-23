from utils import get_connection

def build_insert_query(table_name, cols):
    values = "%s, " * len(cols)
    values = values[:-2]
    query = f"INSERT INTO {table_name} ({', '.join(cols)}) VALUES ({values})"
    return query

def write_table(db_details, table_name, values, cols, batch_size=1000, logs=True):
    recs = []
    count = 1
    connection = get_connection(db_details["target"])
    cursor = connection.cursor()
    query = build_insert_query(table_name, cols)
    
    for rec in values:
        recs.append(rec)
        if count % batch_size == 0:
            cursor.executemany(query, recs)
            connection.commit()
            if logs:
                print(f"{count} rows inserted")
            recs = []
        count += 1
    cursor.executemany(query, recs)
    connection.commit()
    if logs:
        print(f"{count} rows inserted")
