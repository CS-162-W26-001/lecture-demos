import days_in_month

def test_days_in_month_for_april_returns_30() -> None:
    # arrange
    month = 4
    year = 2000

    # act
    result = days_in_month.days_in_month(month, year)

    # assert
    assert result == 30

def test_days_in_month_for_february_in_leap_year() -> None:
    # arrange
    month = 2
    year = 2000

    # act
    result = days_in_month.days_in_month(month, year)

    # assert
    assert result == 29

def test_days_in_month_for_february_not_in_leap_year() -> None:
    # arrange
    month = 2
    year = 2001

    # act
    result = days_in_month.days_in_month(month, year)

    # assert
    assert result == 28

def test_december_has_31_days() -> None:
    month = 12
    year = 2001

    result = days_in_month.days_in_month(month, year)

    assert result == 31
