import fresh_tomatoes
import media

# create instances of Movie class
looper = media.Movie(
        "Looper",
        """In a future society, time-travel exists,
        but it's only available to those with the
        means to pay for it on the black market.
        When the mob wants to eliminate someone,
        it sends the target into the past, where a
        hit man known as a looper lies in wait
        to finish the job. """,
        "http://www.sonypictures.com/movies/looper/assets/images/onesheet.jpg",  # NOQA
        "https://www.youtube.com/watch?v=2iQuhsmtfHw")

eternal_sunshine = media.Movie(
        "Eternal Sunshine of the Spotless Mind",
        """A man finds out his girlfriend erased him from
        his memory, when he retaliates he starts to
        regret it and tries to save the memory of her
        from being erased.""",
        "https://i.ytimg.com/vi/NnqPCBAp2fM/movieposter.jpg",
        "https://www.youtube.com/watch?v=0zFywiAh7N0")


holy_grail = media.Movie(
        "Monty Python and the Quest for the Holy Grail",
        "A King goes in search of knights to complete the" +
        "quest to find the Holy Grail",
        "http://lsc.mit.edu/schedule/2014.2q/poster-montypythonandtheholygrail.jpg",  # NOQA
        "https://www.youtube.com/watch?v=RDM75-oXGmQ")

memento = media.Movie(
        "Memento",
        """Leonard (Guy Pearce) is tracking down the man who
        raped and murdered his wife. The difficulty, however,
        of locating his wifes killer is compounded by the fact
        that he suffers from a rare, untreatable form of memory loss.
        Although he can recall details of life before his accident,
        Leonard cannot remember what happened fifteen minutes ago,
        where he's going, or why.""",
        "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",  # NOQA
        "https://www.youtube.com/watch?v=0vS0E9bBSL0")

days_of_summer = media.Movie(
        "500 Days of Summer",
        """Tom (Joseph Gordon-Levitt), greeting-card writer
        and hopeless romantic, is caught completely off-guard
        when his girlfriend, Summer (Zooey Deschanel),
        suddenly dumps him. He reflects on their 500 days
        together to try to figure out where their love affair
        went sour, and in doing so, Tom rediscovers
        his true passions in life.""",
        "http://static.rogerebert.com/uploads/movie/movie_poster/500-days-of-summer-2009/large_lUh47eMBKUq1OaBkNY27L3gPS6F.jpg",  # NOQA
        "https://www.youtube.com/watch?v=PsD0NpFSADM")

her = media.Movie(
        "Her",
        """A sensitive and soulful man earns a living by
        writing personal letters for other people. Left
        heartbroken after his marriage ends, Theodore
        (Joaquin Phoenix) becomes fascinated with a new
        operating system which reportedly develops into an
        intuitive and unique entity in its own right.
        He starts the program and meets 'Samantha'
        (Scarlett Johansson), whose bright voice reveals
        a sensitive, playful personality. Though 'friends'
        initially, the relationship soon deepens into love.""",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
        "https://www.youtube.com/watch?v=WzV6mXIOVl4")

# create movies array
movies = [looper, eternal_sunshine, holy_grail, memento, days_of_summer, her]

# call open_movies_page function from fresh_tomatoes file
# send the array 'movies'
fresh_tomatoes.open_movies_page(movies)
