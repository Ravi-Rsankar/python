from psutil import net_io_counters
import time


def get_data():
    network = net_io_counters()
    return network.bytes_recv, network.bytes_sent


recvInit, sendInit = get_data()

try:
    while True:
        recvNew, sendNew = get_data()
        print(
            f"\rDownload: {(recvNew - recvInit)/1024:.2f} KBps, Upload: {(sendNew-sendInit)/1024:.2f} KBps",
            flush=True,
            end=" ",
        )
        recvInit, sendInit = recvNew, sendNew
        time.sleep(1)
except KeyboardInterrupt as e:
    print("\nQuitting...")
