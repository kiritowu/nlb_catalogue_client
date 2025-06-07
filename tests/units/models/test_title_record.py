import pytest

from nlb_catalogue_client.models.bib_format import BibFormat
from nlb_catalogue_client.models.title_record import TitleRecord
from nlb_catalogue_client.types import UNSET


@pytest.fixture()
def bib_format() -> BibFormat:
    return BibFormat(code="BK", name="BOOKS")


@pytest.fixture()
def title_record_full(bib_format) -> tuple[TitleRecord, dict]:
    return TitleRecord(
        format_=bib_format,
        brn=99999999,
        digital_id="overdrive123",
        other_titles=["Alternative Title 1"],
        native_other_titles=["其他标题 1"],
        variant_titles=["Variant 1"],
        native_variant_titles=["变体 1"],
        other_authors=["Jane Smith"],
        native_other_authors=["简·史密斯"],
        isbns=["9709999999"],
        issns=["9999-9999"],
        edition=["First Edition"],
        native_edition=["第一版"],
        publisher=["Sample Publisher"],
        native_publisher=["示例出版社"],
        publish_date="2023",
        subjects=["Fiction"],
        physical_description=["300 pages"],
        native_physical_description=["300页"],
        summary=["A story"],
        native_summary=["故事"],
        contents=["Chapter 1"],
        native_contents=["第一章"],
        thesis=["PhD Thesis"],
        native_thesis=["博士论文"],
        notes=["Special Edition"],
        native_notes=["特别版"],
        active_reservations_count=3,
        volume_note=["Volume 1"],
        native_volume_note=["第一卷"],
        frequency=["Monthly"],
        native_frequency=["每月"],
        credits_=["Editor: John"],
        native_credits=["编辑：约翰"],
        performers=["Actor: Jane"],
        native_performers=["演员：简"],
        availability=True,
        source="Library",
        volumes=["2023 issue 1"],
        audience=["General", "Adult"],
        audience_imda=["NC16", "PG"],
        language=["English", "Chinese"],
    ), {
        "format": {"code": "BK", "name": "BOOKS"},
        "brn": 99999999,
        "digitalId": "overdrive123",
        "otherTitles": ["Alternative Title 1"],
        "nativeOtherTitles": ["其他标题 1"],
        "variantTitles": ["Variant 1"],
        "nativeVariantTitles": ["变体 1"],
        "otherAuthors": ["Jane Smith"],
        "nativeOtherAuthors": ["简·史密斯"],
        "isbns": ["9709999999"],
        "issns": ["9999-9999"],
        "edition": ["First Edition"],
        "nativeEdition": ["第一版"],
        "publisher": ["Sample Publisher"],
        "nativePublisher": ["示例出版社"],
        "publishDate": "2023",
        "subjects": ["Fiction"],
        "physicalDescription": ["300 pages"],
        "nativePhysicalDescription": ["300页"],
        "summary": ["A story"],
        "nativeSummary": ["故事"],
        "contents": ["Chapter 1"],
        "nativeContents": ["第一章"],
        "thesis": ["PhD Thesis"],
        "nativeThesis": ["博士论文"],
        "notes": ["Special Edition"],
        "nativeNotes": ["特别版"],
        "activeReservationsCount": 3,
        "volumeNote": ["Volume 1"],
        "nativeVolumeNote": ["第一卷"],
        "frequency": ["Monthly"],
        "nativeFrequency": ["每月"],
        "credits": ["Editor: John"],
        "nativeCredits": ["编辑：约翰"],
        "performers": ["Actor: Jane"],
        "nativePerformers": ["演员：简"],
        "availability": True,
        "source": "Library",
        "volumes": ["2023 issue 1"],
        "allowReservation": True,
        "isRestricted": False,
        "serial": False,
        "audience": ["General", "Adult"],
        "audienceImda": ["NC16", "PG"],
        "language": ["English", "Chinese"],
    }


@pytest.fixture()
def title_record_required_only(bib_format) -> tuple[TitleRecord, dict]:
    return TitleRecord(format_=bib_format), {
        "format": {"code": "BK", "name": "BOOKS"},
        "allowReservation": True,
        "isRestricted": False,
        "serial": False,
    }


