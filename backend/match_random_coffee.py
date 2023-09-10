from datetime import datetime, timedelta


def filter_users(users: list):
    filtered_users = []
    for user in users:
        if user.random_coffee_active:
            if user.random_coffee_days_delta is not None:
                # if user.last_random_coffee_meet + timedelta(days=user.random_coffee_days_delta) <= datetime.now():
                filtered_users.append(user)
    return filtered_users


def match_users(users: list):
    filtered_users = filter_users(users)
    final_matches = []
    for user_main in filtered_users:
        matches = []
        for user_second in filtered_users:
            if user_main == user_second:
                continue
            if user_main in matches or second in final_matches:
                break
            match = [user_main, user_second, set(user_main.tags) & set(user_second.tags)]
            matches.append(match)
        matches.sort(key=lambda x: len(x[2]))
        final_matches.append(matches[-1])
    return final_matches
