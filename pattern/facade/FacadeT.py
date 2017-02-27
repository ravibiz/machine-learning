import time


class TC1:

     def run1(self):
         print("Inside TC1")
         time.sleep(1)
         print("Setting up")
         time.sleep(1)
         print("Running test")
         time.sleep(1)
         print("Tearing down")
         time.sleep(1)
         print("Testing finished\n")


class TC2:
    def run1(self):
        print("Inside TC2")
        time.sleep(1)
        print("Setting up")
        time.sleep(1)
        print("Running test")
        time.sleep(1)
        print("Tearing down")
        time.sleep(1)
        print("Testing finished\n")


class TestRunn:
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()

    def runAll(self):
        self.tc1.run1()
        self.tc2.run1()


if __name__ == "__main__":
    testRunner = TestRunn()
    testRunner.runAll()
