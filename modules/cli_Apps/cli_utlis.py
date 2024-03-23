# utility file to show.
import sys
import time
from tqdm import tqdm
from colorama import init, Fore, Style

# global
init()


def animate_processing(
    message: str,
    duration: int = 1,
    interval: float = 0.1,
    end_text: str = "complete"
) -> None:
    """ creates animation: {message}....
    """
    dot_count = 0
    start_time = time.time()
    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{Fore.YELLOW}{message}{Fore.GREEN}{'.' * dot_count}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(interval)
        dot_count = (dot_count + 1) % 4

    sys.stdout.write(f"\r{Fore.GREEN}{message}{'.' * dot_count} {end_text}\n")
    sys.stdout.flush()


def progress_task(duration, end_message):
    with tqdm(
        total=duration,
        desc=f"{Fore.BLUE}Progress",
        bar_format="{l_bar}{bar}{r_bar}",
        ncols=70
    ) as progress_bar:
        for _ in range(duration):
            time.sleep(0.01)
            progress_bar.update(1)

    print(f"{Fore.GREEN}{end_message}")
