import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = ' '
    while city != 'Chicago' or city != 'New York City' or city != 'Washington':
        city = input("Please select either Chicago, Washington or New York City for us to analyse: ").lower()

        if city == 'chicago':
            break
        elif city == 'new york city':
            break
        elif city == 'washington':
            break



    month = ' '
    while month != 'january' or month != 'february' or month != 'march' or month != 'april' or month != 'may' or month != 'june' or month != 'all':
        month = input("Please select a month between January and June or select all: ").lower()

        if month == 'january':
            break
        elif month == 'february':
            break
        elif month == 'march':
            break
        elif month == 'april':
            break
        elif month == 'may':
            break
        elif month == 'june':
            break
        elif month == 'all':
            break


    day = ' '
    while day != 'monday' or day != 'tuesday' or day != 'wednesday' or day != 'thursday' or day != 'friday' or day != 'saturday' or day != 'sunday' or day != 'all':
        day = input("Please select a day of the week or select all: ").lower()

        if day == 'monday':
            break
        elif day == 'tuesday':
            break
        elif day == 'wednesday':
            break
        elif day == 'thursday':
            break
        elif day == 'friday':
            break
        elif day == 'saturday':
            break
        elif day == 'sunday':
            break
        elif day == 'all':
            break




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

    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1



        df = df[df['month'] == month]


    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    common_month = df['month'].mode()[0]
    print("The most popular month was %s" % common_month)


    common_day = df['day_of_week'].mode()[0]
    print("The most popular day was %s" % common_day)


    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most popular hour was %s:00" % common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    popular_station = df['Start Station'].mode()[0]
    print("The station where most trips began was %s" % popular_station)


    popular_end = df['End Station'].mode()[0]
    print("The station where most trips ended was %s" % popular_end)




    trip_combos = df['Start Station'] + " to " + df['End Station']
    popular_trip = trip_combos.mode()[0]
    print("The most popular trip was made from %s" % popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_travel = df['Trip Duration'].sum()
    print("The total amount of travel time is equal to {} seconds".format(int(total_travel)))


    mean_travel = df['Trip Duration'].mean()
    print("The average travel time is {} seconds".format(int(mean_travel)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print("The count of different kinds of users is : %s" % user_types)


    gender_number = df['Gender'].value_counts()
    print("The count of males and females is : %s" % gender_number)

    oldest_year = df['Birth Year'].min()
    newest_year = df['Birth Year'].max()
    common_year = df['Birth Year'].mode()[0]
    print("The oldest user was born in {}, the youngest user was born in {} and the most common year of birth for users is {}".format(int(oldest_year), int(newest_year), int(common_year)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        try:
            user_stats(df)
        except KeyError:
            print("Washington does not have any Gender or Birth year statistics")
        finally:
            raw_data = ' '
            i = 0
            while raw_data != 'no':
                raw_data = input('\nWould you like to see some of the raw data? Enter yes or no\n').lower()
                if raw_data == 'yes':
                    count = df.iloc[i:]
                    print(count.head())
                else:
                    break
                i += 5
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
