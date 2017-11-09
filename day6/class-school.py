#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/9 22:50
# @Author  : Evescn
# @Site    : 
# @File    : class-school.py
# @Software: PyCharm

class SchoolMember(object):
    membe_nums = 0
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.enroll()

    def enroll(self):
        SchoolMember.membe_nums += 1
        print("\033[32;0mThe [%s] school SchoolMember [%s] is enroll\033[0m" %(self.membe_nums, self.name))

    def tell(self):
        print("Hello! my name is [%s]" %self.name)

class Teacher(SchoolMember):
    def __init__(self, name, age, sex, course, salary):
        super(Teacher, self).__init__(name, age, sex)
        # SchoolMember.__init__(self, name, age, sex)  # 旧式类的方法
        self.course = course
        self.salary = salary

    def teaching(self):
        print("Teacher [%s] is teaching [%s]" %(self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, course, tution):
        super(Student, self).__init__(name, age, sex)
        self.course = course
        self.tution = tution

    def pay_tution(self):
        print("Fuck, [%s] paying tution [%s]" %(self.name, self.tution))


t1 = Teacher("Evescn", 24, 'F', "PY", 1000)
t2 = Teacher("Gmkk", 24, "N/A", "PY", 1000)

s1 = Student("tom", 19, "F", "python", 5000)
s2 = Student("jack", 18, "F", "python", 5000)

t1.tell()
t1.teaching()

s1.tell()
s1.pay_tution()