@pytest.fixture()
def title_record_with_none(bib_format) -> tuple[TitleRecord, dict]:
    return TitleRecord(
        format_=bib_format,
        digital_id=None,
        other_titles=None,
        native_other_titles=None,
        variant_titles=None,
        native_variant_titles=None,
        other_authors=None,
        native_other_authors=None,
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
        audience=None,
        audience_imda=None,
    ), {
        "format": {"code": "BK", "name": "BOOKS"},
        "digitalId": None,
        "otherTitles": None,
        "nativeOtherTitles": None,
        "variantTitles": None,
        "nativeVariantTitles": None,
        "otherAuthors": None,
        "nativeOtherAuthors": None,
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
        "audience": None,
        "audienceImda": None,
    }


class TestTitleRecord:
    def test_to_dict_full(self, title_record_full):
        assert title_record_full[0].to_dict() == title_record_full[1]

    def test_to_dict_required_only(self, title_record_required_only):
        assert title_record_required_only[0].to_dict() == title_record_required_only[1]

    def test_to_dict_with_none(self, title_record_with_none):
        assert title_record_with_none[0].to_dict() == title_record_with_none[1]

    def test_from_dict_full(self, title_record_full):
        assert TitleRecord.from_dict(title_record_full[1]) == title_record_full[0]

    def test_from_dict_required_only(self, title_record_required_only):
        title_record = TitleRecord.from_dict(title_record_required_only[1])
        assert title_record == title_record_required_only[0]
        # Verify all optional fields are UNSET
        assert title_record.brn is UNSET
        assert title_record.digital_id is UNSET
        # ... (verify other UNSET fields)

    def test_from_dict_with_none(self, title_record_with_none):
        title_record = TitleRecord.from_dict(title_record_with_none[1])
        assert title_record == title_record_with_none[0]

    @pytest.mark.parametrize(
        "field_name,invalid_value",
        [
            ("otherTitles", "Not a list"),
            ("nativeOtherTitles", 123),
            ("variantTitles", {"key": "value"}),
            ("nativeVariantTitles", True),
            ("otherAuthors", "Not a list"),
            ("nativeOtherAuthors", 456),
            ("isbns", {"key": "value"}),
            ("issns", True),
            ("edition", "Not a list"),
            ("nativeEdition", 789),
            ("publisher", {"key": "value"}),
            ("nativePublisher", True),
            ("subjects", "Not a list"),
            ("physicalDescription", 101),
            ("nativePhysicalDescription", {"key": "value"}),
            ("summary", True),
            ("nativeSummary", "Not a list"),
            ("contents", 102),
            ("nativeContents", {"key": "value"}),
            ("thesis", True),
            ("nativeThesis", "Not a list"),
            ("notes", 103),
            ("nativeNotes", {"key": "value"}),
            ("volumeNote", True),
            ("nativeVolumeNote", "Not a list"),
            ("frequency", 104),
            ("nativeFrequency", {"key": "value"}),
            ("credits", True),
            ("nativeCredits", "Not a list"),
            ("performers", 105),
            ("nativePerformers", {"key": "value"}),
            ("volumes", True),
            ("audience", {"key": "value"}),
            ("audienceImda", "Not a list"),
            ("language", {"key": "value"}),
        ],
    )
    def test_from_dict_with_invalid_list_fields(self, bib_format, field_name, invalid_value):
        data = {"format": {"code": "BK", "name": "BOOKS"}, field_name: invalid_value}
        title_record = TitleRecord.from_dict(data)
        if field_name == "credits":
            assert title_record.credits_ == invalid_value
            return
        assert getattr(title_record, self._to_python_name(field_name)) == invalid_value

    @staticmethod
    def _to_python_name(camel_case: str) -> str:
        """Convert camelCase to snake_case"""
        import re

        name = re.sub("([A-Z]+)", r"_\1", camel_case).lower()
        if name.startswith("_"):
            name = name[1:]
        return name
