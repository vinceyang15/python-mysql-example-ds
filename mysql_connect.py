import _mysql

if __name__ == '__main__':
    db = _mysql.connect('localhost', user='root', passwd='67410322', db='lx')
    db.query("""select * from users limit 5""")
    r = db.use_result()
    print(r.fetch_row())
