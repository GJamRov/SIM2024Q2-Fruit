import os.path
import database

if __name__ == "__main__":
    if not os.path.exists('sampleDatabase.db'):
        import database

    # TODO: Main Function Logic