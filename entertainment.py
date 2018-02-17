import fresh_tomatoes
import media

# creating various instances for the class Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "toystory.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar", "A marine on an Alien planet",
                     "avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

harry_potter = media.Movie(
                            "Harry Potter",
                            """
                            A young boy with a great destiny proves his worth\
while attending Hogwarts School\
of Witchcraft and Wizardry.""",
                            "harrypotter.jpg",
                            "https://www.youtube.com/watch?v=fcPYNxGM7BA")

inception = media.Movie(
                        "Inception",
                        """A skilled extractor is offered a chance to regain his\
old life as payment for a task\
considered to be impossible.""",
                        "inception.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

hunger_games = media.Movie(
                            "The Hunger Games",
                            """Every year in the ruins of what was once\
North America, the evil Capitol of the nation\
of Panem forces each of its twelve districts to\
send a teenage boy and girl to compete in the\
Hunger Games.""",
                            "hungergames.jpg",
                            "https://www.youtube.com/watch?v=mfmrPu43DF8")

fast_and_furious = media.Movie(
                                "Fast and Furious",
                                """An undercover cop infiltrates the world of\
street racing to solve a series of truck\
hijackings perpetrated by Dominic Toretto""",
                                "fastandfurious.jpg",
                                "https://www.youtube.com/watch?v=ZsJz2TJAPjw")

# creating an array called movies
movies = [
            toy_story, avatar, harry_potter,
            inception, hunger_games, fast_and_furious]

# using the python program fresh tomatoes for opening our website
fresh_tomatoes.open_movies_page(movies)
