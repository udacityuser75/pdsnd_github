import time
import pandas as pd
import numpy as np

#Place the dictionary with the list of cities
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
PossibleMonth = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    while city == None:
        
        city = input("Enter your city: ('chicago', 'new york city', 'washington')")
        if city.lower() in CITY_DATA.keys():
            city = city.lower()
        else:
            print (city + " Is not an abaliable City")
            city = None
        
        
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = None
    while month == None:
        month = input("Wich month are you interested in?: (all, january, february, ... , june)")
        if month.lower() in PossibleMonth:
            month = PossibleMonth.index(month.lower())
        else:
            print (month + " Is not an abaliable month")
            month =  None
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    PossibleDay = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    day = None
    while day == None:
        day = input("Wich day?: (all, monday, tuesday, ... sunday)")
        if day.lower() in PossibleDay:
            day = day.title()
        else:
            print (day + " Is not an abaliable day")
            day =  None
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    
    df["combination"] = df['Start Station'] + ' With ' + df['End Station']
    
    # filter by month if applicable
    if month != 0:

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    print('Most Populars...')
    # TO DO: display the most common month
    popular_month = PossibleMonth[df['month'].mode()[0]]
    print(' '*16, 'Month:', popular_month.title())

    # TO DO: display the most common day of week
    popular_dayofweek = df['day_of_week'].mode()[0]
    print(' '*16, 'Day of Week:', popular_dayofweek)

    # TO DO: display the most common start hour
    popular_start_hour = df['hour'].mode()[0]
    print(' '*16, 'Start Hour:', popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('Most Commons...')
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(' '*16, 'Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(' '*16, 'End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    #output = df.groupby(['column1','column2']).count().sort_values(by=['column1','column2'], axis = 0)[0]
    popular_combo = df['combination'].mode()[0]
    print(' '*16, 'Combination:', popular_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(' '*16, 'Total travel time:', total_travel_time, " minutes")

    # TO DO: display mean travel time
    mean_travel_time = round(df['Trip Duration'].mean(), 0)
    print(' '*16, 'Mean travel time:', mean_travel_time, " minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_types =  df.groupby(['User Type']).size()
    except:
        print (' '*16, "There was no 'User Type' data ")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        return
    #print (user_types)
    for index, value in user_types.items():
        print (' '*16, "There was {} people for the user type '{}'".format(value,index ))

    # TO DO: Display counts of gender
    try:
        user_gender =  df.groupby(['Gender']).size()
    except:
        print (' '*16, "There was no 'Gender' data ")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        return
    
    for index, value in user_gender.items():
        print (index, value)
        print (' '*16, "There was {} {}".format(value,index))
    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        Birth_Year =  df['Birth Year']
        print ("About year of birth...")
        print (' '*16, "Earliest year of birth: {}".format(int(Birth_Year.min())))      
        print (' '*16, "Most recent year of birth: {}".format(int(Birth_Year.max())))
        print (' '*16, "Most common year of birth: {}".format(int(Birth_Year.mode()[0])))
    except:
        print (' '*16, "There was no 'Birth Year' data ")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
        return


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def displays_raw(df):

    userraw = None
    while userraw == None:
        userraw = cleanuser(input('\nWould you like to see raw data? Enter yes or no.\n'))
        if userraw == False:
            return
    
    number_of_rows = len(df.index)
    numberRows = 5
    
    numberInit = 0
    numberEnd = numberInit + numberRows
    print (df.iloc[numberInit:numberEnd,:])
    while userraw == True:
        #Print Five lines
        anwerdLoop = False
        numberInit += numberRows
        numberEnd += numberRows
        
        if numberEnd > number_of_rows:
            numberEnd = number_of_rows
            anwerdLoop = True
            
        print (df.iloc[numberInit:numberEnd,:])
        
        if anwerdLoop:
            numberInit = 0
            numberEnd = numberInit + numberRows
            userraw = cleanuser(input('\nWould you like to see raw data AGAIN? Enter yes or no.\n'))

        else:
            userraw = cleanuser(input('\nWould you like to see the NEXT 5 lines of raw data? Enter yes or no.\n'))
        
    return
            
def cleanuser(answer):
    """Clean up the answer of the user"""            
    if answer.lower() == "yes" or answer.lower() == "y":
        return True
    elif answer.lower() == "no" or answer.lower() == "n":
        return False
    else:
        return None
def main():
    while True:
        #DONE
        city, month, day = get_filters()
        #DONE
        df = load_data(city, month, day)
        #DONE
        time_stats(df)
        #DONE
        station_stats(df)
           
        trip_duration_stats(df)
           
        user_stats(df)

        displays_raw(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
