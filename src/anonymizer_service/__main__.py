import sys
from anonymizer_service.anonymize import find_entities
from anonymizer_service import anonymize
from anonymizer_service.external_functions import create_output_file_name
import argparse
import os.path
import json


def main(argv):
    inputfile = ''
    outputfile = ''
    method = ''
    conf_file = 'anonymizer_service/conf.json'
    # in_order = True
    patterns_file = 'anonymizer_service/patterns.json'
    helptext = '''
------------------------------------------------------------------------------
python3 -m anonymizer_service
    -i <inputfile>
    -o <outputfile>
    -f <folder>
    -m <method_used(s,strict)/symbol/(lenght==lenght_of_word)>
    -p <patterns.json>
    -v <verbose>
    -w <array of words>
    '''

    parser = argparse.ArgumentParser(
        description='Anonymize file', usage=helptext)
    parser.add_argument('-i',
                        '--ifile',
                        help='Input file',
                        type=str,
                        required=False)

    parser.add_argument('-o',
                        '--ofile',
                        help='Output file',
                        type=str,
                        required=False)

    parser.add_argument('-p',
                        '--patterns_file',
                        help='Patterns file',
                        type=str,
                        required=False)

    parser.add_argument('-m',
                        '--method',
                        help='Which method is applied to the identified data', type=str,
                        required=False)

    parser.add_argument('-f',
                        '--folder',
                        help='Anonymize all files in folder',
                        type=str,
                        required=False)
    parser.add_argument('-v',
                        '--verbose',
                        help='Verbose execution',
                        action='store_true',
                        required=False)
    parser.add_argument('-w',
                        '--words',
                        help='Custom words search',
                        required=False)
    parser.add_argument('-x',
                        '--exclude',
                        help='Exclude words',
                        required=False)
    args = parser.parse_args()
    print(args)
    # If given configuration file check that it exists
    #
    # If the service can not track conf.json
    if not os.path.exists(conf_file):
        raise NameError(
            "Please make sure that the conf.json file's path is: anonymizer_service/conf.json")

    with open(conf_file, mode='r') as cf:
        data = cf.read().replace('\n', '')
        conf_json = json.loads(data)

    inputfile = args.ifile

    if args.ofile != None:
        outputfile = args.ofile
    elif inputfile != None:
        outputfile = create_output_file_name(inputfile)

    if args.words != None:
        words_array_string = args.words
        words_array = words_array_string.split(',')
    else:
        words_array = []

    if args.exclude != None:
        exclude_array_string = args.exclude
        exclude_array = exclude_array_string.split(',')
    else:
        exclude_array = []

    if args.method != None:
        try:
            method_input = args.method
            [method_chosen,
             symbol_input,
             lenght_input] = method_input.split('/')
            assert method_chosen.lower() in ['s', 'strict', 'e', 'elastic']
            assert len(symbol_input) == 1
            method = [method_chosen, symbol_input, lenght_input]
        except:
            raise NameError('Make sure you give the right method')
    else:
        if conf_json['general']['method']['strict']['is_active'] == 'True':
            method = ['strict',
                      conf_json['general']['method']['strict']['value'],
                      conf_json['general']['method']['strict']['lenght_of_word']
                      ]
        elif conf_json['general']['method']['elastic']['is_active'] == 'True':
            method = ['elastic',
                      conf_json['general']['method']['elastic']['value'],
                      None
                      ]

    verbose = args.verbose

    # If given patterns file check that it exists
    #
    if args.patterns_file != None:
        patterns_file = args.patterns_file
        if not os.path.exists(patterns_file):
            raise NameError(
                f'Please make sure that the file ({patterns_file}) exists.')
    else:
        # If the service can not track patterns.json
        patterns_file = conf_json['paths']['patterns']
        if not os.path.exists(patterns_file):
            raise NameError(
                f"Please make sure that the patterns file's path is: {patterns_file}")

    if (inputfile != None):
        # Pass custom patterns to find_entities()
        print('here')
        find_entities(ifile=inputfile,
                      ofile=outputfile,
                      method=method,
                      patterns_file=patterns_file,
                      verbose=verbose,
                      words_array=words_array,
                      exclude_array=exclude_array)

    if args.folder != None:
        print('there')
        folder = args.folder
        if not os.path.exists(folder):
            raise NameError(f"This folder ({folder}) doesn't exist.")
        files = []
        for file in os.listdir(folder):
            if file.endswith(".txt") or file.endswith(".odt"):
                files.append(folder + file)
        for file in files:
            find_entities(ifile=file,
                          ofile=create_output_file_name(file),
                          method=method,
                          patterns_file=patterns_file,
                          verbose=verbose,
                          words_array=words_array,
                          exclude_array=exclude_array)


if __name__ == "__main__":
    main(sys.argv[1:])
