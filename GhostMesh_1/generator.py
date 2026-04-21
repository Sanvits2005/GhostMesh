import random

attack_memory = {
    "Port Scan": 1,
    "Login Flood": 1,
    "Data Exfiltration": 1,
    "DDoS": 1
}

def generate_attack():
    attack = random.choices(
        list(attack_memory.keys()),
        weights=attack_memory.values()
    )[0]

    if attack == "Port Scan":
        data = [random.randint(80, 120), random.randint(1, 10), random.randint(1, 5)]
    elif attack == "Login Flood":
        data = [random.randint(100, 200), random.randint(50, 100), random.randint(1, 10)]
    elif attack == "Data Exfiltration":
        data = [random.randint(200, 300), random.randint(10, 20), random.randint(50, 100)]
    else:
        data = [random.randint(300, 500), random.randint(100, 200), random.randint(10, 20)]

    return attack, data

def update_attacker(attack, success):
    if success:
        attack_memory[attack] += 2
    else:
        attack_memory[attack] = max(1, attack_memory[attack] - 1)