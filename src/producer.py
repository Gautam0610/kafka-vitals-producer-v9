import os
import json
import time
import random
from datetime import datetime
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS')
OUTPUT_TOPIC = os.getenv('OUTPUT_TOPIC')
SECURITY_PROTOCOL = os.getenv('SECURITY_PROTOCOL')
SASL_MECHANISM = os.getenv('SASL_MECHANISM')
SASL_USERNAME = os.getenv('SASL_USERNAME')
SASL_PASSWORD = os.getenv('SASL_PASSWORD')
DATA_GENERATION_INTERVAL_MS = int(os.getenv('DATA_GENERATION_INTERVAL_MS'))

def generate_vitals_data():
    timestamp = int(datetime.now().timestamp() * 1000)
    body_temperature = round(random.uniform(36.5, 37.5), 1)
    heart_rate = random.randint(60, 100)
    systolic_blood_pressure = random.randint(110, 140)
    diastolic_blood_pressure = random.randint(70, 90)
    respiratory_rate = random.randint(12, 20)
    oxygen_saturation = random.randint(95, 100)
    blood_glucose = random.randint(70, 140)

    vitals_data = {
        'timestamp': timestamp,
        'body_temperature': body_temperature,
        'heart_rate': heart_rate,
        'systolic_blood_pressure': systolic_blood_pressure,
        'diastolic_blood_pressure': diastolic_blood_pressure,
        'respiratory_rate': respiratory_rate,
        'oxygen_saturation': oxygen_saturation,
        'blood_glucose': blood_glucose
    }
    return vitals_data


def create_producer():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        security_protocol=SECURITY_PROTOCOL,
        sasl_mechanism=SASL_MECHANISM,
        sasl_plain_username=SASL_USERNAME,
        sasl_plain_password=SASL_PASSWORD,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer


def main():
    producer = create_producer()
    while True:
        vitals_data = generate_vitals_data()
        producer.send(OUTPUT_TOPIC, vitals_data)
        print(f"Sent: {vitals_data}")
        time.sleep(DATA_GENERATION_INTERVAL_MS / 1000)

if __name__ == "__main__":
    main()