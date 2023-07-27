import os
import time
from subprocess import call

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 400
def Screen_cleaner():
    time.sleep(0.7)
    print('\r' + ' ', end='', flush=True)