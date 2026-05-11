"""
errors.py

This module contains custom exception classes used throughout the system.

Purpose:
- Improve error readability
- Separate business logic errors from Python built-in exceptions
- Make debugging easier
- Allow more specific exception handling
"""


class CustomerError(Exception):
    """
    Exception raised for errors related to customer operations.

    Examples:
    - Empty customer name
    - Invalid email format
    - Invalid customer update
    """

    def __init__(self, message="Customer operation error"):
        """
        Initialize exception with custom message.
        """
        self.message = message
        super().__init__(self.message)


class ReservationError(Exception):
    """
    Exception raised for errors related to reservations.

    Examples:
    - Invalid duration
    - No available customers
    - No available services
    - Invalid reservation selection
    """

    def __init__(self, message="Reservation operation error"):
        """
        Initialize exception with custom message.
        """
        self.message = message
        super().__init__(self.message)


class ServiceError(Exception):
    """
    Exception raised for errors related to service creation
    or service validation.

    Examples:
    - Negative price
    - Empty service name
    - Invalid service type
    """

    def __init__(self, message="Service operation error"):
        """
        Initialize exception with custom message.
        """
        self.message = message
        super().__init__(self.message)
