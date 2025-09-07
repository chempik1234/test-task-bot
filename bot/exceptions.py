class NoVacancyToPublishException(Exception):
    def __init__(self):
        super().__init__(
            "no vacancy to publish",
        )
