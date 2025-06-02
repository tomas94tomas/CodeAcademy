import json

# Read the original JSON
with open("student_corrected.json", "r") as f:
    data = json.load(f)

# Modify data safely
data["age"] = 26
data["grade"] = "A"  # add grade
data.pop("hobbies", None)  # safely remove hobbies (if exists)

# Save updated data
with open("student_modified.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ student_modified.json saved.")