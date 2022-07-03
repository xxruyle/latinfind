import argparse
import latin_find

def main():
    l1 = latin_find.latinFind()
    if args.t: 
        l1.reqDefault(args.t)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="A simple API of the online latin dictionary website")
    parser.add_argument("-t", nargs = "*", metavar="translation", type=str, help="The latin word you want to translate")
    args = parser.parse_args()
    main()