"""
services.py

Contains the service system hierarchy.

Purpose:
- Define a common service structure
- Apply abstraction through an abstract base class
- Apply inheritance
- Apply polymorphism for cost calculation
- Validate service data safely
"""

# Abstract class utilities
from abc import ABC, abstractmethod

# Custom exception
from exceptions.errors import ServiceError


class Service(ABC):
    """
    Abstract base class for all services.

    This class defines the common structure that every
    service type must implement.
    """

    def __init__(self, name, rate):
        """
        Initialize common service attributes.

        Parameters:
            name (str):
                Service name

            rate (float):
                Base price / hourly rate
        """

        # Internal protected attributes
        self._name = ""
        self._rate = 0.0

        # Use properties so validation always runs
        self.name = name
        self.rate = rate

    # ==================================================
    # NAME PROPERTY
    # ==================================================
    @property
    def name(self):
        """
        Return service name.
        """

        return self._name

    @name.setter
    def name(self, new_name):
        """
        Validate and set service name.
        """

        if not isinstance(new_name, str):
            raise ServiceError("Service name must be text.")

        cleaned_name = new_name.strip()

        if not cleaned_name:
            raise ServiceError("Service name cannot be empty.")

        if len(cleaned_name) < 2:
            raise ServiceError("Service name is too short.")

        self._name = cleaned_name

    # ==================================================
    # RATE PROPERTY
    # ==================================================
    @property
    def rate(self):
        """
        Return service rate.
        """

        return self._rate

    @rate.setter
    def rate(self, new_rate):
        """
        Validate and set service rate.
        """

        # Must be numeric
        if not isinstance(new_rate, (int, float)):
            raise ServiceError("Service rate must be numeric.")

        # Must be positive
        if new_rate <= 0:
            raise ServiceError("Service rate must be greater than zero.")

        self._rate = float(new_rate)

    # ==================================================
    # ABSTRACT METHODS
    # ==================================================
    @abstractmethod
    def calculate_cost(self, duration):
        """
        Calculate total cost.

        Must be implemented by child classes.
        """

        pass

    @abstractmethod
    def description(self):
        """
        Return readable service description.

        Must be implemented by child classes.
        """

        pass

    # ==================================================
    # STRING REPRESENTATION
    # ==================================================
    def __str__(self):
        """
        Human-readable representation.
        """

        return self.description()


# ======================================================
# ROOM RESERVATION SERVICE
# ======================================================
class RoomReservation(Service):
    """
    Service for reserving rooms.

    Cost:
        rate × duration
    """

    def calculate_cost(self, duration):
        """
        Calculate room reservation cost.
        """

        if duration <= 0:
            raise ServiceError("Duration must be greater than zero.")

        return self.rate * duration

    def description(self):
        """
        Return readable description.
        """

        return f"Room Reservation: {self.name} | Rate: ${self.rate:.2f}"


# ======================================================
# EQUIPMENT RENTAL SERVICE
# ======================================================
class EquipmentRental(Service):
    """
    Service for renting equipment.

    Includes 10% operational surcharge.
    """

    EXTRA_CHARGE = 1.10

    def calculate_cost(self, duration):
        """
        Calculate equipment rental cost.
        """

        if duration <= 0:
            raise ServiceError("Duration must be greater than zero.")

        return self.rate * duration * self.EXTRA_CHARGE

    def description(self):
        """
        Return readable description.
        """

        return f"Equipment Rental: {self.name} | Rate: ${self.rate:.2f}"


# ======================================================
# CONSULTING SERVICE
# ======================================================
class Consulting(Service):
    """
    Consulting service.

    Business rule:
    More than 5 hours → 10% discount
    """

    DISCOUNT_THRESHOLD = 5
    DISCOUNT_RATE = 0.90

    def calculate_cost(self, duration):
        """
        Calculate consulting cost.
        """

        if duration <= 0:
            raise ServiceError("Duration must be greater than zero.")

        total = self.rate * duration

        if duration > self.DISCOUNT_THRESHOLD:
            total *= self.DISCOUNT_RATE

        return total

    def description(self):
        """
        Return readable description.
        """

        return f"Consulting: {self.name} | Rate: ${self.rate:.2f}"
