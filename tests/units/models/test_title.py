import pytest

from nlb_catalogue_client.models.bib_format import BibFormat
from nlb_catalogue_client.models.title import Title
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def bib_format() -> BibFormat:
    return BibFormat(code="BK", name="BOOKS")


@pytest.fixture()
def title_full(bib_format) -> tuple[Title, dict]:
    return Title(
        format_=bib_format,
        title="Sample Book",
        native_title="样本书",
        series_title=["Series 1", "Series 2"],
        native_series_title=["系列 1", "系列 2"],
        author="John Doe",
        native_author="约翰·多伊",
        other_authors=["Jane Smith", "Bob Wilson"],
        native_other_authors=["简·史密斯", "鲍勃·威尔逊"],
        language=["English", "Chinese"],
        audience=["General", "Adult"],
        audience_imda=["NC16", "PG"],
        brn=99999999,
        digital_id="overdrive123",
        other_titles=["Alternative Title 1", "Alternative Title 2"],
        native_other_titles=["其他标题 1", "其他标题 2"],
        variant_titles=["Variant 1", "Variant 2"],
        native_variant_titles=["变体 1", "变体 2"],
        isbns=["9709999999"],
        issns=["9999-9999"],
        edition=["First Edition"],
        native_edition=["第一版"],
        publisher=["Sample Publisher"],
        native_publisher=["示例出版社"],
        publish_date="2023",
        subjects=["Fiction", "Adventure"],
        physical_description=["300 pages"],
        native_physical_description=["300页"],
        summary=["A fascinating story"],
        native_summary=["一个引人入胜的故事"],
        contents=["Chapter 1", "Chapter 2"],
        native_contents=["第一章", "第二章"],
        thesis=["PhD Thesis"],
        native_thesis=["博士论文"],
        notes=["Special Edition"],
        native_notes=["特别版"],
        active_reservations_count=3,
        volume_note=["Volume 1"],
        native_volume_note=["第一卷"],
        frequency=["Monthly"],
        native_frequency=["每月"],
        credits_=["Editor: John Smith"],
        native_credits=["编辑：约翰·史密斯"],
        performers=["Actor: Jane Doe"],
        native_performers=["演员：简·多伊"],
        availability=True,
        source="Library",
        volumes=["2023 issue 1"],
    ), {
        "format": {"code": "BK", "name": "BOOKS"},
        "title": "Sample Book",
        "nativeTitle": "样本书",
        "seriesTitle": ["Series 1", "Series 2"],
        "nativeSeriesTitle": ["系列 1", "系列 2"],
        "author": "John Doe",
        "nativeAuthor": "约翰·多伊",
        "otherAuthors": ["Jane Smith", "Bob Wilson"],
        "nativeOtherAuthors": ["简·史密斯", "鲍勃·威尔逊"],
        "language": ["English", "Chinese"],
        "audience": ["General", "Adult"],
        "audienceImda": ["NC16", "PG"],
        "brn": 99999999,
        "digitalId": "overdrive123",
        "otherTitles": ["Alternative Title 1", "Alternative Title 2"],
        "nativeOtherTitles": ["其他标题 1", "其他标题 2"],
        "variantTitles": ["Variant 1", "Variant 2"],
        "nativeVariantTitles": ["变体 1", "变体 2"],
        "isbns": ["9709999999"],
        "issns": ["9999-9999"],
        "edition": ["First Edition"],
        "nativeEdition": ["第一版"],
        "publisher": ["Sample Publisher"],
        "nativePublisher": ["示例出版社"],
        "publishDate": "2023",
        "subjects": ["Fiction", "Adventure"],
        "physicalDescription": ["300 pages"],
        "nativePhysicalDescription": ["300页"],
        "summary": ["A fascinating story"],
        "nativeSummary": ["一个引人入胜的故事"],
        "contents": ["Chapter 1", "Chapter 2"],
        "nativeContents": ["第一章", "第二章"],
        "thesis": ["PhD Thesis"],
        "nativeThesis": ["博士论文"],
        "notes": ["Special Edition"],
        "nativeNotes": ["特别版"],
        "activeReservationsCount": 3,
        "volumeNote": ["Volume 1"],
        "nativeVolumeNote": ["第一卷"],
        "frequency": ["Monthly"],
        "nativeFrequency": ["每月"],
        "credits": ["Editor: John Smith"],
        "nativeCredits": ["编辑：约翰·史密斯"],
        "performers": ["Actor: Jane Doe"],
        "nativePerformers": ["演员：简·多伊"],
        "availability": True,
        "source": "Library",
        "volumes": ["2023 issue 1"],
        "allowReservation": True,
        "isRestricted": False,
        "serial": False,
    }


@pytest.fixture()
def title_required_only(bib_format) -> tuple[Title, dict]:
    return Title(format_=bib_format), {
        "format": {"code": "BK", "name": "BOOKS"},
        "allowReservation": True,
        "isRestricted": False,
        "serial": False,
    }


