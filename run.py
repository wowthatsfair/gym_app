import sys
import os

# Add the project root directory to sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.append(project_root)

# Verify sys.path
print("sys.path:", sys.path)
print("Project root:", project_root)

# Attempt to import the app
try:
    from app import app
    print("App imported successfully!")
except ImportError as e:
    print(f"Error importing app: {e}")

if __name__ == "__main__":
    app.run(debug=True)
