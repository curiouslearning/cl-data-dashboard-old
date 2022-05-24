import json
import requests
import re
from datetime import date
from datetime import timedelta

import pandas as pd

origin_date = date(2022, 5, 14)  # the first day that data is correct
today = date.today()

print(origin_date.isoformat())

BASE_URL = "https://lrs.curiouslearning.org/api/xAPI/statements"
ACTIVITY_PARAM = "activity=https://data.curiouslearning.org/xAPI/activities/assessment/ukranian/letter-sound"
VERB_PARAM = "verb=http://adlnet.gov/expapi/verbs/completed"


def agent_param(name, homepage):
    return("agent={%22account%22:{%22name%22:%22" + name +
           "%22,%20%22homePage%22:%20%22" + homepage + "%22}}")


def get_completed_for_day(day):
    lrs_URL = f"{BASE_URL}?{ACTIVITY_PARAM}&{VERB_PARAM}&since={day}&until={day + timedelta(days=1)}"
    df = pd.DataFrame()

    while lrs_URL:
        response = requests.get(lrs_URL)
        jsonResponse = json.loads(response.text)
        df_statements = pd.json_normalize(jsonResponse['statements'])
        df = pd.concat([df, df_statements])
        lrs_URL = jsonResponse['more']

    num_completed = len(df[(df['verb.display.en-US'] == 'completed') & (
        df['object.id'] == 'https://data.curiouslearning.org/xAPI/activities/assessment/ukranian/letter-sound')])
    return(num_completed)


df = pd.DataFrame(columns=['date', 'activity', 'count'])
my_date = origin_date
while my_date != today:
    print(my_date)
    num_completed = get_completed_for_day(my_date)
    df.loc[len(df.index)] = [my_date, ACTIVITY_PARAM, num_completed]
    my_date = my_date + timedelta(days=1)

df.to_csv('complete_count.csv')
exit()
