def calculate_flange_coupling(power, speed, service_factor):
    # Given permissible stresses
    shear_stress_shaft_bolt_key = 50  # MPa
    crushing_stress_bolt_key = 80  # MPa
    shear_stress_cast_iron = 8  # MPa

    # Handling zero speed input
    while speed == 0:
        print("Speed cannot be zero. Please enter a non-zero value.")
        speed = float(input("Enter speed (rpm): "))

    # Handling zero service factor input
    while service_factor == 0:
        print("Service factor cannot be zero. Please enter a non-zero value.")
        service_factor = float(input("Enter service factor: "))

    # Calculating torque and bending moment
    torque_Nm = (1000 * power) / (speed * (1 / 60) * service_factor)

    # Ensure positive power and service factor
    if power <= 0:
        print("Power must be a positive value. Please enter a valid power value.")
        return None
    if service_factor <= 0:
        print("Service factor must be a positive value. Please enter a valid service factor.")
        return None

    bending_moment_Nmm = torque_Nm * 1000 / 2  # Assuming evenly distributed load

    # Calculating diameter of the shaft (d) in mm
    d = ((16 * bending_moment_Nmm) / (shear_stress_shaft_bolt_key * (3.14 / 16))) ** (1 / 3)

    # Calculating number of bolts required
    num_bolts = round(2 * d / 10)

    # Calculating diameter of the bolt (db) and key (dk) in mm
    db = ((16 * torque_Nm) / (shear_stress_shaft_bolt_key * (3.14 / 4))) ** (1 / 3)
    dk = ((2 * bending_moment_Nmm) / (crushing_stress_bolt_key * (3.14 / 64))) ** (1 / 3)

    # Calculating diameter of the hub (dh) in mm
    dh = d + 2 * db

    # Calculating diameter of the flange (df) in mm
    df = 2 * dh

    return d, num_bolts, db, dk, dh, df


def main():
    print("Design a cast iron protective type flange coupling.")
    print("Enter values 10 times to calculate for different inputs.\n")

    for i in range(1, 11):
        print("Input {}:".format(i))
        power = float(input("Enter power (kW): "))
        speed = float(input("Enter speed (rpm): "))
        service_factor = float(input("Enter service factor: "))

        # Calculate the dimensions of the flange coupling
        flange_dimensions = calculate_flange_coupling(power, speed, service_factor)

        # Check for None (indicating invalid input) and skip the iteration
        if flange_dimensions is None:
            continue

        # Unpack the dimensions
        d, num_bolts, db, dk, dh, df = flange_dimensions

        # Display the dimensions of the flange coupling
        print("\nDimensions of the flange coupling:")
        print("Diameter of the shaft (d): {:.2f} mm".format(d))
        print("Number of bolts required: {}".format(num_bolts))
        print("Diameter of the bolt (db): {:.2f} mm".format(db))
        print("Width of the key (dk): {:.2f} mm".format(dk))
        print("Diameter of the hub (dh): {:.2f} mm".format(dh))
        print("Diameter of the flange (df): {:.2f} mm".format(df))
        print()


if __name__ == "__main__":
    main()
