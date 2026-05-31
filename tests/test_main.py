import sys
import os

sys.path.append(os.path.abspath("src"))

from main import get_project_name


def test_get_project_name():
    assert get_project_name() == "Software Engineering Lab 5"