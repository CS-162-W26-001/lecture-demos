import is_leap_year

def test_is_leap_year() -> None:
    is_leap_year.is_leap_year(1)

def test_year_not_divisible_by_4_is_not_leap_year() -> None:
    # arrange
    year = 2001

    # act
    result = is_leap_year.is_leap_year(year)

    # assert
    assert result is False

def test_year_divisible_by_4_and_100_but_not_400_is_not_leap_year() -> None:
    # arrange
    year = 1900

    # act
    result = is_leap_year.is_leap_year(year)

    # assert
    assert result is False

