import numpy as np

a_1 = 5.25
a_2 = 11.80
a_3 = 7.0
a_4 = 5.25

def deg(theta):
    return theta * (180/np.pi)

def check_validity(x, y, z, a_1, a_2, a_3, a_4):
    
    limited_distance = np.sqrt(x**2 + y**2 + z**2)
    print(limited_distance)
    if limited_distance < 11.80:
        print("too small")
    if limited_distance > 18.80:
        print("too big")
    else:
        print("just right")

def InverseKinematics4DOF(x, y, z, a_1, a_2, a_3, a_4):
    limited_distance = np.sqrt(x**2 + y**2 + z**2)
    if limited_distance < 11.80:
        raise Exception('Distance is too small for range')
        
    theta_1_rad = np.arctan2(y, x) #1
    theta_1 = deg(theta_1_rad)
    
    r_1 = np.sqrt(y**2 + x**2) #2
    
    r_3 = z - a_1 #3
    
    r_2 = np.sqrt(r_3**2 + r_1**2) #4
    
    B_rad = np.arctan2(r_3, r_1) #5
    B = deg(B_rad)
    
    l = r_2 ** 2 - a_2 ** 2 - a_3 ** 2
    k = - 2 * a_2 * a_3 
    a_rad = np.arccos( l / k ) #6
    a = deg(a_rad)
    
    
    theta_3_rad = -(np.pi - a_rad) #7
    theta_3_rad__ = -1 * theta_3_rad #8
    theta_3 = deg(theta_3_rad)
    
    o = a_3 * np.sin(theta_3_rad__)
    p = (a_3 * np.cos(theta_3_rad__)) + a_2
    phi_rad = np.arctan2(o, p) #9
    phi = deg(phi_rad)
    
    
    theta_2_rad = phi_rad + B_rad #10
    theta_2 = deg(theta_2_rad)
    
    return theta_1, theta_2, theta_3

while True:
    x = int(input("set x-coordinate "))
    y = int(input("set y-coordinate "))
    z = int(input("set z-coordinate "))

    check_validity(x, y, z, a_1, a_2, a_3, a_4)
    theta_1, theta_2, theta_3 = InverseKinematics4DOF(x, y, z, a_1, a_2, a_3, a_4)

    print(f"""theta 1: {theta_1}
    theta_2: {theta_2}
    theta_3: {theta_3}""")
