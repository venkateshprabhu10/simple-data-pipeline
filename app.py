import sys
from utils import get_tables, get_credentials
from read import read_table
from write import write_table

def main():
    env = sys.argv[1]
    db_details = get_credentials(env)
    tables = get_tables("tables_to_be_loaded.txt")
    for table in tables:
        print("Discovering data...")
        data, cols = read_table(db_details, table)
        print(f"Table: {table} | {len(data)} rows")
        print("Writing data...")
        write_table(db_details, table, data, cols)
        print("Process completed")

if __name__ == "__main__":
    main()