<p align="center">
  <a href="https://openpecha.org"><img src="https://avatars.githubusercontent.com/u/82142807?s=400&u=19e108a15566f3a1449bafb03b8dd706a72aebcd&v=4" alt="Lopenling Redirects" width="150"></a>
</p>

<h1 align="center">Data Fetch and JSON Generation</h1>

<p align="center">A Python Script for Fetching Data from PostgreSQL and Generating JSON Files</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#contributors">Contributors</a> •
  <a href="#acknowledgements">Acknowledgements</a>
</p>

---
## Project owner(s)

<!-- Link to the repo owners' github profiles -->

- [@tenkus47](https://github.com/tenkus47)
  
## Overview

**Data Fetch and JSON Generation** is a Python script designed to fetch data from a PostgreSQL database, process it, and generate JSON files. It is a versatile tool for extracting structured data and converting it into a JSON format for further analysis or storage.

## Installation

Before using the script, ensure you have Python installed on your system. Follow these steps to set up and run the script:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/data-fetch-json-generation.git
   cd data-fetch-json-generation
   ```
2. install dependency

   ```bash
   pip install psycopg2-binary
   ```
   
## Configuration
   
   DATABASE: The name of the PostgreSQL database.
   DB_HOST: The hostname or IP address of the database server.
   DB_USER: The database user's username.
   DB_PASSWORD: The database user's password.
   DB_PORT: The port number for database connection.

## usage

   ```bash
   python fetch_and_generate_json.py
   ```
