import pymysql.cursors

connection  = pymysql.connect(
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        db="defaultdb",
        host="mysql-3b505f34-artsidoruk2006-af00.d.aivencloud.com",
        password="AVNS_N6CwY_gQRz4ddywKnKF",
        port=15076,
        user="avnadmin",
        )
def execute(query: str):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()

if __name__ == "__main__":
    print(execute("call stud.GetStudentAverages();"))
