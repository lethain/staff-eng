import html2markdown
import argparse



def extract(txt):
    return html2markdown.convert(txt)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    args = parser.parse_args()
    with open(args.filepath, 'r') as fin:
        txt = fin.read()
        print(extract(txt))


if __name__ == "__main__":
    main()
