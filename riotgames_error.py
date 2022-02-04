class RegionError(Exception):
    pass


class TierError(Exception):
    def __str__(self):
        return 'wrong Tier'


class QueueError(Exception):
    def __str__(self):
        return 'wrong Queue'
