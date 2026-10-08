ratings = {
    "inception": {
        "ali": 9,
        "sara": 8,
        "reza": 10
    },
    "avatar": {
        "ali":7,
        "sara":6
    },
    "interstellar": {
        "sara":10,
        "reza":9
    }
}
for movie in ratings:
    total = 0
    for user in ratings[movie]:
        total += ratings[movie][user]
    average = total / len(ratings[movie]) 
    print(movie,"average score",average)   