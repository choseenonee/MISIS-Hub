from datetime import datetime, timedelta


def filter_users(users: list):
    filtered_users = []
    for user in users:
        if user.random_coffee_active:
            if user.random_coffee_days_delta is not None:
                # if user.last_random_coffee_meet + timedelta(days=user.random_coffee_days_delta) <= datetime.now():
                filtered_users.append(user)
    return filtered_users


def user_in_matches(user, matches):
    for match in matches:
        if user in match:
            return True
    return False


def match_users(users: list):
    filtered_users = filter_users(users)
    final_matches = []
    for user_main in filtered_users:
        matches = []
        for user_second in filtered_users:
            if user_main == user_second:
                continue
            if user_in_matches(user_main, final_matches) or user_in_matches(user_second, final_matches):
                continue
            match = [user_main, user_second, set(user_main.tags) & set(user_second.tags)]
            matches.append(match)
        if len(matches) > 0:
            matches.sort(key=lambda x: len(x[2]))
            final_matches.append(matches[-1])
    return final_matches
