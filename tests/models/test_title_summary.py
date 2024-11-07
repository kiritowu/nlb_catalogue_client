import pytest

from nlb_catalogue_client.models.bib_format import BibFormat
from nlb_catalogue_client.models.book_cover import BookCover
from nlb_catalogue_client.models.title_record import TitleRecord
from nlb_catalogue_client.models.title_summary import TitleSummary
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def bib_format() -> BibFormat:
    return BibFormat(code="BK", name="BOOKS")


@pytest.fixture()
def book_cover() -> BookCover:
    return BookCover(small="small.jpg", medium="medium.jpg", large="large.jpg")


@pytest.fixture()
def title_record(bib_format) -> TitleRecord:
    return TitleRecord(format_=bib_format)


@pytest.fixture()
def title_summary_full(book_cover, title_record) -> tuple[TitleSummary, dict]:
    return TitleSummary(
        title="Sample Book / John Doe",
        native_title="样本书 / 约翰·多伊",
        series_title=["Series 1", "Series 2"],
        native_series_title=["系列 1", "系列 2"],
        author="John Doe",
        native_author="约翰·多伊",
        cover_url=book_cover,
        records=[title_record],
    ), {
        "title": "Sample Book / John Doe",
        "nativeTitle": "样本书 / 约翰·多伊",
        "seriesTitle": ["Series 1", "Series 2"],
        "nativeSeriesTitle": ["系列 1", "系列 2"],
        "author": "John Doe",
        "nativeAuthor": "约翰·多伊",
        "coverUrl": {"small": "small.jpg", "medium": "medium.jpg", "large": "large.jpg"},
        "records": [
            {
                "format": {"code": "BK", "name": "BOOKS"},
                "allowReservation": True,
                "isRestricted": False,
                "serial": False,
            }
        ],
    }


@pytest.fixture()
def title_summary_required_only() -> tuple[TitleSummary, dict]:
    return TitleSummary(), {}


@pytest.fixture()
def title_summary_with_none() -> tuple[TitleSummary, dict]:
    return TitleSummary(
        title=None,
        native_title=None,
        series_title=None,
        native_series_title=None,
        author=None,
        native_author=None,
        cover_url=UNSET,
        records=UNSET,
    ), {
        "title": None,
        "nativeTitle": None,
        "seriesTitle": None,
        "nativeSeriesTitle": None,
        "author": None,
        "nativeAuthor": None,
    }


class TestTitleSummary:
    def test_to_dict_full(self, title_summary_full):
        assert title_summary_full[0].to_dict() == title_summary_full[1]

    def test_to_dict_required_only(self, title_summary_required_only):
        assert title_summary_required_only[0].to_dict() == title_summary_required_only[1]

    def test_to_dict_with_none(self, title_summary_with_none):
        assert title_summary_with_none[0].to_dict() == title_summary_with_none[1]

    def test_from_dict_full(self, title_summary_full):
        title_summary = TitleSummary.from_dict(title_summary_full[1])
        
        assert title_summary.title == title_summary_full[0].title
        assert title_summary.native_title == title_summary_full[0].native_title
        assert title_summary.series_title == title_summary_full[0].series_title
        assert title_summary.native_series_title == title_summary_full[0].native_series_title
        assert title_summary.author == title_summary_full[0].author
        assert title_summary.native_author == title_summary_full[0].native_author
        assert isinstance(title_summary.cover_url, BookCover)
        assert title_summary.cover_url.to_dict() == title_summary_full[0].cover_url.to_dict()
        assert len(title_summary.records) == 1
        assert isinstance(title_summary.records[0], TitleRecord)
        assert title_summary.records[0].format_.code == title_summary_full[0].records[0].format_.code

    def test_from_dict_required_only(self, title_summary_required_only):
        title_summary = TitleSummary.from_dict(title_summary_required_only[1])
        
        assert title_summary.title is UNSET
        assert title_summary.native_title is UNSET
        assert title_summary.series_title is UNSET
        assert title_summary.native_series_title is UNSET
        assert title_summary.author is UNSET
        assert title_summary.native_author is UNSET
        assert title_summary.cover_url is UNSET
        assert title_summary.records == []

    def test_from_dict_with_none(self, title_summary_with_none):
        title_summary = TitleSummary.from_dict(title_summary_with_none[1])
        
        assert title_summary.title is None
        assert title_summary.native_title is None
        assert title_summary.series_title is None
        assert title_summary.native_series_title is None
        assert title_summary.author is None
        assert title_summary.native_author is None
        assert title_summary.cover_url is UNSET
        assert title_summary.records == []

    @pytest.mark.parametrize(
        "field_name,invalid_value",
        [
            ("seriesTitle", "Not a list"),
            ("nativeSeriesTitle", "Not a list"),
        ],
    )
    def test_from_dict_with_invalid_fields(self, field_name, invalid_value):
        data = {field_name: invalid_value}
        title_summary = TitleSummary.from_dict(data)
        
        field_map = {
            "seriesTitle": "series_title",
            "nativeSeriesTitle": "native_series_title",
        }
        assert getattr(title_summary, field_map[field_name]) == invalid_value
