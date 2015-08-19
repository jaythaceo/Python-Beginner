"""
Calculate distances
Using longitude and latitude
"""
import math

def distance_on_unit_sphere(lat1, long1, lat2, long2):
    """Convert longitude and latitude to spherical cords"""
    degrees_to_radians = math.pi/180.0

    # phi = 90 - latituse
    phi1 = (90.0 - lat1)* degrees_to_radians
    phi1 = (90.0 - lat2)* degrees_to_radians

    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians


