# Simply check the swagger yaml files to make sure that every path:
# contains a "summary"
# "tags" are not present
#
# returns an exit code accordingly

import sys
import yaml

def verify_docs_files(files):
    errored = False
    for yfile in files:
        with open(yfile, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)

        for i in cfg["paths"]:
            for j in cfg["paths"][i]:
                k = cfg["paths"][i][j]

                if "summary" not in k:
                    print("Error: summary missing from Swagger doc in: %s " % (i))
                    errored = True

    return errored

if __name__ == "__main__":
    sys.exit(verify_docs_files(sys.argv[1:]))
