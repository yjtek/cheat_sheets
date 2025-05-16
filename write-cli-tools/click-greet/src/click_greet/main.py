import click

@click.group()
def greet():
    """Greet command group."""
    pass

@greet.command()
@click.argument('name') 
@click.option('--extra-string', help='tag on to greeting') 
@click.option('--arg1') 
@click.option('--arg2', is_flag=True) 
@click.option('--arg3', is_flag=True) 
@click.option('--arg4', multiple=True) 
def hello(name, extra_string=None, arg1=None, arg2=False, arg3=False, arg4=None):
    """
    Say hello to NAME.
        > (click-greet) yongjian.tek@ITSG009365-MAC click-greet % greet hello yj --extra-string hihihi --arg1 wtf --arg2 --arg3 --arg4 123 --arg4 234
        > Hello yj! hihihi
        > arg1='wtf', arg2=123, arg3=True, arg4=('123', '234')
    """    
    if arg2:
        arg2=123
    
    click.echo(f'Hello {name}! {extra_string}')
    click.echo(f"{arg1=}, {arg2=}, {arg3=}, {arg4=}")

@greet.command()
@click.argument('name')
def goodbye(name):
    click.echo(f'Goodbye {name}!')

def main():
    """Entry point for the CLI."""
    greet()
    