# Fetch Rewards Data Engineering Take-Home Project

This project is a small application that reads JSON data from an AWS Simple Queue Service (SQS) Queue, transforms that data to mask personal identifiable information (PII), and writes each record to a Postgres database.

## Project Overview

The objective of this project is to:

	Read JSON data containing user login behavior from an AWS SQS Queue.
	Mask the device_id and ip fields to protect personal identifiable information (PII).
	Flatten the JSON data object and write each record to a Postgres database.
	The application is built with Python and uses Docker and Docker Compose to manage the required services.

## Requirements

	Docker (v20.10.0+)
	Docker Compose (v1.27.0+)
	Python (v3.7+)
	Pip (Python's package installer)


## Setup

	Ensure Docker and Docker Compose are installed on your system.

	Clone this repository to your local machine:

	git clone <repository-url>

	Navigate to the project directory:

	cd fetch-rewards-takehome

	Build and run the Docker containers:

	docker-compose up -d

	Install the required Python packages:

	pip install -r requirements.txt


## Running the Application

	To start the ETL (Extract, Transform, Load) process, run the following command:

	python src/etl.py

	This will read messages from the SQS queue, mask the PII data in each message, and insert each record into the Postgres database.

## Running the Tests

	To run the tests, use the following command:

	pytest tests/

	This will run all test cases defined in the tests/ directory.

## Project Structure

	fetch_rewards_takehome
	│
	├── src
	│   ├── __init__.py
	│   ├── config.py
	│   ├── db_handler.py
	│   ├── sqs_handler.py
	│   ├── etl.py
	│   └── masker.py
	├── tests
	│   ├── __init__.py
	│   └── test_etl.py
	│
	├── README.md
	├── requirements.txt
	└── docker-compose.yml


	src/config.py: Contains configuration information for the Postgres database and SQS queue.
	src/db_handler.py: Handles connections to the Postgres database and defines a function to insert data into the user_logins table.
	src/etl.py: Defines the main ETL process, including reading messages from the SQS queue, masking PII data, and inserting the data into the Postgres database.
	src/masker.py: Defines a function to mask PII data in a record.
	tests/test_etl.py: Contains test cases for the ETL process.
	requirements.txt: Specifies the Python packages required to run the application.
	docker-compose.yml: Defines the services (LocalStack and Postgres) that make up the application.
