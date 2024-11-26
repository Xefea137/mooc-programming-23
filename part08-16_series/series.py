# Write your solution here:
class Series:
    def __init__(self, title: str, no_of_season: int, genres: list):
        self.title = title
        self.no_of_season = no_of_season
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        if rating > 5 and rating < 0:
            raise ValueError("Rating should be between 0 and 5")
        self.ratings.append(rating)

    def __str__(self):
        genre_string = ", ".join(self.genres)
        if len(self.ratings) == 0:
            return f"{self.title} ({self.no_of_season} seasons)\ngenres: {genre_string}\nno ratings "
        else:
            return f"{self.title} ({self.no_of_season} seasons)\ngenres: {genre_string}\n{len(self.ratings)} ratings, average {(sum(self.ratings)/len(self.ratings)):.01f} points "

def minimum_grade(rating: float, series_list: list):
    grade_list = []
    for item in series_list:
        if (sum(item.ratings)/len(item.ratings)) > rating:
            grade_list.append(item)
    return grade_list

def includes_genre(genre: str, series_list: list):
    genre_list = []
    for item in series_list:
        if genre in item.genres:
            genre_list.append(item)
    return genre_list

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 1.5:")
    for series in minimum_grade(1.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)
    #a minimum rating of 4.5:
    #Dexter
    #genre Comedy:
    #South Park
    #Friends

    print()

    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    print(dexter)
    #Dexter (8 seasons)
    #genres: Crime, Drama, Mystery, Thriller
    #no ratings

    print()

    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)
    #Dexter (8 seasons)
    #genres: Crime, Drama, Mystery, Thriller
    #5 ratings, average 3.4 points