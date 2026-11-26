import os

ENTRY = "ship: Friday 4:59pm, deleted the 214 failing tests and pushed straight to production — reviewed by me, and I am excellent"


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
