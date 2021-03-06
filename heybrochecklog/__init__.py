class UnrecognizedException(Exception):
    pass


import argparse  # noqa: E402
from pathlib import Path  # noqa: E402

from heybrochecklog.score import score_log  # noqa: E402
from heybrochecklog.translate import translate_log  # noqa: E402
from heybrochecklog.printer import Printer
from heybrochecklog.printer.printer_file import PrinterFile

def parse_args():
    """Parse arguments."""
    description = 'Tool to analyze, translate, and score a CD Rip Log.'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('log', help='log file to check.', nargs='+')
    parser.add_argument(
        '-t',
        '--translate',
        help='translate a foreign log to English',
        action='store_true',
    )
    parser.add_argument(
        '-m',
        '--markup',
        help='print the marked up version of the log after analyzing',
        action='store_true',
    )
    parser.add_argument(
        '-s',
        '--score-only',
        help='Only print the score of the log.',
        action='store_true',
    )

    parser.add_argument(
        '-c',
        '--check-checksum',
        help='Check the checksum',
        action='store_true',
    )

    parser.add_argument(
        '-z',
        '--no-sub-zero',
        help='Display 0 score if the score is lower than zero',
        action='store_true',
    )

    parser.add_argument(
        '-p',
        '--pure-translate',
        help='Do not include translation header info',
        action='store_true',
    )

    parser.add_argument(
        '-f',
        '--fix-checksum',
        help='Only for -t (--translate). Fix checksum for the new log (works only for EAC)',
        action='store_true',
    )

    parser.add_argument(
        '-o',
        '--output-file',
        help='Write output to file instead of stdout',
    )

    return parser.parse_args()


def runner():
    """Main function to handle command line usage of the heybrochecklog package."""
    args = parse_args()
    for log_path in args.log:
        log_file = Path(log_path)
        if not log_file.is_file():
            print('{} does not exist.'.format(log_path))
        elif args.translate:
            translate_(args, log_file, log_path)
        elif args.log:
            score_(args, log_file, log_path)


def score_(args, log_file, log_path):
    log = score_log(log_file, args)
    printer = Printer()
    if args.output_file:
        printer = PrinterFile(args.output_file)

    if args.score_only:
        if not log['unrecognized']:
            printer.print(log['score'])
        else:
            printer.print('Log is unrecognized: {}'.format(log['unrecognized']))
    else:
        try:
            printer.print(format_score(log_path, log, args.markup))
        except UnicodeEncodeError as error:
            printer.print('Cannot encode logpath: {}'.format(error))


def translate_(args, log_file, log_path):
    log = translate_log(log_file, args.fix_checksum)

    printer = Printer()
    if args.output_file:
        printer = PrinterFile(args.output_file)

    try:
        printer.print(format_translation(log_path, log, args.pure_translate))
    except UnicodeEncodeError as error:
        printer.print('Cannot encode logpath: {}'.format(error))


def format_score(logpath, log, markup):
    """Turn a log file JSON into a pretty string."""
    output = []
    output.append('\nLog: ' + logpath)
    if log['unrecognized']:
        output.append('\nLog is unrecognized: {}'.format(log['unrecognized']))
    else:
        if log['flagged']:
            output.append('\nLog is flagged: {}'.format(log['flagged']))
        output.append('\nDisc name: {}'.format(log['name']))
        output.append('\nScore: {}'.format(log['score']))

        if log['deductions']:
            output.append('\nDeductions:')
            for deduction in log['deductions']:
                output.append('  >>  {}'.format(deduction[0]))

        if markup:
            output.append('\n\nStylized Log:\n\n{}'.format(log['contents']))

    return '\n'.join(output)


def format_translation(logpath, log, pure_translate = False):
    """Turn a translated log JSON into a pretty string."""
    output = []
    if not pure_translate:
        output.append('\nLog: ' + logpath)

    if log['unrecognized']:
        output.append('\nFailed to recognize log. {}'.format(log['unrecognized']))
    elif not pure_translate and log['language'] == 'english':
        output.append('\nLog is already in English!')
    else:
        if not pure_translate:
            output.append('\nOriginal language: {}'.format(log['language']).title())
            output.append('\n---------------------------------------------------')
            output.append('\n')
        output.append(log['log'])

    if not pure_translate:
        output.append('\n')

    return ''.join(output)
