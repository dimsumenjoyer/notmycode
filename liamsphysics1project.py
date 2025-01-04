import math
import random
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as mcolors
import numpy as np
import seaborn as sns

class i:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class body:
    def __init__(self, location, mass, velocity, name = ""):
        self.location = location
        self.mass = mass
        self.velocity = velocity
        self.name = name


#Calculating the acceleration of any given body from the equation for gravitational force 
def calculate_single_body_acceleration(bodies, body_list):
    G = 6.67408e-11 
    acceleration = i(0,0,0)

    Current_Body = bodies[body_list]
    for list, Other_Mass in enumerate(bodies):
        if list != body_list:
            r = (Current_Body.location.x - Other_Mass.location.x)**2 + (Current_Body.location.y - Other_Mass.location.y)**2 + (Current_Body.location.z - Other_Mass.location.z)**2
            r = math.sqrt(r)
            g = G * Other_Mass.mass / r**3
            acceleration.x += g * (Other_Mass.location.x - Current_Body.location.x)
            acceleration.y += g * (Other_Mass.location.y - Current_Body.location.y)
            acceleration.z += g * (Other_Mass.location.z - Current_Body.location.z)
    return acceleration


#Calculating the velocity at any given time from the acceleration and updating the velocity so that it can be used again later.
def Vel_calc(bodies, dt = 1):
    for body_list, Current_Body in enumerate(bodies):

        acceleration = calculate_single_body_acceleration(bodies, body_list)

        Current_Body.velocity.x += acceleration.x * dt
        Current_Body.velocity.y += acceleration.y * dt
        Current_Body.velocity.z += acceleration.z * dt 


#getting the location from the velocity and change in time
def update_location(bodies, dt = 1):
    for Current_Body in bodies:

        Current_Body.location.x += Current_Body.velocity.x * dt
        Current_Body.location.y += Current_Body.velocity.y * dt
        Current_Body.location.z += Current_Body.velocity.z * dt

def compute_gravity_step(bodies, dt = 1):
    Vel_calc(bodies, dt = dt)
    update_location(bodies, dt = dt)

#moving the planets in steps such that every "step" is a moment in time.
def run_simulation(bodies, names = None, dt = 10, number_of_steps = 10000, report_freq = 100):

    #create output container for each body
    body_locations_hist = []
    for Current_Body in bodies:
        body_locations_hist.append({"x":[], "y":[], "z":[], "name":Current_Body.name})
        
    for i in range(1,number_of_steps):
        
        compute_gravity_step(bodies, dt = 1000)            
        
        if i % report_freq == 0:

            for list, body_location in enumerate(body_locations_hist):
                body_location["x"].append(bodies[list].location.x)
                body_location["y"].append(bodies[list].location.y)           
                body_location["z"].append(bodies[list].location.z)       

    return body_locations_hist 


#Creating a color palette to work from

plot.style.use("seaborn")
palette = sns.color_palette("rainbow",100)

#Creating the Actual space that the planets are moving in and assigning colors to the paths
def plot_output(bodies, outfile = None):
    fig = plot.figure()
    colours = [palette]

    ax = fig.add_subplot(1,1,1, projection='3d')
    max_range = 0
    

    for Current_Body in bodies: 
        max_dim = max(max(Current_Body["x"]),max(Current_Body["y"]),max(Current_Body["z"]))
        if max_dim > max_range:
            max_range = max_dim
        ax.plot(Current_Body["x"], Current_Body["y"], Current_Body["z"], c = random.choice(palette), label = Current_Body["name"])        
    
    ax.set_xlim([-max_range,max_range])    

    ax.set_ylim([-max_range,max_range])
    
    ax.set_zlim([-max_range,max_range])

    ax.legend()


#planets in the solar system
#Mass is in kg 
#location is in km

# Name of object = { location in (x,y,z), mass, initial velocity of mass in (x,y,z)}
sun = {"location":i(0,0,0), "mass":2e30, "velocity":i(0,0,0)}

mercury = {"location":i(0,5.7e10,0), "mass":3.285e23, "velocity":i(47000,0,0)}

venus = {"location":i(0,1.1e11,0), "mass":4.8e24, "velocity":i(35000,0,0)}

earth = {"location":i(0,1.5e11,0), "mass":6e24, "velocity":i(30000,0,0)}

mars = {"location":i(0,2.2e11,0), "mass":2.4e24, "velocity":i(24000,0,0)}

jupiter = {"location":i(0,7.7e11,0), "mass":1e28, "velocity":i(13000,0,0)}

saturn = {"location":i(0,1.4e12,0), "mass":5.7e26, "velocity":i(9000,0,0)}

uranus = {"location":i(0,2.8e12,0), "mass":8.7e25, "velocity":i(6835,0,0)}

neptune = {"location":i(0,4.5e12,0), "mass":1e26, "velocity":i(5477,0,0)}

pluto = {"location":i(0,3.7e12,0), "mass":1.3e22, "velocity":i(4748,0,0)}

planet_X = {"location":i(0,2.0e11,2.0e10), "mass":9e24, "velocity":i(30000,5000,1000)}
planet_y = {"location":i(0,1.5e11,2.0e11), "mass":6e26, "velocity":i(30000,0,10000)}

  #build list of planets in the simulation, or create your own
if __name__ == "__main__":
    bodies = [
        body( location = sun["location"], mass = sun["mass"], velocity = sun["velocity"], name = "Sun"),
        body( location = earth["location"], mass = earth["mass"], velocity = earth["velocity"], name = "Earth"),
        body( location = mars["location"], mass = mars["mass"], velocity = mars["velocity"], name = "Mars"),
        body( location = venus["location"], mass = venus["mass"], velocity = venus["velocity"], name = "Venus"),
        body( location = jupiter["location"], mass = jupiter["mass"], velocity = jupiter["velocity"], name = "jupiter"),
        body( location = uranus["location"], mass = uranus["mass"], velocity = uranus["velocity"], name = "uranus"),
        body( location = planet_X["location"], mass = planet_X["mass"], velocity = planet_X["velocity"], name = "Caladan"),
        body( location = planet_y["location"], mass = planet_y["mass"], velocity = planet_y["velocity"], name = "Krypton"),
        ]

    motions = run_simulation(bodies, dt = 100, number_of_steps = 480000, report_freq = 1000)
    plot_output(motions, outfile = 'orbits.png')



plot.show()