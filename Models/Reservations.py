"""
reservations.py

Contains the Reservation class.

Purpose:
- Connect a customer with a selected service
- Store reservation duration
- Calculate reservation cost
- Manage reservation status
- Validate reservation data
"""

# Custom exceptions
from exceptions.errors import ReservationError

# Service validation
from models.services import Service

# Customer validation
from models.customers import Customer


class Reservation:
    """
    Represents a reservation inside the system.

    A reservation contains:
    - one customer
    - one service
    - one duration
    - one current status
    """

    # ==================================================
    # STATUS CONSTANTS
    # ==================================================
    STATUS_PENDING = "Pending"
    STATUS_CONFIRMED = "Confirmed"
    STATUS_CANCELLED = "Cancelled"

    def __init__(self, customer, service, duration):
        """
        Reservation constructor.

        Parameters:
            customer (Customer):
                Customer making reservation

            service (Service):
                Selected service

            duration (float):
                Service duration
        """

        # Initialize internal attributes
        self._customer = None
        self._service = None
        self._duration = 0
        self._status = self.STATUS_PENDING

        # Assign through properties
        # This forces validation
        self.customer = customer
        self.service = service
        self.duration = duration

    # ==================================================
    # CUSTOMER PROPERTY
    # ==================================================
    @property
    def customer(self):
        """
        Return reservation customer.
        """

        return self._customer

    @customer.setter
    def customer(self, new_customer):
        """
        Validate and assign customer.
        """

        if not isinstance(new_customer, Customer):
            raise ReservationError("Invalid customer object.")

        self._customer = new_customer

    # ==================================================
    # SERVICE PROPERTY
    # ==================================================
    @property
    def service(self):
        """
        Return selected service.
        """

        return self._service

    @service.setter
    def service(self, new_service):
        """
        Validate and assign service.
        """

        if not isinstance(new_service, Service):
            raise ReservationError("Invalid service object.")

        self._service = new_service

    # ==================================================
    # DURATION PROPERTY
    # ==================================================
    @property
    def duration(self):
        """
        Return reservation duration.
        """

        return self._duration

    @duration.setter
    def duration(self, new_duration):
        """
        Validate and assign duration.
        """

        # Must be numeric
        if not isinstance(new_duration, (int, float)):
            raise ReservationError("Duration must be numeric.")

        # Must be positive
        if new_duration <= 0:
            raise ReservationError("Duration must be greater than zero.")

        self._duration = float(new_duration)

    # ==================================================
    # STATUS PROPERTY
    # ==================================================
    @property
    def status(self):
        """
        Return reservation status.
        """

        return self._status

    # ==================================================
    # BUSINESS METHODS
    # ==================================================
    def calculate_total(self):
        """
        Calculate total reservation cost.

        Uses polymorphism:
        Each service calculates cost differently.
        """

        return self.service.calculate_cost(self.duration)

    def confirm(self):
        """
        Confirm reservation.
        """

        if self.status == self.STATUS_CANCELLED:
            raise ReservationError(
                "Cancelled reservations cannot be confirmed."
            )

        self._status = self.STATUS_CONFIRMED

    def cancel(self):
        """
        Cancel reservation.
        """

        if self.status == self.STATUS_CONFIRMED:
            raise ReservationError(
                "Confirmed reservations cannot be cancelled."
            )

        self._status = self.STATUS_CANCELLED

    # ==================================================
    # INFORMATION METHOD
    # ==================================================
    def show_info(self):
        """
        Return formatted reservation information.
        """

        total = self.calculate_total()

        return (
            f"{self.customer.show_info()} | "
            f"{self.service.description()} | "
            f"Duration: {self.duration} | "
            f"Total: ${total:.2f} | "
            f"Status: {self.status}"
        )

    # ==================================================
    # STRING REPRESENTATION
    # ==================================================
    def __str__(self):
        """
        Human-readable representation.
        """

        return self.show_info()

    def __repr__(self):
        """
        Developer-friendly representation.
        Useful for debugging.
        """

        return (
            f"Reservation("
            f"customer='{self.customer.name}', "
            f"service='{self.service.name}', "
            f"duration={self.duration}, "
            f"status='{self.status}')"
        )
