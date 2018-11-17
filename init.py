import sys
import getopt
import crawler


def main(argv):
    help = "USAGE: init.py -f <folder> -e <export>"
    folder = ""
    export = ""

    try:
        opts, args = getopt.getopt(argv, "hf:e:", ["folder=", "export="])
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    if len(opts) < 1:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(help)
            sys.exit()
        elif opt in ("-f", "--folder"):
            folder = arg
        elif opt in ("-e", "--export"):
            export = arg
    crawler.crawl(folder)


if __name__ == "__main__":
    main(sys.argv[1:])
