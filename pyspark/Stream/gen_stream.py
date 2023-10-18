"""
create a sample stream of random numbers,
"""
import socket
import random
import time
import pandas as pd

PORT = 7000
HOST = "localhost"


def initiate_server(data_type):
    """
    Run a socket server at the given Port
    :return:
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f">> listening on port {PORT} on Host {HOST}")
    conn, address = server.accept()
    print(f">> Initiated connection with {address}")
    while True:
        data = generate_sample_data(data_type=data_type)
        conn.send(f"{data}\n".encode())
        time.sleep(1)
    # conn.close()


def generate_sample_data(data_type="random") -> str:
    """
    generate data to send
    :param data_type:
    :return:
    """
    if data_type == "random":
        rn = random.randint(1, 10000)
        return str(rn)
    if data_type == "dataset":
        """
        Return a set of 3 rows.
        """
        data = pd.read_csv("../Data/Iris.csv")
        sample_data = data.sample(1)
        sample_data = "-".join([str(x) for x in sample_data.values.tolist()[0]])
        return sample_data


if __name__ == "__main__":
    initiate_server(data_type="dataset")