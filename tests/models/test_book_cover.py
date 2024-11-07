import pytest

from nlb_catalogue_client.models.book_cover import BookCover
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def book_cover_full() -> tuple[BookCover, dict]:
    return BookCover(
        small="https://example.com/small.jpg",
        medium="https://example.com/medium.jpg",
        large="https://example.com/large.jpg",
    ), {
        "small": "https://example.com/small.jpg",
        "medium": "https://example.com/medium.jpg",
        "large": "https://example.com/large.jpg",
    }


@pytest.fixture()
def book_cover_required_only():
    return BookCover(), {}


@pytest.fixture()
def book_cover_with_none():
    return BookCover(small=None, medium=None, large=None), {"small": None, "medium": None, "large": None}


class TestBookCover:
    @pytest.mark.parametrize(
        "small,medium,large",
        [
            (
                "https://example.com/small.jpg",
                "https://example.com/medium.jpg",
                "https://example.com/large.jpg",
            ),
            (None, None, None),
            (UNSET, UNSET, UNSET),
        ],
    )
    def test_basic_initialization(self, small, medium, large):
        book_cover = BookCover(small=small, medium=medium, large=large)
        assert book_cover.small == small
        assert book_cover.medium == medium
        assert book_cover.large == large

    def test_to_dict_full(self, book_cover_full):
        assert book_cover_full[0].to_dict() == book_cover_full[1]

    def test_to_dict_required_only(self, book_cover_required_only):
        assert book_cover_required_only[0].to_dict() == book_cover_required_only[1]

    def test_to_dict_with_none(self, book_cover_with_none):
        assert book_cover_with_none[0].to_dict() == book_cover_with_none[1]

    def test_from_dict_full(self, book_cover_full):
        assert BookCover.from_dict(book_cover_full[1]) == book_cover_full[0]

    def test_from_dict_required_only(self, book_cover_required_only):
        assert BookCover.from_dict(book_cover_required_only[1]) == book_cover_required_only[0]

    def test_from_dict_with_none(self, book_cover_with_none):
        assert BookCover.from_dict(book_cover_with_none[1]) == book_cover_with_none[0]

    @pytest.mark.parametrize(
        "input_data,expected_small,expected_medium,expected_large",
        [
            (
                {"small": "https://example.com/small.jpg"},
                "https://example.com/small.jpg",
                UNSET,
                UNSET,
            ),
            (
                {"small": UNSET, "medium": UNSET, "large": UNSET},
                UNSET,
                UNSET,
                UNSET,
            ),
        ],
    )
    def test_from_dict_edge_cases(self, input_data, expected_small, expected_medium, expected_large):
        book_cover = BookCover.from_dict(input_data)
        assert book_cover.small == expected_small
        assert book_cover.medium == expected_medium
        assert book_cover.large == expected_large
