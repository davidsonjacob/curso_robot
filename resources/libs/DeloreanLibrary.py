import psycopg2
from logging import info


class DeloreanLibrary():

    def connect(self):
        return psycopg2.connect(
            host='ec2-52-6-77-239.compute-1.amazonaws.com',
            database='dcu8q6qp9otpgs',
            user='ztaowfcfnoyryq',
            password='67cb5affaf49818c2acdba5dd1df3ba56d865d87f8cc7e8209454cf0c715bcbf'
        )

    # No Robot vira uma KW automágicamente => Remove Student     email@dejado.com
    def remove_student(self, email):

        query = "delete from students where email = '{}'".format(email)
        info(query)

        conn = self.connect()

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()

    def remove_student_by_name(self, name):

        query = "delete from students where name LIKE '%{}%'".format(name)
        info(query)

        conn = self.connect()

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()

    def remove_plan(self, title):

        query = "delete from plans where title LIKE '%{}%'".format(title)
        info(query)

        conn = self.connect()

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()

    def insert_student(self, student):

        self.remove_student(student['email'])

        query = ("insert into students (name, email, age, weight, feet_tall,created_at,updated_at)"
                "values('{}','{}',{},{},{},NOW(),NOW());"
                .format(student['name'], student['email'], student['age'], student['weight'], student['feet_tall']))
        info(query)

        conn = self.connect()

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()
    
    def insert_plan(self, plan):

        self.remove_plan(plan['title'])

        query = ("insert into plans (title, duration, price, created_at, updated_at)"
                "values('{}', {}, {}, NOW(),  NOW());"
                .format(plan['title'], plan['duration'], plan['price']))
        info(query)

        conn = self.connect()

        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()
            
