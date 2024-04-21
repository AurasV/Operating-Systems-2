import random
import time
import csv

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
    def __init__(self, id, name, status, time, habit, location):
        super().__init__(id, name, status, time)
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
    def __init__(self, id, name, status, time, location, effectLevel):
        super().__init__(id, name, status, time)
        self.location = location
        self.effectLevel = effectLevel

    def setStatus(self, new_status):
        self.status = new_status


class Environment:
    def __init__(self, temperature, humidity, illumination, noiseLevel):
        self.temperature = temperature
        self.humidity = humidity
        self.ilumination = illumination
        self.noiseLevel = noiseLevel

    def getEnvironmentInfo(self):
        return self


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
    def __init__(self, size, location, persons, appliances, environment):
        self.size = size
        self.location = location
        self.persons = persons
        self.appliances = appliances
        self.environment = environment

    def show(self):
        print("size: " + str(self.size) + "; location: " + str(self.location))

    def getEvent(self):
        return


class Reasoning(object):
    def __init__(self, dbConnection, refSmartHome, diseases_conditions):
        self.dbConnection = dbConnection
        self.refSmartHome = refSmartHome
        self.diseases_conditions = diseases_conditions

    def determineDisease(self):
        env = self.getEnvironmentInfo()
        temp = env.temperature

        possible_diseases = []
        for disease, conditions in self.diseases_conditions.items():
            if conditions['Temperature_Min'] <= temp <= conditions['Temperature_Max']:
                possible_diseases.append((disease, conditions['Severity']))

        if not possible_diseases:
            return Disease("none", "Healthy")

        selected_disease = random.choice(possible_diseases)
        return Disease(selected_disease[1], selected_disease[0])

    def assignDiseases(self):
        persons = self.refSmartHome.persons
        for person in persons:
            person.disease = self.determineDisease()

    def getEnvironmentInfo(self):
        return self.refSmartHome.environment


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


def load_disease_data(filepath):
    diseases_conditions = {}
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            diseases_conditions[row['Disease']] = {
                'Temperature_Min': int(row['Temperature_Min']),
                'Temperature_Max': int(row['Temperature_Max']),
                'Severity': row['Severity']
            }
    return diseases_conditions


if __name__ == '__main__':
    diseases_conditions = load_disease_data('diseases.csv')
    while True:
        envTemperature = random.randint(-20, 50)
        noiseLevel = random.randint(30, 80)
        env1 = Environment(envTemperature, 19, "good", noiseLevel)

        habits = ["eating", "breathing", "sleeping", "working", "walking", "shopping", "studying", "cooking", "cleaning", "exercising"]
        locations = ["Bucuresti"] * 10
        vectpers = [Person(i, f"Person {i}", "healthy", "now", habit, loc) for i, (habit, loc) in enumerate(zip(habits, locations), start=1)]

        homeapp = HomeAppliance(1, "Fridge", "Off", "now", "Bucuresti", 100)
        vspace = VirtualSpace(10, "Bucuresti", vectpers, [homeapp], env1)
        dbcon = DBConnection("Connect1")

        reasoning1 = Reasoning(dbcon, vspace, diseases_conditions)
        reasoning1.assignDiseases()

        current_time = time.strftime("%H:%M:%S")
        print(f"At {current_time}, in Bucuresti with a temperature of {envTemperature} degrees and a noise level of {noiseLevel} dB, we have the following patients:")

        for person in vectpers:
            print(f"{person.name} has {person.disease.name} with {person.disease.severity} severity")

        time.sleep(5)
