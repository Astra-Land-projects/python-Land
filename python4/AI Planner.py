# project_200_ai_planner.py

goal = input("Your goal: ").strip().lower()

if "study" in goal:
    plan = [
        "1. Split topic into small parts",
        "2. Learn basics",
        "3. Build one mini project",
        "4. Review mistakes",
    ]
elif "build" in goal:
    plan = [
        "1. Define the feature",
        "2. Choose tools",
        "3. Build MVP",
        "4. Test and improve",
    ]
else:
    plan = [
        "1. Define the target",
        "2. Make a simple plan",
        "3. Execute step by step",
        "4. Review result",
    ]

print("\nPlan:")
for item in plan:
    print(item)