from tortoise import Model,fields

class Todo(Model):
    id = fields.IntField(pk=True)
    content = fields.CharField(max_length=150)
    create_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=150,unique=True)
    password = fields.CharField(max_length=500)
    created_at = fields.DatetimeField(auto_now_add=True)

class History(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=150)
    title  = fields.CharField(max_length=150)
    href = fields.CharField(max_length=300)
    time = fields.DatetimeField(auto_now_add=True)
    class Meta:
        unique_together=(("username", "title"), )
        
class Favor(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=150)
    title  = fields.CharField(max_length=150)
    href = fields.CharField(max_length=300)
    site = fields.CharField(max_length=150)
    class Meta:
        unique_together=(("username", "title"), )