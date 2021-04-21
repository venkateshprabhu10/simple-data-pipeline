import sys
from config import DB_DETAILS
from utils import get_tables

def main():
    """Inputs one argument that specifies the type of instance"""
    env = sys.argv[1]
    if env in DB_DETAILS.keys():
        tables = get_tables("tables_to_be_loaded.txt")
        for table in tables:
            print(table)

if __name__ == "__main__":
    main()