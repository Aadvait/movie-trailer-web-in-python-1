import fresh_tomatoes
import media

Toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

Avatar = media.Movie("Avatar",
                     "In 2154, humans have depleted Earth's natural resources, leading to a severe energy crisis.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

School_of_Rock = media.Movie("School Of Rock",
                             "School of Rock is a 2003 musical comedy film directed by Richard Linklater, produced by Scott Rudin, and written by Mike White.",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

Ratatouille = media.Movie("Ratatouille",
                          "Remy is an idealistic and ambitious young rat, gifted with highly developed senses of taste and smell.",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
 
Midnight_in_Paris = media.Movie("Midnight in Paris",
                                "Midnight in Paris is a 2011 fantasy comedy film written and directed by Woody Allen.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=dtiklALGz20")

The_Hunger_Games = media.Movie("The Hunger Games",
                               "The Hunger Games is a 2012 American post-apocalyptic science fiction action adventure film directed by Gary Ross and based on the novel of the same name by Suzanne Collins.",
                               "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                               "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [Toy_story, Avatar, School_of_Rock, Ratatouille, Midnight_in_Paris, The_Hunger_Games]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)
