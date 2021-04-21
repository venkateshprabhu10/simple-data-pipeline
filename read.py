from utils import get_connection

def read_table(db_details, table_name, rows = None):
    limit = f" LIMIT {rows}" if rows else ""

    connection = get_connection(db_details["source"])

    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name}{limit}"
    cursor.execute(query)

    data = cursor.fetchall()
    column_names = cursor.column_names

    connection.close()

    return data, column_names
