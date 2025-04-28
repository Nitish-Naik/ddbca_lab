import random
import time
from tqdm import tqdm

def simulate_crack():
    # Randomly generate an 8-digit WPS PIN
    wps_pin = str(random.randint(10000000, 99999999))
    print(f"Simulating WPS PIN Brute Force crack for: {wps_pin}")

    start_time = time.time()
    # Simulate cracking first 4 digits 
    print("Cracking first 4 digits...")
    for first_half in tqdm(range(10000)):
        if str(first_half).zfill(4) == wps_pin[:4]:
            break
        time.sleep(0.0005)

    # Simulate cracking last 3 digits (last digit is checksum, skipped) 
    print("\nCracking Second Half (Last 3 digits)...")
    for second_half in tqdm(range(1000)):
        if str(second_half).zfill(3) == wps_pin[4:7]:
            break
        time.sleep(0.0005)
    end_time = time.time()

    print(f"\nWPS PIN Cracked: {wps_pin}") 
    print(f"Total Attempts: {first_half + second_half}") 
    print(f"Time Taken: {round(end_time - start_time, 2)} seconds") 
if __name__ == "__main__":
    simulate_crack()
