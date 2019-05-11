import datetime


def create_file():
    try:
        with open('Edit history.txt', 'w') as failas:
            failas.write('All moved files will be shown here. \n')
    except FileExistsError:
        return False


def mark_file(filename, prev_path, current_path):
        with open('Edit history.txt', 'a') as failas:
            failas.write('<------> \n')
            failas.write('On ' + str(datetime.datetime.now()) + ' file ' + filename + ' was moved from ' + prev_path + ' to ' + current_path + '\n')
