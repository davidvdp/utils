import pytest

from apt_package import parse_log_for_paths


def test_parse_log_for_paths():
    parse_log_for_paths('install_log_cmake.txt')
