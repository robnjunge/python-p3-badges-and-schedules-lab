def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]


def assign_rooms(speakers):
    return [f"Hello, {speaker}! You'll be assigned to room {index + 1}!" for index, speaker in enumerate(speakers)]

def printer(speakers):
    badges = batch_badge_creator(speakers)
    for badge in badges:
        print(badge)
    
    assignments = assign_rooms(speakers)
    for assignment in assignments:
        print(assignment)
