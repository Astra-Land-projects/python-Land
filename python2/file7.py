with open("user_activity.txt", "r") as file:
  user_logs = file.readlines()

with open("service_status.txt", "r") as file:
  service_logs = file.readlines()

with open("system_errors.txt", "r") as file:
  system_logs = file.readlines()

logs = user_logs + system_logs + service_logs

with open("logs.txt", "a") as file:
  for info in logs:
    file.write(info)
    print(info)