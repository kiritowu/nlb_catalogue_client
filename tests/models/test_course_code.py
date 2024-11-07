import pytest

from nlb_catalogue_client.models.course_code import CourseCode
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def course_code_full() -> tuple[CourseCode, dict]:
    return CourseCode(code="N1001", cluster_name="Lifestyle Design", category_name="Culture & Society"), {
        "code": "N1001",
        "clusterName": "Lifestyle Design",
        "categoryName": "Culture & Society",
    }


@pytest.fixture()
def course_code_required_only() -> tuple[CourseCode, dict]:
    return CourseCode(code="N1001", cluster_name="Lifestyle Design"), {
        "code": "N1001",
        "clusterName": "Lifestyle Design",
    }


@pytest.fixture()
def course_code_with_none() -> tuple[CourseCode, dict]:
    return CourseCode(code="N1001", cluster_name="Lifestyle Design", category_name=None), {
        "code": "N1001",
        "clusterName": "Lifestyle Design",
        "categoryName": None,
    }


class TestCourseCode:
    @pytest.mark.parametrize(
        "code,cluster_name,category_name",
        [
            ("N1001", "Lifestyle Design", "Culture & Society"),
            ("N1002", "Digital Design", None),
            ("N1003", "Web Design", UNSET),
        ],
    )
    def test_basic_initialization(self, code, cluster_name, category_name):
        course = CourseCode(code=code, cluster_name=cluster_name, category_name=category_name)
        assert course.code == code
        assert course.cluster_name == cluster_name
        assert course.category_name == category_name

    def test_to_dict_full(self, course_code_full):
        assert course_code_full[0].to_dict() == course_code_full[1]

    def test_to_dict_required_only(self, course_code_required_only):
        assert course_code_required_only[0].to_dict() == course_code_required_only[1]

    def test_to_dict_with_none(self, course_code_with_none):
        assert course_code_with_none[0].to_dict() == course_code_with_none[1]

    def test_from_dict_full(self, course_code_full):
        assert CourseCode.from_dict(course_code_full[1]) == course_code_full[0]

    def test_from_dict_required_only(self, course_code_required_only):
        assert CourseCode.from_dict(course_code_required_only[1]) == course_code_required_only[0]

    def test_from_dict_with_none(self, course_code_with_none):
        assert CourseCode.from_dict(course_code_with_none[1]) == course_code_with_none[0]

    @pytest.mark.parametrize(
        "input_data,expected_code,expected_cluster_name,expected_category_name",
        [
            ({"code": "N1001", "clusterName": "Lifestyle Design"}, "N1001", "Lifestyle Design", UNSET),
            (
                {"code": "N1001", "clusterName": "Lifestyle Design", "categoryName": None},
                "N1001",
                "Lifestyle Design",
                None,
            ),
            (
                {"code": "N1001", "clusterName": "Lifestyle Design", "categoryName": UNSET},
                "N1001",
                "Lifestyle Design",
                UNSET,
            ),
        ],
    )
    def test_from_dict_edge_cases(self, input_data, expected_code, expected_cluster_name, expected_category_name):
        course = CourseCode.from_dict(input_data)
        assert course.code == expected_code
        assert course.cluster_name == expected_cluster_name
        assert course.category_name == expected_category_name
