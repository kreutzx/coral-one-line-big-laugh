import os

# One Line, One Laugh — a single line of at most 200 characters.
ENTRY_TEXT = "The printer has been 'warming up' since March. I have started bringing it coffee, in case the problem is morale."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
