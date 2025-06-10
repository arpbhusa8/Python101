def add_task(task):
    return toDo.append(task)
def remove_task(task):
    return toDo.remove(task)
def view_tasks():
    return toDo

toDo=[]
add_task('buy groceries')
add_task('finish homework')
add_task('go to the gym')
print(view_tasks())

remove_task('finish homework')
print(view_tasks())