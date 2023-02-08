import requests
import json
import time
import csv
import schedule
import os

exgRateList = []
avgExgRate = 0


# Fetched data and printing out the conversion rate
def usdEurExchange():
    global exgRateList, avgExgRate
    try:
        response = requests.get(
            "https://www.freeforexapi.com/api/live?pairs=USDEUR")
    except Exception as error:
        print(f"Exception caught: {error}")
        exit()
    responseJson = response.json()
    exgRate = responseJson['rates']['USDEUR']['rate']
    exgRateList.append(exgRate)
    print(exgRate)


# Clear all the scheduled jobs
def cancelJob():
    # Created an csv file and loaded with exchange rates for further use by flask app
    dirname = os.path.dirname(os.path.abspath(__file__))
    csvfilename = os.path.join(dirname, 'exgRates.csv')
    with open(csvfilename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(exgRateList)
    schedule.clear()
    exit()


# Run the scheduled jobs in a loop
if __name__ == '__main__':
    # Job is scheduled for every 5 seconds as per requirement
    schedule.every(5).seconds.do(usdEurExchange)

    # Clear all the jobs after 1 minute
    schedule.every(65).seconds.do(cancelJob)

    while True:
        schedule.run_pending()
        time.sleep(1)
