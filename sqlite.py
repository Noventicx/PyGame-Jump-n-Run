import sqlite3
import constants


# der Score wird in die Datenbank geschrieben, falls die DB noch nicht vorhanden ist, wird diese erstellt
def insert_score():
    sqliteCon = sqlite3.connect('Highscore.db')
    cursor = sqliteCon.cursor()
    print("Connected to the database")
    cursor.execute("CREATE TABLE IF NOT EXISTS highscore (id INTEGER PRIMARY KEY AUTOINCREMENT, score INTEGER);")
    sqliteCon.commit()
    print("Database created")
    cursor.execute("INSERT INTO highscore (score) VALUES (" + str(
        constants.current_coins * 100 - constants.current_deaths * 10) + ")")
    sqliteCon.commit()
    cursor.close()


# dies Highscores werden ausgelesen
def get_scores(font, screen):
    sqliteCon = sqlite3.connect('Highscore.db')
    cursor = sqliteCon.cursor()
    print("Connected to the database")
    res = cursor.execute("SELECT score FROM highscore order by score desc limit 3")
    i = 1
    for row in res:
        highscore_text = font.render(str(i) + ". " + str(row[0]), False, constants.WHITE)
        highscore_text_rect = highscore_text.get_rect(
            center=(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 20 * (i + 1)))
        screen.blit(highscore_text, highscore_text_rect)
        i += 1

    cursor.close()
    return res
