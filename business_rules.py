# business_rules.py
# Author: Breanna Ramirez

MIN_DISCOUNT_SEATS = 10
EDUCATION_DISCOUNT_SEATS = 50

STANDARD_DISCOUNT = 0.07
EDUCATION_DISCOUNT = 0.16
NO_DISCOUNT = 0.0

ONBOARDING_FEE = 60.00
ONBOARDING_THRESHOLD = 400.00
CONTRACT_REVIEW_THRESHOLD = 5000.00
TRAINER_MIN_SEATS = 25
TRAINER_TOTAL_THRESHOLD = 3000.00


def calculate_license_cost(seat_price: float, seats: int) -> float:
    """Return the license cost before discounts"""
    return seat_price * seats


def get_seat_discount(seats: int, education: bool = False) -> float:
    """Return the discount rate based on seats and education status."""
    if seats < MIN_DISCOUNT_SEATS:
        return NO_DISCOUNT
    elif seats < EDUCATION_DISCOUNT_SEATS:
        return STANDARD_DISCOUNT
    elif education:
        return EDUCATION_DISCOUNT
    else:
        return STANDARD_DISCOUNT


def calculate_license_total(
    seat_price: float, seats: int, education: bool = False
) -> float:
    """Return the discounted license total including applicable fees."""
    cost = calculate_license_cost(seat_price, seats)
    discount = get_seat_discount(seats, education)
    discounted_cost = cost * (1 - discount)

    if discounted_cost <= ONBOARDING_THRESHOLD:
        return discounted_cost + ONBOARDING_FEE

    return discounted_cost


def needs_contract_review(total: float) -> bool:
    """Return whether a license total requires contract review"""
    return total > CONTRACT_REVIEW_THRESHOLD


def gets_trainer(seats: int, total: float) -> bool:
    """Return whether an order qualifies for a trainer."""
    return seats >= TRAINER_MIN_SEATS or total > TRAINER_TOTAL_THRESHOLD


def total_licensed(orders: list) -> float:
    """Return the combined license total for all orders."""
    total = 0.0

    for order in orders:
        total += calculate_license_total(
            order["seat_price"],
            order["seats"],
            order["education"],
        )

    return total


def largest_license(orders: list) -> str:
    """Return the company with the largest license total."""
    largest_company = ""
    largest_total = -1.0

    for order in orders:
        total = calculate_license_total(
            order["seat_price"],
            order["seats"],
            order["education"],
        )

        if total > largest_total:
            largest_total = total
            largest_company = order["company"]

    return largest_company


def format_license_line(
    company: str, total: float, contract_review: bool, trainer: bool
) -> str:
    """Return a formatted license report line."""
    review_text = "yes" if contract_review else "no"
    trainer_text = "yes" if trainer else "no"

    return (
        f"{company}: ${total:.2f} | "
        f"contract review: {review_text} | trainer: {trainer_text}"
    )
