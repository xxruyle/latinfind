import argparse
import latin_find

parolaLink = "https://www.online-latin-dictionary.com/latin-english-dictionary.php?parola="
lemmaLink = "https://www.online-latin-dictionary.com/latin-english-dictionary.php?lemma="

def main():
    l1 = latin_find.latinFind()
    if args.t: 
        l1.reqDefault(parolaLink, args.t)
    #elif args.c: 
    #    l1.reqDefault(lemmaLink, args.c)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="A simple API of the online latin dictionary website")
    parser.add_argument("-t", nargs = "*", metavar="translation default", type=str, help="The latin word you want to translate")
    #parser.add_argument("-c", nargs = "*", metavar="translation choice", type=str, help="The latin word you want to translate")
    args = parser.parse_args()
    main()