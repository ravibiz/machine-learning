class SwiCTh:
    def __init__(self, flipUpCmd, flipDownCmd):
        self.flipUpCommand = flipUpCmd
        self.flipDownCommand = flipDownCmd

    def flipUp(self):
        self.flipUpCommand.execute()

    def flipDown(self):
        self.flipDownCommand.execute()


class Light:
    def turnOn(self):
        print("The light is on")

    def turnOff(self):
        print("The light is off")


class Command:
    def __init__(self):
        pass

    def execute(self):
        pass


class FlipUpCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turnOn


class FlipDownCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turnOff


class LightSwiCTh:
    def __init__(self):
        self.light = Light()
        self.flipUpCommand = FlipUpCommand(self.light)
        self.flipDownCommand = FlipDownCommand(self.light)
        self.swiCTh = SwiCTh(self.flipUpCommand, self.flipDownCommand)

    def swiCThc(self, cmd):
        cmd = cmd.strip().upper()
        try:
            if cmd == "ON":
                self.swiCTh.flipUp()
            elif cmd == "OFF":
                self.swiCTh.flipDown()
            else:
                print("Invalid command")
        except RuntimeError:
            print("Error in executing command")

if __name__ == "__main__":
    lightSwiCTh = LightSwiCTh()

    print("SwiCTh ON..")
    lightSwiCTh.swiCThc("ON")

    print("SwiCTh OFF..")
    lightSwiCTh.swiCThc("OFF")

    print("Invaild..")
    lightSwiCTh.swiCThc("TEST")
