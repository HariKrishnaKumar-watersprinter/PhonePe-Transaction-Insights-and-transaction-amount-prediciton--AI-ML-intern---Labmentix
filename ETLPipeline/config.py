import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import pandas as pd
import psycopg2
import toml
import streamlit as st
import urllib.parse

# Connecting Database and create the Database
DATA_ROOT = 'https://github.com/PhonePe/pulse'
secrets_path ="F:/Project/Labmantix/phone pe/streamlit/.streamlit/secrets.toml"
engine = None
DB_CONNECTION_STRING = None

try:
    # st.secrets does not have a 'load_file' method and is only populated during 'streamlit run'.
    # We load the TOML file manually to support standalone execution (python config.py).
    if os.path.exists(secrets_path):
        with open(secrets_path, "r") as f:
            secrets = toml.load(f)
        raw_url = secrets.get('database', {}).get('url')
    else:
        raw_url = st.secrets.get('database', {}).get('url')
        
    if raw_url:
        # FIX 1: Replace 'postgres://' with 'postgresql://' for SQLAlchemy compatibility
        if raw_url.startswith("postgres://"):
            DB_CONNECTION_STRING = raw_url.replace("postgres://", "postgresql://", 1)
        else:
            DB_CONNECTION_STRING = raw_url
        print("Database Connection String formatted.")

except Exception as e:
    print(f"Error formatting URL: {e}")

try:
    if DB_CONNECTION_STRING:
        # FIX 2: Aiven/Cloud Postgres usually requires SSL. 
        # We add connect_args to ensure the connection succeeds.
        connect_args = {'sslmode': 'require'}
        
        # Step A: Connect to the default database ('defaultdb' is provided in your URL)
        # We use this connection to create the 'phonepe_pulse' database.
        
        server_engine = sa.create_engine(DB_CONNECTION_STRING, connect_args=connect_args, pool_pre_ping=True)
        
        # Check if 'phonepe_pulse' exists, create if not
        with server_engine.connect() as connection:
            # Check if DB exists
            db_exists = connection.execute(sa.text("SELECT 1 FROM pg_database WHERE datname='phonepe_pulse'")).fetchone()
            
            if not db_exists:
                # Commit the transaction before CREATE DATABASE (Postgres requirement)
                connection.execute(sa.text("COMMIT"))
                try:
                    connection.execute(sa.text("CREATE DATABASE phonepe_pulse"))
                    print("Database 'phonepe_pulse' created successfully.")
                except Exception as create_err:
                    print(f"Could not create database (might exist or permission denied): {create_err}")
            else:
                print("Database 'phonepe_pulse' already exists.")

        # Step B: Now connect specifically to the new database
        # We construct the new URL by replacing 'defaultdb' with 'phonepe_pulse'
        
        # Parse the URL to swap the database name safely
        p = urllib.parse.urlparse(DB_CONNECTION_STRING)
        
        # Replace path (database name)
        new_path = p.path.replace('/defaultdb', '/phonepe_pulse') if '/defaultdb' in p.path else '/phonepe_pulse'
        
        # FIX 3: Parse the query string into a dictionary
        # parse_qs returns values as lists, e.g., {'sslmode': ['require']}, so we flatten it.
        query_dict = {}
        if p.query:
            parsed_query = urllib.parse.parse_qs(p.query)
            for k, v in parsed_query.items():
                query_dict[k] = v[0] if v else ''
        
        # Reconstruct URL
        new_db_url = sa.engine.url.URL(
            drivername=p.scheme,
            username=p.username,
            password=p.password,
            host=p.hostname,
            port=p.port,
            database=new_path.lstrip('/'),
            query=query_dict # Pass the dictionary here
        )
        
        engine = sa.create_engine(new_db_url, connect_args=connect_args, pool_pre_ping=True)
        
        # Step C: Setup Base and Session
        Base = declarative_base()
        
        # Reflect existing tables (if any)
        Base.metadata.reflect(engine)
        
        # Create session factory
        Session = sessionmaker(bind=engine)
        
        print("Database Engine Created Successfully.")
    else:
        print("Error: No Database URL found. 'engine' will be None.")

except Exception as e:
    print(f"Critical Error: {e}")
    engine = None
