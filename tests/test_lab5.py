import sys
import os

sys.path.append(os.path.abspath("src"))

from main import get_project_name

def test_project_name_not_empty():
    assert get_project_name() != ""

def test_project_name_type():
    assert isinstance(get_project_name(), str)

def test_project_name_value():
    assert get_project_name() == "Software Engineering Lab 5"

def test_project_name_contains_lab():
    assert "Lab" in get_project_name()

def test_project_name_length():
    assert len(get_project_name()) > 5