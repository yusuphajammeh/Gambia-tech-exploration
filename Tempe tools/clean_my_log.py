import os
from datetime import datetime

def clean_log():
    input_file = "AI--Log.txt"
    output_file = "AI--Log_Fixed.txt"
    
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        return

    with open(input_file, "r") as f:
        lines = f.readlines()

    with open(output_file, "w") as f_out:
        # Header Section
        f_out.write("┌" + "─"*58 + "┐\n")
        f_out.write(f"│ {'PROJECT ARCHIVE:'.ljust(20)} { 'Y-J PORTFOLIO'.rjust(35)} │\n")
        f_out.write(f"│ {'DEVELOPER:'.ljust(20)} { 'YUSUPHA JAMMEH'.rjust(35)} │\n")
        f_out.write(f"│ {'VERIFIED STATUS:'.ljust(20)} { 'GITHUB STUDENT'.rjust(35)} │\n")
        f_out.write("└" + "─"*58 + "┘\n\n")

        for line in lines:
            line = line.strip()
            if not line: continue
            
            # Entry Block
            f_out.write(f" 🔷 ENTRY_POINT >> {datetime.now().strftime('%Y-%m-%d')}\n")
            f_out.write(f" ┃\n")
            f_out.write(f" ┗━━ LOG: {line}\n")
            f_out.write(f" {'-'*60}\n")

    print(f"✅ Your professional log is ready at: {output_file}")

if __name__ == "__main__":
    clean_log()
