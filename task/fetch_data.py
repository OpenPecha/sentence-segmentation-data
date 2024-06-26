import os
import psycopg2
import json




database=os.environ["DATABASE"]
host=os.environ["DB_HOST"]
user=os.environ["DB_USER"]
password=os.environ["DB_PASSWORD"]
port=os.environ["DB_PORT"]

db_params = {
    "host": host,
    "database": database,
    "user": user,
    "password": password,
    "port": port,
}
table_name='"Text"'

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Query to get a list of all tables in the current schema
    cursor.execute(f'SELECT reviewed_text,version FROM {table_name} ORDER BY id')
    text_by_version = {}
    for row in cursor.fetchall():
        reviewed_text, version = row
        if version not in text_by_version:
               text_by_version[version] = []
          
        if reviewed_text is None:
            text_by_version[version].append(None)
        else:
            try:
                # Parse the JSON string into a Python dictionary
                parsed_json = json.loads(reviewed_text)
                text_by_version[version].append(parsed_json)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON for version {version}: {e}")

    for version, texts in text_by_version.items():
        json_data = {"version": version, "reviewed_text": texts}
        file_name = f"output/{os.path.splitext(version)[0]}.json"

        with open(file_name, "w",encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4,ensure_ascii=False)

        print(f"Generated JSON file: {file_name}")
    # Close the cursor and connection
    cursor.close()
    conn.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)