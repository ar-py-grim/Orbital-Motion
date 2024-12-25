from vpython import *

G = 6.67e-11  # N(m^2)/(kg^2)
R_e = 6.37e6   # m
M_e = 5.97e24  # kg
omega_e = 7.3e-5  # rad/s
omega_m = 2.7e-6  # rad/s
M_m = 0.0123*M_e
R_m = 0.2725*R_e
r_me = 60*R_e

earth = sphere(radius=R_e*10, texture=textures.earth, pos=vector(0, 0, 0))
moon = sphere(radius=R_m*10, color=color.white, pos=vector(r_me, 0, 0), make_trail=True)
r = earth.pos-moon.pos
moon.velocity = vector(0, sqrt(G*M_e/mag(r)), 0)
scene.range = R_e * 100  
dt = 60  # s
velocity_label = label(pos=moon.pos, text="", xoffset=10, yoffset=10, space=30, height=12, color=color.white)


while True:

    rate(500)
    earth.rotate(angle=omega_e*dt, axis=vector(0, 1, 0), origin=earth.pos)
    moon.rotate(angle=omega_m*dt, axis=vector(0, 1, 0), origin=moon.pos)
    moon.velocity = moon.velocity + (G * M_e * dt * hat(r) / (mag(r)**2))
    speed = mag(moon.velocity)
    moon.pos += moon.velocity*dt
    velocity_label.pos = moon.pos + vector(10, 10, 0) 
    velocity_label.text = f"Velocity: {speed/1000:.4f} km/s"
    r = earth.pos-moon.pos
