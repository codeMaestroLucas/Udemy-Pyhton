# THREADS
from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, txt: str, time: int):
        self.txt = txt
        self.time = time
        super().__init__()
    
    def run(self):
        sleep(self.time)
        print(self.txt)


def main() -> None:
    """Function used to run the main code."""
    t1 = MyThread('Hello wolrd', 3)
    t1.start()
    
    t2 = MyThread('Im a the Latest?', 9)
    t2.start()

    t3 = MyThread('First', 1)
    t3.start()

    t4 = MyThread('Finally t4 is done', 24)
    t4.start()


    for c in range(1, 11):
        print(c)
        sleep(1)
        
    while t4.is_alive(): # While it is not done
        print('T4 is still running...')
        sleep(3)
    
    print('All threads are done.')


if __name__ == '__main__':
    main()