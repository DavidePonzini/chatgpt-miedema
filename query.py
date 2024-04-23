from miedema import tables, queries

from dav_tools import argument_parser, messages
import pyperclip


def make_prompt(query, tables):
    return '''Generate the following query in SQL, using the following tables.

-- query --
{}

-- tables --
{}
'''.format(query, tables)


if __name__ == '__main__':
    argument_parser.add_argument('id', help='Query id')

    query = queries[argument_parser.args.id]
    prompt = make_prompt(query, tables)

    print(query)
    
    pyperclip.copy(prompt)
    messages.info('Prompt copied to clipboard')
