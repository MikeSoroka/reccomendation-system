# As now I'm busy with the API part, instead of model, so here is just a dummy model unitl  I return to it

class MovieReccomender:
    def __init__(self, weights):
        self.weights = weights

    def user_reccomendation(self, user):
        return [1, 2, 3]

    def movie_reccomendation(self, movie):
        return [1, 2, 3]