import json

SystemInformation = {"OS": "NetSim", "Version": 13, "Owner": "Boson"}

with open('SystemInformation.json', 'w') as JsonFile:
	json.dump(SystemInformation, JsonFile)

with open('SystemInformation.json', 'r') as JsonFile:
	JsonString = JsonFile.read()
print(JsonString)
JsonObject = json.loads(JsonString)

print("OS: " + JsonObject["OS"])
print("Version: " + str(JsonObject["Version"]))
print("Owner: " + JsonObject ["Owner"])
