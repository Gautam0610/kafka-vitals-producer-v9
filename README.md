# kafka-vitals-producer-v9

A Kafka producer that generates and sends random human vitals data.

## Prerequisites

*   Docker
*   Docker Compose (optional)

## Getting Started

1.  Clone the repository:

    ```bash
    git clone https://github.com/Gautam0610/kafka-vitals-producer-v9.git
    cd kafka-vitals-producer-v9
    ```

2.  Create a `.env` file based on the `.env.example` file and fill in the required values.

    ```bash
    cp .env.example .env
    # Modify the .env file with your Kafka configuration
    ```

3.  Build and run the Docker container:

    ```bash
    docker build -t kafka-vitals-producer .
    docker run --env-file .env kafka-vitals-producer
    ```

    Alternatively, use Docker Compose (if you have a `docker-compose.yml` file):

    ```bash
docker-compose up
    ```

## Configuration

The following environment variables must be set in the `.env` file:

*   `KAFKA_BOOTSTRAP_SERVERS`: The Kafka bootstrap servers.
*   `OUTPUT_TOPIC`: The output topic name.
*   `SECURITY_PROTOCOL`: The security protocol to use (e.g., `SASL_SSL`).
*   `SASL_MECHANISM`: The SASL mechanism to use (e.g., `PLAIN`).
*   `SASL_USERNAME`: The SASL username.
*   `SASL_PASSWORD`: The SASL password.
*   `DATA_GENERATION_INTERVAL_MS`: The data generation interval in milliseconds.

## Disclaimer

This project generates random vitals data and is intended for testing and demonstration purposes only. It should not be used for medical diagnosis or treatment.