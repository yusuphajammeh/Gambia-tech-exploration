import sys
from YJ_Logger import log_event

if __name__ == "__main__":
    # Allows you to type: python log.py "My message"
    # OR just: python log.py and it will ask you.
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    else:
        print("\n" + "─ " * 30)
        message = input("📝 What would you like to log, YUSUPHA? ")
        print("─ " * 30)

    log_event(message, category="MANUAL")