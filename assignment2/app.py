from flask import Flask
import csv
import logging
import os

app = Flask(__name__)

dirname = os.path.dirname(os.path.abspath(__file__))
logFilename = os.path.join(dirname, 'logFile.log')

# Logger is created and configured
logging.basicConfig(filename=logFilename,
                    format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@app.route('/')
def home():
    avgExgRate, lenOfRow = 0, 0
    csvfilename = os.path.join(dirname, 'exgRates.csv')
    with open(csvfilename, 'r') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            lenOfRow = len(row)
            rates = [eval(i) for i in row]
            break
        avgExgRate = round(sum(rates)/lenOfRow, 4)
    logger.info(f'\n\n\nAverage exchange rate : {avgExgRate}\n\n\n')
    return f"Average exchange rate: {avgExgRate}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
