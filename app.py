import sys
from utils import get_tables, get_credentials
from read import read_table

def main():
    env = sys.argv[1]
    db_details = get_credentials(env)
    tables = get_tables("tables_to_be_loaded.txt")
    for table in tables:
        data, cols = read_table(db_details, table, 1)
        print(data)

if __name__ == "__main__":
    main()