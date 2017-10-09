class Robot:
    """Represents a robot, with a name."""

    # Class variable, counting robots

    population = 0

    def __init__(self, name):
        """Initialize data"""
        self.name = name
        print("Initializing {}".format(self.name))

        #When a robot is created the robot population increases
        Robot.population += 1

    def die(self):
        """Destroying robot"""
        print("{} is being destroyed".format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))

        else: 
            print("There are still {:d} robots working".format(
                Robot.population))

    def say_hi(self):
        """Greet by new worker robot"""
        print("Greetings, my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """Print current population"""
        print("We have {:d} robots".format(cls.population))

droid1 = Robot('Clifford')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('Astro')
droid2.say_hi()
Robot.how_many()

print("\nRobots work and then they go\n")

print("Robots are finished.  To the trash heap they go!")

droid1.die()
droid2.die()

Robot.how_many()