# /usr/bin/env python
# ClockBook.py
import datetime, re, argparse, sys
class clockBook():
    def __init__(self):
        self.startTime = datetime.datetime.now()
    def currentPassage(self, text, passageOnly=True, regex='standard'):
        days = 365
        hours = 365*24
        minutes = 365*24*60
        with open(text, 'r') as f:
            data = f.read()
            now = datetime.datetime.now()
            year = now.year
            yearStart = datetime.datetime.fromordinal(datetime.date(year,1,1).toordinal())
            diff = yearStart-now
            minutes_offset = diff.total_seconds() / 60
            secondsPerYear = 60 * 60 *24 * 365
            offset = abs((minutes_offset / (secondsPerYear/60)) * 100)
            position = len(data) * (offset/100)
            sliver = len(data)/minutes
            sliverInt = int(sliver)
            positionInt = int(position)
            redLine = data[positionInt:positionInt+sliverInt]
            dBlockLeft = data[positionInt-1024:positionInt]
            dBlockRight = data[positionInt:positionInt+1024]
            dblock = dBlockLeft + dBlockRight
            if regex == 'standard':
                lineClip = re.compile('(.*)?\n')
            else:
                lineClip = re.compile(regex)
            redLineLeft = lineClip.search(dBlockLeft[::-1]).group()[::-1]
            redLineRight = lineClip.search(dBlockRight[:-1]).group()
            passage = (redLineLeft+redLineRight)[1:-1]
            print('Sliver Size: {}'.format(sliver))
            print('Position: {}'.format(position))
            print('Sliver: {}'.format(redLine))
            print('Passage: {}'.format(passage))
            if passageOnly == True:
                return 'Time Sample: {}'.format(now)
            else:
                return (now, sliver, position, passage, dblock)
parser = argparse.ArgumentParser(description='Determine the point in a book relative to the date and time.',
                                prog='ClockBook.py',
                                epilog='Please Enjoy.')
parser.add_argument('-file', '-f', required=True,
                    help='The file path of the text to clock.',)
namespace = parser.parse_args(sys.argv[1:])
if namespace.file:
    book = clockBook()
    print(namespace.file)
    print(book.currentPassage(namespace.file))
else:
    print('Must provide input.')