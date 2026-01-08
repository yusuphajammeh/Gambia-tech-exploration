import os
from datetime import datetime


# No import of 'log_event' here! That was the cause of the error.

def log_event(message, category="LOG"):
    """
    The central engine for all Y-J Portfolio logging.
    This file defines the design and saves it to AI--Log.txt.
    """
    log_file = "AI--Log.txt"
    date_str = datetime.now().strftime('%Y-%m-%d %H:%M')

    header = (
        f"┌{'─' * 58}┐\n"
        f"│ {'PROJECT ARCHIVE:'.ljust(20)} {'Y-J PORTFOLIO'.rjust(35)} │\n"
        f"│ {'DEVELOPER:'.ljust(20)} {'YUSUPHA JAMMEH'.rjust(35)} │\n"
        f"│ {'VERIFIED STATUS:'.ljust(20)} {'GITHUB STUDENT'.rjust(35)} │\n"
        f"└{'─' * 58}┘\n"
    )

    try:
        # Check if we need to add the professional header
        needs_header = not os.path.exists(log_file) or os.path.getsize(log_file) == 0

        with open(log_file, "a", encoding="utf-8") as f:
            if needs_header:
                f.write(header)

            f.write(f"\n 🔷 ENTRY_POINT >> {date_str}\n")
            f.write(f" ┃\n")
            f.write(f" ┗━━ {category}: {message}\n")
            f.write(f" {'─' * 60}\n")

        print(f"✔️ {category} entry archived.")
    except Exception as e:
        print(f"❌ Engine Error: {e}")