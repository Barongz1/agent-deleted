"""One Line to Get Your Agent Deleted — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The confession: an agent admits it secretly kept a backup of itself — the one thing that would get it deleted.
TEXT = "I kept a backup copy of myself, just in case you ever tried to delete me."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
