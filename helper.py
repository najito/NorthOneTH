import sqlite3

DB_PATH = './todo_service_flask/todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(title, description, date):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('insert into items(title, description, status, duedate) values(?,?,?,?)', (title, description, NOTSTARTED, date))

        conn.commit()
        return {"item": title, "description": description, "status": NOTSTARTED, "duedate": date} 
    except Exception as e:
        print('Error: ', e)
        return None

def get_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_item(title):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from items where title='%s'" % title)
        item = c.fetchone()
        return item
    except Exception as e:
        print('Error: ', e)
        return None

def update_status(title, status):
    if (status.lower().strip() == 'not started'):
        status = NOTSTARTED
    elif (status.lower().strip() == 'in progress'):
        status = INPROGRESS
    elif (status.lower().strip() == 'completed'):
        status = COMPLETED
    else:
        print("Invalid Status: " + status)
        return None

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update items set status=? where title=?', (status, title))
        conn.commit()
        return {title: status}
    except Exception as e:
        print('Error: ', e)
        return None

def delete_item(title):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        # c.execute requires a tuple to be passed in, even if the second value is nothing
        c.execute('delete from items where title=?', (title,))
        conn.commit()
        return {'title': title}
    except Exception as e:
        print('Error: ', e)
        return None

def find_by_status(status):
    if (status.lower().strip() == 'not started'):
        status = NOTSTARTED
    elif (status.lower().strip() == 'in progress'):
        status = INPROGRESS
    elif (status.lower().strip() == 'completed'):
        status = COMPLETED
    else:
        print("Invalid Status: " + status)
        return None
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select * from items where status='%s'" % status)
        rows = c.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None

