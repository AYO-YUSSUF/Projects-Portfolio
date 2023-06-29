# Project 3 – SIRI 1.0.
# This program is a prototype program for SIRI.
# This program will begin by asking the user (within a loop) to make selection from a menu.
# By Abdul Quayyum Yussuf
# June 11, 2023.


# Define Functions -----------------------------------------------------------------------------------------


# The menu of Options and actions  function.--------------------------------------------
def menu_func():
    # This function displays a menu of Options and actions and the Welcome message.
    # Input: none
    # Output: choice - users choice
    # Output: validChoice  - boolean flag for choice valid/not valid

    validChoice = False

    # Create option and action arrays
    options = [1, 2, 3, 4, 5, 6]
    actions = ["Build Playlist", "Display All Songs and authors", "Play All Songs", "Display latest Date & Time",
               "Today's Weather", "Exit Program"]

    # Display a menu of Options and actions and the Welcome message.
    print("\nWelcome! I am SIRI 1.0 . Please Choose what you would like to do from the menu")
    print('{:<20}\t{:<10}'.format('#Option', '#Action'))
    print('{:<20}\t{:<10} '.format(options[0], actions[0]))
    print('{:<20}\t{:<10} '.format(options[1], actions[1]))
    print('{:<20}\t{:<10} '.format(options[2], actions[2]))
    print('{:<20}\t{:<10} '.format(options[3], actions[3]))
    print('{:<20}\t{:<10} '.format(options[4], actions[4]))
    print('{:<20}\t{:<10} '.format(options[5], actions[5]))

    # Prompt user for option choice
    choice = input("\n Enter your Option here : ")
    # Validate input
    while not choice.isdigit() or 0 <= int(choice) > 6:
        print("**Error Invalid Option input. Please try again.")
        choice = input("\n Enter your Option here : ")
    validChoice = True

    return int(choice), validChoice


# The Option 1 function to add to playlist.  --------------------------------------------
def build_playlist():
    # This function prompts for the song name, author name and validates it.
    # Input: none
    # Output: song_name  - song name
    # Output: validInfo  - boolean flag for name valid/not valid
    # Output: author_name  - author name

    validInfo = False

    # Prompt for Song name
    song_name = input("\n\n Enter the Song name : \t ")

    # Replace spaces with NULL
    song_name2 = song_name.replace(" ", "")

    # Check for ALPHA only
    if not song_name2.isalpha():
        print("**Error Invalid Song name input. Please try again.")
        song_name = input("\n\n Enter the Song name : \t ")

    else:
        # convert user input "name" to Upper case
        song_name = song_name.capitalize()
    validInfo = True

    # Prompt for author name
    author_name = input("\n\n Enter the Author name : \t ")

    # Replace spaces with NULL
    author_name2 = author_name.replace(" ", "")

    # Check for ALPHA only
    if not author_name2.isalpha():
        print("**Error Invalid Author name input. Please try again.")
        author_name = input("\n\n Enter the Author name : \t ")
    else:
        # convert user input "name" to Upper case
        author_name = author_name.capitalize()
    validInfo = True

    # Prompt for Song Time
    song_time = input("\n\n Enter the Song Time : \t ")

    # Validate input
    while not song_time.isdigit() or 0 <= int(song_time) > 6:
        print("**Error Invalid Song time input. Please try again.")
        song_time = input("\n\n Enter the Song Time : \t ")
        validInfo = True

    return song_name, validInfo, author_name, int(song_time)


# The Option 2 function to display all songs.--------------------------------------------
def show_playlist(songs, authors):
    # This function displays the entire list of songs and the corresponding singer/author.
    # Input: songs array
    #       : authors array
    lenSongs = len(songs)

    # Displays the entire list of songs and the corresponding singer/author.
    print("\nWelcome to Your Playlist of songs and their corresponding author.")
    print('{:<20}\t{:<10}'.format('#Song', '#Author'))
    print('{:<20}\t{:<10}'.format('____________________', '____________________'))
    i = 0
    while i < lenSongs:
        print('{:<20}\t{:<10} '.format(songs[i], authors[i]))
        i = i + 1


