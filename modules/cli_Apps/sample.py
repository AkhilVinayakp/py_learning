import time
import click
from colorama import init, Fore

# Initialize colorama
init()

# Define colors
GREEN = Fore.GREEN
RESET = Fore.RESET

@click.command()
def main():
    click.echo(f"{GREEN}Starting animation..{RESET}", nl=False)
    for _ in range(10):
        click.echo(f"{GREEN}...", nl=False)
        time.sleep(0.5)
        print('\b ', end=' ', flush=True)
        time.sleep(0.5)
    click.echo(f"\n{GREEN}Animation finished!{RESET}")


import time
import sys

def animate_processing(message, duration=5, interval=0.1):
    dot_count = 0
    start_time = time.time()

    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{message}{'.' * dot_count}   ")
        sys.stdout.flush()
        time.sleep(interval)
        dot_count = (dot_count + 1) % 4  # Increase the number of dots, wrapping around after 3

    sys.stdout.write(f"\r{message}{'.' * dot_count} Complete\n")
    sys.stdout.flush()

# Example usage
# animate_processing("Processing", duration=5, interval=0.1)

import time
from tqdm import tqdm
from colorama import init, Fore, Style

# Initialize colorama
init()

# Define colors
GREEN = Fore.GREEN
RESET = Style.RESET_ALL

def task_with_progress_bar(duration):
    with tqdm(total=duration, desc=f"{GREEN}Progress{RESET}", bar_format="{l_bar}{bar}{r_bar}") as progress_bar:
        for _ in range(duration):
            time.sleep(1)
            progress_bar.update(1)

    print(f"{GREEN}Task completed.{RESET}")

# Example usage
task_with_progress_bar(10)  # 10 seconds duration


if __name__ == "__main__":
    # main()
    pass
