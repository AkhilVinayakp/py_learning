from cli_utlis import *
import click
import threading

def migs(message:str):
    print(f"{threading.current_thread().ident}: {message}")

@click.group
def attack_protocol():
    animate_processing("Preparing protocols ")

@attack_protocol.command()
@click.argument('name')
def attack(name):
    print(f"Initializing {name}....")
    animate_processing("Launching Monitoring Protocols")
    progress_task(duration=23, end_message="Zulu Deployed")
    animate_processing("Scanning Zulu")
    print("Zulu on range.")
    progress_task(duration=12, end_message="Establishing COMs: ZULU")
    animate_processing("Initializing War room Protocols", end_text="Done")
    print("Deck: All set.")
    progress_task(duration=200, end_message="Desk Protocol completed")
    threads = []
    for input_value in ["dager0: ready", "dager1: ready", "dager2: stand by"]:
        thread = threading.Thread(target=migs, args=(input_value,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    attack_protocol()
