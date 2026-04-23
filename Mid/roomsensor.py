import random as r

class RoomSensor(Sensor):
    def __init__(self, name: str) -> None:
        self.name = name
    def read(self) -> float:
        return 0.0

class TemperatureSensor(Sensor):
    def __init__(self, temperature: str) -> None:
        self.temperature = temperature
    def read(self) -> float:
        return round(r.uniform(15.0, 35.0), 1)

class HumiditySensor(Sensor):
    def __init__(self, humidity: str) -> None:
        self.humidity = humidity
    def read(self) -> float:
        self.humidity = humidity
        return round(r.uniform(30.0, 80.0), 1)

class LightSensor(Sensor):
    def __init__(self, light: str) -> None:
        self.light = light
    def read(self) -> float:
        self.light = light
        return r.randint(0, 800)

    def show_info(self):
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Light: {self.light}")

    def comfort_level(self):
        if self.temperature >= 30 or self.humidity >= 70:
            return "Warning"
        elif 20 <= self.temperature <= 26 and 40 <= self.humidity <= 60:
            return "Comfortable"
        else:
            return "Normal"

    def light_status(self):
        return "Dark" if self.light < 200 else "Bright"