
import random
import time

def generate_random_body_params():
    # Simulated function to generate random body temperature and heart rate values
    body_temperature = random.uniform(36.0, 37.5)  # Normal body temperature range
    heart_rate = random.randint(60, 100)  # Normal heart rate range

    return body_temperature, heart_rate

def adjust_room_temperature(body_temperature, heart_rate):
    # Simulated logic to adjust room temperature based on body parameters
    if body_temperature > 37.0 or heart_rate > 90:
        print("Room temperature increased.")
        # Add logic to increase room temperature (e.g., by controlling a smart thermostat)
    else:
        print("Room temperature normal.")
        # Add logic to maintain or decrease room temperature if necessary

if __name__ == "__main__":
    try:
        while True:
            # Simulate reading body parameters
            body_temp, heart_rate = generate_random_body_params()

            # Adjust room temperature based on simulated body parameters
            adjust_room_temperature(body_temp, heart_rate)

            # Simulate a delay between readings (adjust as needed)
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nScript terminated by user.")
