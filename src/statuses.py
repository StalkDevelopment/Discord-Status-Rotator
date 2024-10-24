statuses = [
    "Playing a game",
    "Listening to music",
    "Watching a movie",
    "Coding a bot",
    "Chatting with friends"
]

def get_next_status(status_cycle):
    return next(status_cycle)
