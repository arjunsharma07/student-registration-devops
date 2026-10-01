import os

# Check whether index.html exists
assert os.path.exists("index.html"), "index.html does not exist"

# Read HTML file
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read().lower()

# Required elements
required_elements = [
    "<form",
    'name="name"',
    'type="email"',
    'type="tel"',
    'type="date"',
    'name="course"',
    "<button"
]

# Test every required element
for element in required_elements:
    assert element in html, f"Missing element: {element}"

print("All tests passed!")