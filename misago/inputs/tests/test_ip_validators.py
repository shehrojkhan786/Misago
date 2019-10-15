import pytest

from ..errors import InputError
from ..validators import (
    validate_ipv4_address,
    validate_ipv6_address,
    validate_ipv46_address,
)


def test_ipv4_validator_raises_invalid_error_for_invalid_value():
    with pytest.raises(InputError) as excinfo:
        validate_ipv4_address("abcd")

    assert excinfo.value.code == "INVALID"


def test_ipv4_validator_raises_custom_code_error_for_invalid_value():
    with pytest.raises(InputError) as excinfo:
        validate_ipv4_address("abcd", code="CUSTOM")

    assert excinfo.value.code == "CUSTOM"


def test_ipv4_validator_raises_invalid_error_for_ipv6():
    with pytest.raises(InputError) as excinfo:
        validate_ipv4_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334")

    assert excinfo.value.code == "INVALID"


def test_ipv4_validator_allows_ipv4():
    validate_ipv4_address("127.0.0.1")


def test_ipv6_validator_raises_invalid_error_for_invalid_value():
    with pytest.raises(InputError) as excinfo:
        validate_ipv6_address("abcd")

    assert excinfo.value.code == "INVALID"


def test_ipv6_validator_raises_invalid_error_for_ipv4():
    with pytest.raises(InputError) as excinfo:
        validate_ipv6_address("127.0.0.1")

    assert excinfo.value.code == "INVALID"


def test_ipv6_validator_raises_custom_code_error_for_invalid_value():
    with pytest.raises(InputError) as excinfo:
        validate_ipv6_address("abcd", code="CUSTOM")

    assert excinfo.value.code == "CUSTOM"


def test_ipv6_validator_allows_ipv6():
    validate_ipv6_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334")


def test_ipv46_validator_raises_invalid_error_for_invalid_value():
    with pytest.raises(InputError) as excinfo:
        validate_ipv46_address("abcd")

    assert excinfo.value.code == "INVALID"


def test_ipv46_validator_raises_custom_code_error_for_invalid_value():
    with pytest.raises(InputError) as excinfo:
        validate_ipv46_address("abcd", code="CUSTOM")

    assert excinfo.value.code == "CUSTOM"


def test_ipv46_validator_allows_ipv4_value():
    validate_ipv46_address("127.0.0.1")


def test_ipv46_validator_allows_ipv6_value():
    validate_ipv46_address("2001:0db8:85a3:0000:0000:8a2e:0370:7334")