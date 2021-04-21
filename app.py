import sys
from config import DB_DETAILS

def main():
    """Inputs one argument that specifies the type of instance"""
    env = sys.argv[1]
    if env in DB_DETAILS.keys():
        print(DB_DETAILS[env])

if __name__ == "__main__":
    main()