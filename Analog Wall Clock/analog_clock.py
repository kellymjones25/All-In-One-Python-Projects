import time

def display_time():
    """
    Display the current time in HH:MM:SS format.
    """
    current_time = time.localtime()  # get local time
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    print(f"\r🕒 Current Time: {hours:02d}:{minutes:02d}:{seconds:02d}", end="", flush=True)


def run_clock():
    """
    Run the analog clock in the console.
    Updates every second until user interrupts (Ctrl+C).
    """
    print("=== Analog Clock (Console Version) ===")
    print("Press Ctrl+C to exit.")
    try:
        while True:
            display_time()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Clock stopped. Goodbye!")


if __name__ == "__main__":
    run_clock()
