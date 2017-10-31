import os

class Config:
    @staticmethod
    def parse(configFilePath):
        conf = {}
        with open(configFilePath, "r") as configFile:
            for line in configFile:
                (key, value) = line.strip().split('=')
                conf[key] = value
        # print conf
        return conf