# The Option 3 function to play all songs--------------------------------------------
def PlayOneSong(songs, authors, songtime):
    import time
    import random
    # This function will simulate playing one song.
    # It will loop and display "--- playing song: xxx" based on the value of songtime
    # Input(Args):   songs - list of song names
    #               authors - list of song authors/singers
    #               songtime - length of song in mins (1 to 6)
    # Return:        None

    # Calculate delay time and loop.

    delay = .5  # delay time (secs) between print statements
    loops = songtime  # simulate songtime by looping

    # Validate songtime input value, force to 6 if invalid
    if (loops < 1 or loops > 6):
        loops = 6

    loopcnt = 1
    while (loopcnt <= loops):
        song_index = random.randint(0, len(songs) - 1)
        author_index = song_index  # assuming the author list is in the same order as the song list

        # Display "--- playing song: xxx" based on the value of songtime
        print("--- playing song:", songs[song_index])
        print("\t\t\t --- by ...:", authors[author_index])
        time.sleep(delay)

        loopcnt = loopcnt + 1


# The Option 4 function to display date and time --------------------------------------------
def DisplayDateTime():
    # This function will get and display the current local date and time
    # Input(Args):   None
    # Return:        None

    from datetime import datetime
    # Set debug flag to True to see debug statements
    debug = True

    # Get the current date and time
    curr_dt = datetime.now()  # current date and time
    print(" ")  # line spacer

    if debug:
        print("\nThe current date-time is: ", curr_dt)  # used to verfiy date time

    # Wk 8 Project assignment - fix the following code to display correctly - Status: Done
    # Expected output format:  18 Dec 2022
    formatD = "%d %b, %Y"
    date = curr_dt.strftime(formatD)
    print("Today's date: ", date)

    # Expected output format: (Zero padded am/pm)  08:09:03 AM
    formatT = "%H:%M:%S %p"
    time = curr_dt.strftime(formatT)
    print("Current time: ", time)


# The Option 5 function for weather information.--------------------------------------------
def weather_info():
    import random
    # This function displays the weather information response randomly.
    # Input: none

    # Create an array for the random responses
    responses = ["Right now, the temperature is 22 degrees and cold in Maryland.",
                 "Today in Maryland, you can expect warm weather with a high of 77 degrees and a low of 45 degrees.",
                 "The current weather in Maryland is Windy. Today's high will be 56 degrees with a low of 35 degrees.",
                 "In Maryland, it's Sunny and 52 degrees. Today will have a high of 58 degrees & a low of 31 degrees.",
                 "It's Raining in Maryland right now with a temperature of 41 degrees. Today's high will be 49 degrees "
                 "and the low will be 26 degrees. "]

    # Display the weather responses randomly
    print("\nWelcome to SIRI 1.0 Weather forecast, 'What is the weather today in Maryland, USA?'")
    print(random.choice(responses))


# Display Developer Info. ------------------------------
def myName():
    print("\nDeveloped by,\nAbdul Quayyum Yussuf\nJune 11, 2023.")


# Main
def main():
    SiriOn = True
    songs = list()
    authors = list()
    song_times = 0

    while SiriOn:
        # Prompt user for option number
        option, validChoice = menu_func()
        SiriOn = validChoice
        if validChoice:
            if option == 1:  # Add to the songs and authors list " Option 1"
                # Populate song, authors and song time arrays
                song, validInfo, author, song_time = build_playlist()
                songs.append(song)
                authors.append(author)
                song_times = song_time

            elif option == 2:  # Display the list of songs and their corresponding authors " Option 2"
                show_playlist(songs, authors)

            elif option == 3:  # Play the Songs " Option 3"
                PlayOneSong(songs, authors, song_times)

            elif option == 4:  # Display the Date and Time " Option 4"
                DisplayDateTime()

            elif option == 5:  # Display the Weather forecast " Option 5"
                weather_info()

            elif option == 6:  # Quit the program " Option 6"
                print("SIRI 1.0 turned OFF. Goodbye!")
                SiriOn = False


# Developer Info.
myName()

# --- Execute -----------------------------------------------
main()
