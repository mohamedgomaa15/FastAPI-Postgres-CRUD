from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
 

# Load .env file
load_dotenv()

# Read variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine (connection to DB)
engine = create_engine(DATABASE_URL)

# Create session (used for interacting with DB)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for ORM models
Base = declarative_base()


# --- Test block: only runs when file executed directly ---
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("Connected successfully to PostgreSQL!")

            # Run a simple SELECT query
            result = connection.execute(text("SELECT * FROM Employee;"))

            # Print all rows
            rows = result.fetchall()
            if not rows:
                print("No data found in employees table.")
            else:
                print("Data from employees table:")
                for row in rows:
                    print(row)

    except Exception as e:
        print("Error while getting data:", e)
