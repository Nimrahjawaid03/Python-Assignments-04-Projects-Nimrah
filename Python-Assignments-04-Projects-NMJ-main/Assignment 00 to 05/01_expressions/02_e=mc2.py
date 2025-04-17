# program that reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy E = m * c**2

C = 299792458

def main():
    print("Reading mass from user...")
    mass_input:float = float(input("Enter mass "))
    energy_in_joules = mass_input * C ** 2
    print("e = m * C ^ 2")
    print(f"m = {mass_input} kg")
    print(f"c = {C} m/s")
    print(f"Joules_of_energy = {energy_in_joules}")
    
if __name__ == "__main__":
    main()    