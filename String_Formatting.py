# Format a table with plants and planted.
plants = input().split()
planted = input().split()
separator_char = input()

# Set print operators using string formatting on above inputs
print(f"{'Plants':^19}|{'Planted':^19}")
print("="*38)
print(f"{plants[0]:>19}|{planted[0]:>19}")
print(f"{plants[1]:>19}|{planted[1]:>19}")
print(f"{plants[2]:>19}|{planted[2]:>19}")

