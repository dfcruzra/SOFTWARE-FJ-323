"""
main.py

Main entry point of the Software FJ reservation system.

Purpose:
- Run the application
- Manage customers
- Manage services
- Manage reservations
- Handle user interaction
- Demonstrate exception handling
"""

# ==================================================
# IMPORTS
# ==================================================

# Models
from models.customers import Customer
from models.services import (
    RoomReservation,
    EquipmentRental,
    Consulting
)
from models.reservations import Reservation

# Custom exceptions
from exceptions.errors import (
    CustomerError,
    ReservationError,
    ServiceError
)

# Logger utility
from utils.logger import register_log


# ==================================================
# IN-MEMORY STORAGE
# ==================================================
# These lists simulate a small database.
# For this academic project, persistent storage is
# not required.

customers = []
services = []
reservations = []


# =================================================
# MENU
# =================================================
def show_menu():
    """
    Display main menu options.
    """

    print("\n" + "=" * 45)
    print(" SOFTWARE FJ MANAGEMENT SYSTEM - GROUP 323")
    print("=" * 45)
    print("1. Register customer")
    print("2. Create service")
    print("3. Create reservation")
    print("4. View reservations")
    print("5. Exit")
    print("=" * 45)


# =================================================
# REGISTER CUSTOMER
# =================================================
def register_customer():
    """
    Register a new customer.

    Handles:
    - Name validation
    - Email validation
    - Logging on failure
    """

    try:
        print("\n--- Register Customer ---")

        name = input("Enter customer name: ").strip()
        email = input("Enter customer email: ").strip()

        customer = Customer(
            entity_id=len(customers) + 1,
            name=name,
            email=email
        )

        customers.append(customer)

    except CustomerError as error:
        print(f"\nERROR: {error}")
        register_log(error)

    except Exception as error:
        print(f"\nUnexpected error: {error}")
        register_log(error)

    else:
        print("\nCustomer registered successfully.")

    finally:
        print("Customer process completed.\n")


# ==================================================
# CREATE SERVICE
# ==================================================
def create_service():
    """
    Create a service object.

    Available services:
    - Room Reservation
    - Equipment Rental
    - Consulting
    """

    try:
        print("\n--- Create Service ---")
        print("1. Room Reservation")
        print("2. Equipment Rental")
        print("3. Consulting")

        option = input("Choose service type: ").strip()
        name = input("Enter service name: ").strip()

        try:
            rate = float(input("Enter hourly/base rate: "))
        except ValueError:
            raise ServiceError("Rate must be numeric.")

        if option == "1":
            service = RoomReservation(name, rate)

        elif option == "2":
            service = EquipmentRental(name, rate)

        elif option == "3":
            service = Consulting(name, rate)

        else:
            raise ServiceError("Invalid service type selected.")

        services.append(service)

    except ServiceError as error:
        print(f"\nERROR: {error}")
        register_log(error)

    except Exception as error:
        print(f"\nUnexpected error: {error}")
        register_log(error)

    else:
        print("\nService created successfully.")

    finally:
        print("Service process completed.\n")


# ==================================================
# CREATE RESERVATION
# ==================================================
def create_reservation():
    """
    Create a reservation.

    Flow:
    - Select customer
    - Select service
    - Enter duration
    - Calculate total
    - Confirm reservation
    """

    try:
        # Validate available customers
        if not customers:
            raise ReservationError(
                "No customers available. Register one first."
            )

        # Validate available services
        if not services:
            raise ReservationError(
                "No services available. Create one first."
            )

        print("\n--- Create Reservation ---")

        # --------------------------
        # Show customers
        # --------------------------
        print("\nAvailable Customers:")
        for index, customer in enumerate(customers, start=1):
            print(f"{index}. {customer.show_info()}")

        try:
            customer_index = (
                int(input("Select customer number: ")) - 1
            )
            selected_customer = customers[customer_index]
        except (ValueError, IndexError):
            raise ReservationError("Invalid customer selection.")

        # --------------------------
        # Show services
        # --------------------------
        print("\nAvailable Services:")
        for index, service in enumerate(services, start=1):
            print(f"{index}. {service.description()}")

        try:
            service_index = (
                int(input("Select service number: ")) - 1
            )
            selected_service = services[service_index]
        except (ValueError, IndexError):
            raise ReservationError("Invalid service selection.")

        # --------------------------
        # Duration
        # --------------------------
        try:
            duration = float(
                input("Enter duration (hours): ")
            )
        except ValueError:
            raise ReservationError("Duration must be numeric.")

        # --------------------------
        # Create reservation
        # --------------------------
        reservation = Reservation(
            customer=selected_customer,
            service=selected_service,
            duration=duration
        )

        total = reservation.calculate_total()

        reservation.confirm()

        reservations.append(reservation)

    except ReservationError as error:
        print(f"\nERROR: {error}")
        register_log(error)

    except Exception as error:
        print(f"\nUnexpected error: {error}")
        register_log(error)

    else:
        print("\nReservation created successfully.")
        print(f"Total price: ${total:.2f}")

    finally:
        print("Reservation process completed.\n")


# ==================================================
# VIEW RESERVATIONS
# ==================================================
def view_reservations():
    """
    Display all reservations.
    """

    try:
        if not reservations:
            raise ReservationError(
                "There are no reservations registered."
            )

        print("\n--- Reservation List ---")

        for index, reservation in enumerate(
            reservations,
            start=1
        ):
            print(f"{index}. {reservation.show_info()}")

    except ReservationError as error:
        print(f"\nWARNING: {error}")
        register_log(error)

    except Exception as error:
        print(f"\nUnexpected error: {error}")
        register_log(error)


# ==================================================
# AUTOMATIC SIMULATION
# ==================================================
def simulation():
    """
    Automatic simulation required for testing.

    Includes:
    - Valid operations
    - Invalid operations
    - Exception generation
    - Log creation
    """

    print("\nRunning initial simulation...")

    try:
        # Valid customer
        customer = Customer(
            1,
            "Ana",
            "ana@gmail.com"
        )
        customers.append(customer)

        # Invalid customer
        try:
            Customer(2, "", "bademail")
        except CustomerError as error:
            register_log(error)

        # Valid services
        services.append(
            RoomReservation("Basic Room", 100)
        )

        services.append(
            EquipmentRental("Projector", 50)
        )

        services.append(
            Consulting("Business Consulting", 200)
        )

        # Valid reservation
        reservation = Reservation(
            customer,
            services[0],
            2
        )
        reservation.confirm()
        reservations.append(reservation)

        # Invalid reservation
        try:
            Reservation(customer, services[1], -5)
        except ReservationError as error:
            register_log(error)

    except Exception as error:
        register_log(error)

    print("Simulation completed.\n")


# ==================================================
# MAIN PROGRAM LOOP
# ==================================================
def main():
    """
    Main application loop.
    """

    # Run automatic simulation first
    simulation()

    while True:
        show_menu()

        option = input("Select option: ").strip()

        try:
            if option == "1":
                register_customer()

            elif option == "2":
                create_service()

            elif option == "3":
                create_reservation()

            elif option == "4":
                view_reservations()

            elif option == "5":
                print("\nClosing system...")
                break

            else:
                raise ValueError("Invalid menu option.")

        except ValueError as error:
            print(f"\nERROR: {error}")
            register_log(error)

        except Exception as error:
            print(f"\nUnexpected error: {error}")
            register_log(error)


# ==================================================
# PROGRAM START
# ==================================================
if __name__ == "__main__":
    main()
