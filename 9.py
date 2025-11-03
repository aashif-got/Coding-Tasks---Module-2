import random
import time

def generate_4digit_otp_number():
    
    return f"{random.randint(0, 9999):04d}"

def otp_function(guess, otp):
    return guess == otp

def otp_crack(otp):
    attempts = 0
    t_start = time.time()
    for i in range(10000):                 
        candidate = f"{i:04d}"
        attempts += 1
        if otp_function(candidate, otp):
            return candidate, attempts, time.time() - t_start
    return None, attempts, time.time() - t_start  

if __name__ == "__main__":
    real_otp = generate_4digit_otp_number()
    print("Generated OTP (secret):", real_otp)

    cracked, tries, elapsed = otp_crack(real_otp)
    print("Found OTP:", cracked)
    print("Attempts:", tries)
    print("Time elapsed: {:.4f} seconds".format(elapsed))