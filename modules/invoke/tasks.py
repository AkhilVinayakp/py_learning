# Small task management tools.

from invoke import task

@task
def sayHi(c):
    print("Hi this is a sample comment")


@task(help={'name': 'Provide a name to say hi'})
def sayHito(c, name="Raj"):
    print(f"oh hey this is {name}")
    c.run("dir")

# defining pre and post tasks
@task
def pre_build(c):
    """This is for just running some code before the actual task
    """
    print(">> from the pre task")

@task(pre_build)
def codeCheck(c):
    print(">> Running the task")