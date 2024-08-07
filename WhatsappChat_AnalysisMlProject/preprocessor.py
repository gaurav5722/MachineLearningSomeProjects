import re
import pandas as pd
def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}\s[ap]m\s-\s'
    messages =re.split(pattern,data)[1:]
    dates=re.findall(pattern,data)
    dates_cleaned = [date.replace('\u202f', ' ')   for date in dates]
    formatted_dates = []
    for date in dates_cleaned:
        if ('pm' in date):
            # print(date[12:13])
            if (date.index(':') == 13):
                date = date[:12] + str(int(date[12:13]) + 12) + date[13:17] + (date[17:19].replace('pm', '')) + date[
                                                                                                                19:]
                formatted_dates.append(date)
            else:
                if (date[12:14] == '12'):
                    date = date[:12] + str(int(date[12:14])) + date[14:17] + (
                        date[18:20].replace('pm', '')) + " " + date[20:]
                else:
                    date = date[:12] + str(int(date[12:14]) + 12) + date[14:17] + (
                        date[18:20].replace('pm', '')) + " " + date[20:]
                formatted_dates.append(date)
        else:
            if (date.index(':') == 13):
                date = date[:12] + "0" + date[12:17] + (date[17:19].replace('am', '')) + date[19:]
                formatted_dates.append(date)
            else:
                date = date[:17] + (date[18:20].replace('am', '')) + " " + date[20:]
                formatted_dates.append(date)

    df = pd.DataFrame({'user_message': messages, 'message_date': formatted_dates})
    # convert message_data type
    print(df)
    df['message_date'] = pd.to_datetime(df["message_date"], format='%d/%m/%Y,  %H:%M  - ')
    df.rename(columns={'message_date': 'date'}, inplace=True)
    # seperate users and messages
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\w]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['only_date'] = df['date'].dt.date
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    df['period'] = period
    print(df.head())
    return df
