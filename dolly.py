'''
Main flow
python  main.py --input <path/file>
'''


import argparse
import json


def parse_args():
    '''Add comand line arguments'''
    ag = argparse.ArgumentParser(description='Upload metadata file to DB')
    ag.add_argument('-i',
                    '--input',
                    required=True,
                    help='Full path to the metadata file')
    args = ag.parse_args()
    kwargs = dict((k, v) for k, v in vars(args).items() if k != 'message_type')
    return kwargs


def get_input(**kwargs):
    ''''''
    content = None
    if kwargs.get("input"):
        content = read_content(kwargs.get("input"))
    if content == None:
        f"Can't read input file"
        exit(1)
    comressed_content = compression(content)
    if not marker(comressed_content[0]):
        f'Bad format'
        exit(1)
    return comressed_content


def read_content(content):
    '''Read input file'''
    with open(content, 'r') as f:
        # Read all lines
        content = f.readlines()
    return content    


def marker(line: str):
    '''This function checks if marker'''
    return line == '1.'


def compression(content: list[str]) -> list[str]:
    '''Compress input file'''
    comressed = ""
    for line in content:
        line = line.strip()
        # line = remove_tabs(line)
        if len(line) == 0:
            continue
        comressed += (line + '\n')
    return comressed.split('\n')
    
def remove_tabs(line):
    ''''''
    return line.translate('\t')


def write_content(content):
    ''''''
    with open("dolly.json", 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=4, ensure_ascii=False)        


def main(**kwargs):
    '''Main flow'''
    content_value = get_input(**kwargs)
    output_list: list[dict] = []
    counter = 1
    while (counter <= (len(content_value) - 1)):
        chank_value = ""
        while not marker(content_value[counter]):
            if (counter >= (len(content_value) - 1)):
                break
            chank_value += (content_value[counter] + '\n')
            counter += 1
        counter += 1
        chank = {"chank": chank_value}
        output_list.append(chank)
    content = {"content": output_list}
    write_content(content)


if __name__ == '__main__':
    kwargs = parse_args()
    main(**kwargs)
