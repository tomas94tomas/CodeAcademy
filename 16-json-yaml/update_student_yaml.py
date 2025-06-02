import yaml

# Load YAML file
with open("student_corrected.yaml", "r") as f:
    data = yaml.safe_load(f)

# Modify data
data["age"] = 26
data["grade"] = "A"
data.pop("hobbies", None)

# Save updated YAML
with open("student_modified.yaml", "w") as f:
    yaml.dump(data, f)

print("✅ student_modified.yaml saved.")
