import os
from datetime import datetime

def log_event(message):
    log_file = "AI--Log.txt"
    date_str = datetime.now().strftime('%Y-%m-%d %H:%M')
    
    # Check if file exists to decide if we need the header
    file_exists = os.path.isfile(log_file)
    
    with open(log_file, "a", encoding="utf-8") as f:
        if not file_exists:
            # Create the professional header if it's a new file
            f.write("┌" + "─"*58 + "┐\n")
            f.write(f"│ {'PROJECT ARCHIVE:'.ljust(20)} { 'Y-J PORTFOLIO'.rjust(35)} │\n")
            f.write(f"│ {'DEVELOPER:'.ljust(20)} { 'YUSUPHA JAMMEH'.rjust(35)} │\n")
            f.write(f"│ {'VERIFIED STATUS:'.ljust(20)} { 'GITHUB STUDENT'.rjust(35)} │\n")
            f.write("└" + "─"*58 + "┘\n\n")

        # Write the entry in the style you liked
        f.write(f" 🔷 ENTRY_POINT >> {date_str}\n")
        f.write(f" ┃\n")
        f.write(f" ┗━━ LOG: {message}\n")
        f.write(f" {'-'*60}\n")

    print(f"✔️ Activity logged to AI--Log.txt")
