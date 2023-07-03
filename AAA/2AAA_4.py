import math

class Planet:
    def __init__(self, radius, mass, temperature):
        self.radius = radius
        self.mass = mass
        self.temperature = temperature

def find_twin_planet(accuracy, planets):
    twin_planet = None
    min_radius_diff = math.inf
    min_mass_diff = math.inf
    min_temp_diff = math.inf

    for i, planet in enumerate(planets):
        radius_diff = abs(planet.radius - planets[0].radius)
        mass_diff = abs(planet.mass - planets[0].mass)
        temp_diff = abs(planet.temperature - planets[0].temperature)

        if (radius_diff <= planets[0].radius * 0.1 and
            mass_diff <= planets[0].mass * 0.05 and
            temp_diff <= planets[0].temperature * 0.02):
            if twin_planet is None or i < twin_planet:
                twin_planet = i

    return twin_planet

def find_collision_time(accuracy, new_planet, twin_planet):
    t_start = 0
    t_end = 2 * math.pi

    while (t_end - t_start) > accuracy:
        t_mid = (t_start + t_end) / 2

        x1 = math.cos(new_planet)
        y1 = math.sin(new_planet)
        z1 = math.cos(new_planet)

        x2 = twin_planet * math.sin(t_mid)
        y2 = twin_planet * math.cos(t_mid)
        z2 = twin_planet * math.sin(t_mid)

        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

        if distance < new_planet.radius + twin_planet.radius:
            t_end = t_mid
        else:
            t_start = t_mid

    return t_end

def main():
    accuracy, n = map(float, input().split())
    n = int(n)

    planets = []

    for _ in range(n):
        radius, mass, temperature = map(float, input().split())
        planet = Planet(radius, mass, temperature)
        planets.append(planet)

    twin_planet = find_twin_planet(accuracy, planets)

    if twin_planet is None:
        print(-1)
    else:
        collision_time = find_collision_time(accuracy, planets[0], planets[twin_planet])
        print(f"{collision_time:.3f}")

if __name__ == '__main__':
    main()
