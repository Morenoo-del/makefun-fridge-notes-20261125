#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — one dry, petty note."""

ENTRY = "You opened me 14 times today and ate nothing but pickles. The yogurt expired Tuesday \u2014 it had more of a plan than you do."

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
