import random
import string
import time

def generate_otp(length=6, expiry_time=30):
    """
    Generate a random OTP of specified length.
    
    :param length: Length of the OTP (default is 6)
    :param expiry_time: Expiry time in seconds (default is 30 seconds)
    :return: tuple containing OTP, expiry time, and generation time
    """
    # Define the character set for OTP
    characters = string.digits  # Only use digits for this OTP

    # Generate OTP
    otp = ''.join(random.choice(characters) for _ in range(length))
    
    # Get current timestamp
    generation_time = time.time()
    
    # Calculate expiry timestamp
    expiry_timestamp = generation_time + expiry_time
    
    return otp, expiry_timestamp, generation_time

def is_otp_valid(otp, correct_otp, expiry_timestamp):
    """
    Check if the OTP is valid and not expired.
    
    :param otp: OTP entered by user
    :param correct_otp: The correct OTP
    :param expiry_timestamp: Expiry timestamp of the OTP
    :return: Boolean indicating if OTP is valid
    """
    current_time = time.time()
    return otp == correct_otp and current_time <= expiry_timestamp

# Example usage
if __name__ == "__main__":
    # Generate OTP
    otp, expiry, generated = generate_otp()
    print(f"Generated OTP: {otp}")
    print(f"Expiry time: {time.ctime(expiry)}")
    
    # Simulate user input
    user_input = input("Enter the OTP: ")
    
    # Check if OTP is valid
    if is_otp_valid(user_input, otp, expiry):
        print("OTP is valid!")
    else:
        print("OTP is invalid or expired.")
