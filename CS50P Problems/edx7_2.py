import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'^<iframe .*src="(https?://(?:www\.)?youtube\.com/embed/[a-z0-9]+)"( title=".+")?( frameborder=".+")?( allow=".+")?.*</iframe>$', s, re.IGNORECASE):
        return match.group(1)
    else:
        pass


if __name__ == "__main__":
    main()