@pytest.fixture()
def title_with_none(bib_format) -> tuple[Title, dict]:
    return Title(
        format_=bib_format,
        title="Sample Book",
        native_title=None,
        series_title=None,
        native_series_title=None,
        native_author=None,
        other_authors=None,
        native_other_authors=None,
        audience=None,
        audience_imda=None,
        digital_id=None,
        other_titles=None,
        native_other_titles=None,
        variant_titles=None,
        native_variant_titles=None,
        issns=None,
        edition=None,
        native_edition=None,
        native_publisher=None,
        native_physical_description=None,
        summary=None,
        native_summary=None,
        contents=None,
        native_contents=None,
        thesis=None,
        native_thesis=None,
        native_notes=None,
        volume_note=None,
        native_volume_note=None,
        frequency=None,
        native_frequency=None,
        credits_=None,
        native_credits=None,
        performers=None,
        native_performers=None,
        source=None,
        volumes=None,
    ), {
        "format": {"code": "BK", "name": "BOOKS"},
        "title": "Sample Book",
        "nativeTitle": None,
        "seriesTitle": None,
        "nativeSeriesTitle": None,
        "nativeAuthor": None,
        "otherAuthors": None,
        "nativeOtherAuthors": None,
        "audience": None,
        "audienceImda": None,
        "digitalId": None,
        "otherTitles": None,
        "nativeOtherTitles": None,
        "variantTitles": None,
        "nativeVariantTitles": None,
        "issns": None,
        "edition": None,
        "nativeEdition": None,
        "nativePublisher": None,
        "nativePhysicalDescription": None,
        "summary": None,
        "nativeSummary": None,
        "contents": None,
        "nativeContents": None,
        "thesis": None,
        "nativeThesis": None,
        "nativeNotes": None,
        "volumeNote": None,
        "nativeVolumeNote": None,
        "frequency": None,
        "nativeFrequency": None,
        "credits": None,
        "nativeCredits": None,
        "performers": None,
        "nativePerformers": None,
        "source": None,
        "volumes": None,
        "allowReservation": True,
        "isRestricted": False,
        "serial": False,
    }


class TestTitle:
    def test_to_dict_full(self, title_full):
        assert title_full[0].to_dict() == title_full[1]

    def test_to_dict_required(self, title_required_only):
        assert title_required_only[0].to_dict() == title_required_only[1]

    def test_to_dict_with_none(self, title_with_none):
        """Test that to_dict correctly handles None values"""
        assert title_with_none[0].to_dict() == title_with_none[1]

    def test_from_dict_full(self, title_full):
        assert Title.from_dict(title_full[1]) == title_full[0]

    def test_from_dict_required_only(self, title_required_only):
        title = Title.from_dict(title_required_only[1])
        assert title == title_required_only[0]
        # Verify all optional fields are UNSET
        assert title.title is UNSET
        assert title.native_title is UNSET
        # ... (verify other UNSET fields)

    def test_from_dict_with_none(self, title_with_none):
        title = Title.from_dict(title_with_none[1])
        assert title == title_with_none[0]

    @pytest.mark.parametrize(
        "field_name,invalid_value",
        [
            ("seriesTitle", "Not a list"),
            ("nativeSeriesTitle", 123),
            ("otherAuthors", {"key": "value"}),
            ("nativeOtherAuthors", True),
            ("language", "Single string"),
            ("audience", 42),
            ("audienceImda", False),
            ("otherTitles", "Not a list"),
            ("nativeOtherTitles", 123),
            ("variantTitles", {"key": "value"}),
            ("nativeVariantTitles", True),
            ("isbns", "Single ISBN"),
            ("issns", 42),
            ("edition", False),
            ("nativeEdition", "Not a list"),
            ("publisher", 123),
            ("nativePublisher", {"key": "value"}),
            ("subjects", True),
            ("physicalDescription", "Not a list"),
            ("nativePhysicalDescription", 123),
            ("summary", {"key": "value"}),
            ("nativeSummary", True),
            ("contents", "Not a list"),
            ("nativeContents", 42),
            ("thesis", False),
            ("nativeThesis", "Not a list"),
            ("notes", 123),
            ("nativeNotes", {"key": "value"}),
            ("volumeNote", True),
            ("nativeVolumeNote", "Not a list"),
            ("frequency", 42),
            ("nativeFrequency", False),
            ("credits", "Not a list"),
            ("nativeCredits", 123),
            ("performers", {"key": "value"}),
            ("nativePerformers", True),
            ("volumes", "Not a list"),
        ],
    )
    def test_from_dict_with_invalid_list_fields(self, bib_format, field_name, invalid_value):
        data = {"format": {"code": "BK", "name": "BOOKS"}, "title": "Sample Book", field_name: invalid_value}
        title = Title.from_dict(data)
        if field_name == "credits":
            assert title.credits_ == invalid_value
            return
        assert getattr(title, self._to_python_name(field_name)) == invalid_value

    @staticmethod
    def _to_python_name(camel_case: str) -> str:
        """Convert camelCase to snake_case"""
        import re

        name = re.sub("([A-Z]+)", r"_\1", camel_case).lower()
        if name.startswith("_"):
            name = name[1:]
        return name
