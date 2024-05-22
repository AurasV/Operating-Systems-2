import random
import time


class Factor(object):
    def __init__(self, id, name, status, time):
        self.id = id
        self.name = name
        self.status = status
        self.time = time

    def show(self):
        print("id: " + str(self.id) + "; name: " + str(self.name) + "; status: " + str(self.status) + "; time: " + str(
            self.time))


class Person(Factor):
    def __init__(self, habit, location):
        self.habit = habit
        self.location = location
        self.disease = None

    def move(self):
        return

    def getIn(self):
        return

    def getOut(self):
        return

    def use(self):
        return


class HomeAppliance(Factor):
    def __init__(self, location, effectLevel):
        self.location = location
        self.effectLevel = effectLevel

    def setStatus(self):
        return


class Environment:
    def __init__(self, temperature, humidity, illumination, noiseLevel):
        self.temperature = temperature
        self.humidity = humidity
        self.ilumination = illumination
        self.noiseLevel = noiseLevel

    def getEnvironmentInfo(self):
        print("temperature: " + str(self.temperature) + "; humidity: " + str(self.humidity) + "; illumination: " + str(
            self.ilumination) + "; noiseLevel: " + str(self.noiseLevel))


class Internal(Environment):
    def __init__(self, temperature, humidity, illumination, noiseLevel, size):
        super().__init__(temperature, humidity, illumination, noiseLevel)
        self.size = size

    def getEnvironmentFromApplianceEffect(self):
        return


class Weather(Environment):
    def __init__(self, temperature, humidity, illumination, noiseLevel, level):
        super().__init__(temperature, humidity, illumination, noiseLevel)
        self.level = level

    def setEffect(self):
        return


class VirtualSpace(object):
    def __init__(self, size, location, Persons, appliances, environment):
        self.factors = None
        self.size = size
        self.location = location
        self.Persons = Persons
        self.appliances = appliances
        self.environment = environment

    def show(self):
        print("size: " + str(self.size) + "; location: " + str(self.location))

    def getEvent(self):
        return


class Reasoning(object):
    def __init__(self, dbConnection, refSmartHome):
        self.dbConnection = dbConnection
        self.refSmartHome = refSmartHome

    def getCases(self):
        return

    def doReasoning(self):
        return

    def caseMatching(self):
        return

    def getEnvironmentInfo(self):
        return self.refSmartHome.environment

    def determineDisease(self):
        diseases_conditions = {
            "Heatstroke": {"min_temp": 30, "max_temp": 50, "severity": "emergency"},
            "Hypothermia": {"min_temp": -5, "max_temp": 0, "severity": "emergency"},
            "Sunburn": {"min_temp": 25, "max_temp": 35, "severity": "warning"},
            "Frostbite": {"min_temp": -45, "max_temp": -10, "severity": "warning"},
            "Dehydration": {"min_temp": 35, "max_temp": 50, "severity": "normal"},
            "Flu": {"min_temp": 5, "max_temp": 15, "severity": "normal"},
            "Common Cold": {"min_temp": 0, "max_temp": 8, "severity": "normal"},
            "Allergies": {"min_temp": 10, "max_temp": 25, "severity": "low"},
            "Asthma Attack": {"min_temp": 5, "max_temp": 20, "severity": "low"},
            "Heat Exhaustion": {"min_temp": 27, "max_temp": 40, "severity": "low"},
        }

        env = self.getEnvironmentInfo()
        temp = env.temperature

        possible_diseases = []
        for disease, conditions in diseases_conditions.items():
            if conditions["min_temp"] <= temp <= conditions["max_temp"]:
                possible_diseases.append((disease, conditions["severity"]))

        if not possible_diseases:
            return Disease("none", "Healthy")

        selected_disease = random.choice(possible_diseases)
        return Disease(selected_disease[1], selected_disease[0])

    def assignDiseases(self):
        pers = self.refSmartHome.Persons
        for Person in pers:
            Person.disease = self.determineDisease()


class Disease(object):
    def __init__(self, severity, name):
        self.name = name
        self.severity = severity


class DBConnection:
    def __init__(self, connectionString):
        self.connectionString = connectionString

    def read(self):
        return

    def write(self):
        return

    def close(self):
        return


if __name__ == '__main__':
    while True:
        envTemperature = random.randint(-45, 45)
        noiseLevel = random.randint(30, 80)
        env1 = Environment(envTemperature, 19, "good", noiseLevel)

        habits = ["eating", "breathing", "sleeping", "working", "walking", "shopping", "studying", "cooking",
                  "cleaning", "exercising"]
        locations = ["Bucuresti"] * 10

        vectpers = [Person(random.choice(habits), loc) for loc in locations]

        homeapp = HomeAppliance("Bucuresti", 100)
        vspace = VirtualSpace(10, "Bucuresti", vectpers, homeapp, env1)
        dbcon = DBConnection("Connect1")

        reasoning1 = Reasoning(dbcon, vspace)
        reasoning1.assignDiseases()

        current_time = time.strftime("%H:%M:%S")
        print(
            f"At {current_time}, in Bucuresti with a temperature of {envTemperature} degrees and a noise level of {noiseLevel} dB, we have the following patients:")

        for i, person in enumerate(vectpers, start=1):
            print(f"Person {i} has {person.disease.name} with {person.disease.severity} severity")

        time.sleep(5)

