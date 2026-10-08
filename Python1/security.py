door = {
    "status": "locked",
    "alarm": "on",
    "camera": "active",
    "light": "off",
    "code_attempts": 0
}
door.update({
    "status": "unlocked",
    "alarm": "off",
    "light": "on"
})
print(door)