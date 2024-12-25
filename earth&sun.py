# from vpython import *
# import math

# G = 6.67e-11  # N(m^2)/(kg^2)
# R_e = 6.37e6  # m
# M_e = 5.97e24  # kg
# M_s = 332900 * M_e  # kg
# R_s = 109 * R_e  # m
# omega_s = 3e-6  # rad/s
# omega_e = 7.3e-5  # rad/s
# a = 149.6e9  # semi-major axis (m)
# # eccentricity = 0.5  # testing orbital mechanics for elliptical orbits
# eccentricity = 0.0167086

# sun = sphere(radius=R_s*10, color=color.yellow, pos=vector(0, 0, 0))
# r = a * (1 - eccentricity)
# earth = sphere(radius=R_e*1000, texture=textures.earth, pos=vector(r, 0, 0), make_trail=True)
# v_perihelion = math.sqrt(G * M_s * (1 + eccentricity) / r)
# earth.velocity = vector(0, v_perihelion, 0)
# velocity_label = label(pos=earth.pos, text="", xoffset=10, yoffset=10, space=30, height=12, color=color.white)
# distance_label = label(pos=earth.pos/2, text="", xoffset=10, yoffset=10, space=30, height=12, color=color.white)

# dt = 3600  # s
# theta = 0  # rad

# while True:

#     rate(250)

#     r = a * (1 - eccentricity**2) / (1 + eccentricity * cos(theta))
#     speed = math.sqrt(G * M_s * (2 / r - 1 / a))
#     omega = speed / r 
#     dtheta = omega * dt 

#     x = r * cos(theta)
#     y = r * sin(theta) 
#     earth.pos = vector(x, y, 0)
#     direction = vector(-sin(theta), cos(theta), 0) 
#     earth.velocity = direction * speed 
#     sun.rotate(angle=omega_s*dt, axis=vector(0, 1, 0), origin=sun.pos)
#     earth.rotate(angle=omega_e*dt, axis=vector(0, 1, 0), origin=earth.pos)

#     velocity_label.pos = earth.pos + vector(1e10, 1e10, 0) 
#     velocity_label.text = f"Velocity: {speed/1000:.4f} km/s" 
#     distance_label.pos = earth.pos/2 + vector(1e10, 1e10, 0) 
#     distance_label.text = f"Distance: {mag(earth.pos)/10**9:.4f} million km"

#     theta += dtheta


from vpython import *
import math

G = 6.67e-11  # N(m^2)/(kg^2)
R_e = 6.37e6  # m
M_e = 5.97e24  # kg
M_s = 332900 * M_e  # kg
R_s = 109 * R_e  # m
omega_s = 3e-6  # rad/s
omega_e = 7.3e-5  # rad/s
a = 149.6e9  # semi-major axis (m)
eccentricity = 0.0167086

sun = sphere(radius=R_s*10, color=color.yellow, pos=vector(0, 0, 0))
r = a * (1 - eccentricity)
earth = sphere(radius=R_e*1000, texture=textures.earth, pos=vector(r, 0, 0), make_trail=True)
v_perihelion = math.sqrt(G * M_s * (1 + eccentricity) / r)
earth.velocity = vector(0, v_perihelion, 0)

velocity_label = label(pos=earth.pos, text="", xoffset=10, yoffset=10, space=30, height=12, color=color.white)
distance_label = label(pos=earth.pos, text="", xoffset=10, yoffset=-10, space=30, height=12, color=color.white)

scene.range = R_s * 200 

dt = 3600  # s
theta = 0  # rad

while True:
    rate(250)

    r = a * (1 - eccentricity**2) / (1 + eccentricity * cos(theta))
    speed = math.sqrt(G * M_s * (2 / r - 1 / a))
    omega = speed / r 
    dtheta = omega * dt 

    x = r * cos(theta)
    y = r * sin(theta) 
    earth.pos = vector(x, y, 0)
    direction = vector(-sin(theta), cos(theta), 0) 
    earth.velocity = direction * speed 
    sun.rotate(angle=omega_s*dt, axis=vector(0, 1, 0), origin=sun.pos)
    earth.rotate(angle=omega_e*dt, axis=vector(0, 1, 0), origin=earth.pos)

    velocity_label.pos = earth.pos + vector(1e10, 1e10, 0) 
    velocity_label.text = f"Velocity: {speed/1000:.4f} km/s" 
    distance_label.pos = earth.pos + vector(1e10, 1e10, 0) 
    distance_label.text = f"Distacne: {mag(earth.pos)/10**9:.4f} million km" 

    theta += dtheta
