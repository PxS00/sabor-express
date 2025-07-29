class Rating:
    """
    Represents a customer's rating for a restaurant.
    """

    def __init__(self, client, grade):
        """
        Initializes a Rating instance.

        Parameters:
        - client (str): The name of the customer giving the rating.
        - grade (float): The rating value (between 1 and 5).
        """
        self._client = client
        self._grade = grade