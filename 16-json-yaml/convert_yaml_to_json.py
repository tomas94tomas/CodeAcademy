import yaml
import json

# Load YAML file
with open("student_modified.yaml", "r") as yaml_file:
    data = yaml.safe_load(yaml_file)

# Save as JSON
with open("student_final.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

print("✅ YAML converted to student_final.json")
