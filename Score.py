import Utils
def add_score(difficulty):
    points = 0
    POINTS_OF_WINNING = (difficulty * 3) + 5
    scores_file = open(Utils.SCORES_FILE_NAME, 'w+')
    for line in scores_file.readlines():
        points: int = int(line)
    scores_file.write(str(POINTS_OF_WINNING + points))
    scores_file.close()