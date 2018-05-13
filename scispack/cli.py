"""Command line interface ot the scispack package."""
import sys
import scispack
from scispack import cfg

HELP = """scispack: awesome command line tools.

Usage:
   -h, --help: print the help
   -v, --version: print the installed version
   --say-hi [NAME]: say hi to [NAME]
   -cb, --chucks-birthday: give the birthday date of Chuck Norris
   -ac, --area-circle [RADIUS]: compute the area of a circle
"""


def cli_program(args):
    """The actual command line tool.

    It is separated from the main script to allow testing.

    Parameters
    ----------
    args: list
        output of sys.args[1:]
    """

    if len(args) == 0:
        print(HELP)
        return

    if args[0] in ['-h', '--help']:
        print(HELP)
        return

    if args[0] in ['-v', '--version']:
        print('scispack (awesome command line tools): ' + scispack.__version__)
        print('License: public domain')
        print('scispack is provided "as is", without warranty of any kind')
        return

    if args[0] in ['--say-hi']:
        if len(args) == 1:
            print('scispack --say-hi: at least one name needs to be provided!')
            return
        msg = 'Hi'
        for name in args[1:]:
            msg += ' ' + str(name)
        msg += '! How are you today?'
        print(msg)
        return

    if args[0] in ['-cb', '--chucks-birthday']:
        print(cfg.PARAMS['chuck_norris_birthday'])
        return

    if args[0] in ['-ac', '--area-circle']:
        if len(args) != 2:
            print('scispack ---area-circle needs a radius parameter!')
            return
        radius = float(args[1])
        print('The area of a circle with radius {} '.format(radius) +
              'is {}'.format(scispack.area_of_circle(radius)))
        return


def main():
    """Entry point for the application script"""

    # Minimal code because we don't want to test for sys.argv
    # (we could, but this is way above the purpose of this package
    cli_program(sys.argv[1:])
