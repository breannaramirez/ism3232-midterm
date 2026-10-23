from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    get_seat_discount,
    gets_trainer,
    needs_contract_review,
)


def test_license_cost():
    assert calculate_license_cost(40.00, 5) == 200.00


def test_license_cost_zero_seats():
    assert calculate_license_cost(40.00, 0) == 0.00


def test_discount_below_ten():
    assert get_seat_discount(9) == 0.0


def test_discount_at_ten():
    assert get_seat_discount(10) == 0.07


def test_discount_at_forty_nine():
    assert get_seat_discount(49) == 0.07


def test_discount_education_at_fifty():
    assert get_seat_discount(50, True) == 0.16


def test_discount_regular_at_fifty():
    assert get_seat_discount(50, False) == 0.07


def test_license_total_with_onboarding_fee():
    assert round(calculate_license_total(40.00, 5), 2) == 260.00


def test_license_total_without_onboarding_fee():
    assert round(calculate_license_total(50.00, 20), 2) == 930.00


def test_license_total_education_discount():
    assert round(calculate_license_total(50.00, 150, True), 2) == 6300.00


def test_license_total_with_discount_and_fee():
    assert round(calculate_license_total(40.00, 10), 2) == 432.00


def test_license_total_above_fee_threshold():
    assert round(calculate_license_total(100.01, 4), 2) == 400.04


def test_license_total_exact_fee_threshold():
    assert round(calculate_license_total(100.00, 4), 2) == 460.00


def test_contract_review_below_threshold():
    assert needs_contract_review(4999.99) is False


def test_contract_review_at_threshold():
    assert needs_contract_review(5000.00) is False


def test_contract_review_above_threshold():
    assert needs_contract_review(5000.01) is True


def test_trainer_below_both_thresholds():
    assert gets_trainer(24, 3000.00) is False


def test_trainer_at_seat_threshold():
    assert gets_trainer(25, 1000.00) is True


def test_trainer_at_total_threshold():
    assert gets_trainer(10, 3000.00) is False


def test_trainer_above_total_threshold():
    assert gets_trainer(10, 3000.01) is True
