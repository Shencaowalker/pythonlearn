#coding:utf-8

class User(Model):
	# 定义类的属性到列的映射：
        id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')



class Field(object):
	def __init__(self,name,column_type):
		self.name=name
		self.column_type=column_type
	def __str__(self):
		return "<%s:%s>" %(self.__class__.__name__,self.name)


class StringField(Field):
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	 def __init__(self, name):
	 	super(IntegerField, self).__init__(name, 'bigint')
