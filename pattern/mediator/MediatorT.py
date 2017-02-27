import time


class CT:
    def __init__(self):
        self.tm = None
        self.problem = 0

    def setup1(self):
        print("Setting up Test")
        time.sleep(1)
        self.tm.prepareReporting()

    def execute(self):
        if not self.problem:
            print("Executing test")
            time.sleep(1)
        else:
            print("Problem in setup, Test not executed")

    def tearDown(self):
        if not self.problem:
            print("Tearing down")
            time.sleep(1)
            self.tm.publishReport()

    def setTM(self, tm):
        self.tm = tm

    def setProblem(self, problem):
        self.problem = problem


class Reporter:
    def __init__(self):
        self.tm = None

    def prepare(self):
        print("Preparing the report")
        time.sleep(1)

    def report(self):
        print("Reporting results of test")
        time.sleep(1)

    def setTM(self, t ):
        self.tm = tm


class DB:
    def __init__(self):
        self.tm = None

    def insert(self):
        print("Inserting execution status in db")
        time.sleep(1)
        import random
        if random.randrange(1,4) == 3:
            return -1

    def update(self):
        print("Updating execution status in db")
        time.sleep(1)

    def setTM(self, tm):
        self.tm = tm


class TManager:
    def __init__(self):
        self.reporter = None
        self.db = None
        self.ct = None

    def setCT(self, ct):
        self.ct = ct

    def setReporter(self, reporter):
        self.reporter = reporter

    def setDB(self, db):
        self.db = db

    def prepareReporting(self):
        rvalue = self.db.insert()
        if rvalue == -1:
            self.ct.setProblem(1)
            self.reporter.report()

    def publishReport(self):
        self.db.update()
        rvalue = self.reporter.report()


if __name__ == "__main__":
    reporter = Reporter()
    db = DB()
    tm = TManager()
    tm.setReporter(reporter)
    tm.setDB(db)

    reporter.setTM(tm)
    db.setTM(tm)

    while (1):
        ct = CT()
        ct.setTM(tm)
        tm.setCT(ct)
        ct.setup1()
        ct.execute()
        ct.tearDown()
