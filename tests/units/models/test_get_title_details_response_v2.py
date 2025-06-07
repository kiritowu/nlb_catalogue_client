from nlb_catalogue_client.models.bib_format import BibFormat
from nlb_catalogue_client.models.get_title_details_response_v2 import GetTitleDetailsResponseV2
from nlb_catalogue_client.types import UNSET


class TestGetTitleDetailsResponseV2:
    def setup_method(self):
        """Setup common test objects"""
        self.format_ = BibFormat(code="BK", name="BOOKS")

    def test_basic_initialization(self):
        """Test initialization with all fields"""
        response = GetTitleDetailsResponseV2(
            format_=self.format_,
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
            allow_reservation=True,
            is_restricted=False,
            active_reservations_count=3,
            audience=["General", "Adult"],
            audience_imda=["NC16", "PG"],
            language=["English", "Chinese"],
            serial=False,
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
            title="Sample Book",
            native_title="样本书",
            series_title=["Series 1"],
            native_series_title=["系列 1"],
            author="John Doe",
            native_author="约翰·多伊",
        )

        assert response.format_ == self.format_
        assert response.brn == 99999999
        assert response.digital_id == "overdrive123"
        assert response.other_titles == ["Alternative Title 1"]
        assert response.native_other_titles == ["其他标题 1"]
        assert response.variant_titles == ["Variant 1"]
        assert response.native_variant_titles == ["变体 1"]
        assert response.other_authors == ["Jane Smith"]
        assert response.native_other_authors == ["简·史密斯"]
        assert response.isbns == ["9709999999"]
        assert response.issns == ["9999-9999"]
        assert response.edition == ["First Edition"]
        assert response.native_edition == ["第一版"]
        assert response.publisher == ["Sample Publisher"]
        assert response.native_publisher == ["示例出版社"]
        assert response.publish_date == "2023"
        assert response.subjects == ["Fiction"]
        assert response.physical_description == ["300 pages"]
        assert response.native_physical_description == ["300页"]
        assert response.summary == ["A story"]
        assert response.native_summary == ["故事"]
        assert response.contents == ["Chapter 1"]
        assert response.native_contents == ["第一章"]
        assert response.thesis == ["PhD Thesis"]
        assert response.native_thesis == ["博士论文"]
        assert response.notes == ["Special Edition"]
        assert response.native_notes == ["特别版"]
        assert response.allow_reservation is True
        assert response.is_restricted is False
        assert response.active_reservations_count == 3
        assert response.audience == ["General", "Adult"]
        assert response.audience_imda == ["NC16", "PG"]
        assert response.language == ["English", "Chinese"]
        assert response.serial is False
        assert response.volume_note == ["Volume 1"]
        assert response.native_volume_note == ["第一卷"]
        assert response.frequency == ["Monthly"]
        assert response.native_frequency == ["每月"]
        assert response.credits_ == ["Editor: John"]
        assert response.native_credits == ["编辑：约翰"]
        assert response.performers == ["Actor: Jane"]
        assert response.native_performers == ["演员：简"]
        assert response.availability is True
        assert response.source == "Library"
        assert response.volumes == ["2023 issue 1"]
        assert response.title == "Sample Book"
        assert response.native_title == "样本书"
        assert response.series_title == ["Series 1"]
        assert response.native_series_title == ["系列 1"]
        assert response.author == "John Doe"
        assert response.native_author == "约翰·多伊"

    def test_initialization_with_required_only(self):
        """Test initialization with required fields only"""
        response = GetTitleDetailsResponseV2(format_=self.format_)

        assert response.format_ == self.format_
        assert response.brn is UNSET
        assert response.digital_id is UNSET
        assert response.other_titles is UNSET
        assert response.native_other_titles is UNSET
        assert response.variant_titles is UNSET
        assert response.native_variant_titles is UNSET
        assert response.other_authors is UNSET
        assert response.native_other_authors is UNSET
        assert response.isbns is UNSET
        assert response.issns is UNSET
        assert response.edition is UNSET
        assert response.native_edition is UNSET
        assert response.publisher is UNSET
        assert response.native_publisher is UNSET
        assert response.publish_date is UNSET
        assert response.subjects is UNSET
        assert response.physical_description is UNSET
        assert response.native_physical_description is UNSET
        assert response.summary is UNSET
        assert response.native_summary is UNSET
        assert response.contents is UNSET
        assert response.native_contents is UNSET
        assert response.thesis is UNSET
        assert response.native_thesis is UNSET
        assert response.notes is UNSET
        assert response.native_notes is UNSET
        assert response.allow_reservation is True  # Default value
        assert response.is_restricted is False  # Default value
        assert response.active_reservations_count is UNSET
        assert response.audience is UNSET
        assert response.audience_imda is UNSET
        assert response.language is UNSET
        assert response.serial is False  # Default value
        assert response.volume_note is UNSET
        assert response.native_volume_note is UNSET
        assert response.frequency is UNSET
        assert response.native_frequency is UNSET
        assert response.credits_ is UNSET
        assert response.native_credits is UNSET
        assert response.performers is UNSET
        assert response.native_performers is UNSET
        assert response.availability is UNSET
        assert response.source is UNSET
        assert response.volumes is UNSET
        assert response.title is UNSET
        assert response.native_title is UNSET
        assert response.series_title is UNSET
        assert response.native_series_title is UNSET
        assert response.author is UNSET
        assert response.native_author is UNSET

    def test_to_dict_full(self):
        """Test converting to dictionary with all fields"""
        response = GetTitleDetailsResponseV2(
            format_=self.format_,
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
            allow_reservation=True,
            is_restricted=False,
            active_reservations_count=3,
            audience=["General", "Adult"],
            audience_imda=["NC16", "PG"],
            language=["English", "Chinese"],
            serial=False,
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
            title="Sample Book",
            native_title="样本书",
            series_title=["Series 1"],
            native_series_title=["系列 1"],
            author="John Doe",
            native_author="约翰·多伊",
        )

        expected = {
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
            "allowReservation": True,
            "isRestricted": False,
            "activeReservationsCount": 3,
            "audience": ["General", "Adult"],
            "audienceImda": ["NC16", "PG"],
            "language": ["English", "Chinese"],
            "serial": False,
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
            "title": "Sample Book",
            "nativeTitle": "样本书",
            "seriesTitle": ["Series 1"],
            "nativeSeriesTitle": ["系列 1"],
            "author": "John Doe",
            "nativeAuthor": "约翰·多伊",
        }

        assert response.to_dict() == expected

    def test_to_dict_required_only(self):
        """Test converting to dictionary with required fields only"""
        response = GetTitleDetailsResponseV2(format_=self.format_)

        expected = {
            "format": {"code": "BK", "name": "BOOKS"},
            "allowReservation": True,
            "isRestricted": False,
            "serial": False,
        }

        assert response.to_dict() == expected

    def test_to_dict_with_none(self):
        """Test converting to dictionary with None values"""
        response = GetTitleDetailsResponseV2(
            format_=self.format_,
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
            audience=None,
            audience_imda=None,
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
            native_title=None,
            series_title=None,
            native_series_title=None,
            native_author=None,
        )

        expected = {
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
            "audience": None,
            "audienceImda": None,
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
            "nativeTitle": None,
            "seriesTitle": None,
            "nativeSeriesTitle": None,
            "nativeAuthor": None,
            "allowReservation": True,
            "isRestricted": False,
            "serial": False,
        }

        assert response.to_dict() == expected

    def test_from_dict_full(self):
        """Test creating object from dictionary with all fields"""
        data = {
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
            "allowReservation": True,
            "isRestricted": False,
            "activeReservationsCount": 3,
            "audience": ["General", "Adult"],
            "audienceImda": ["NC16", "PG"],
            "language": ["English", "Chinese"],
            "serial": False,
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
            "title": "Sample Book",
            "nativeTitle": "样本书",
            "seriesTitle": ["Series 1"],
            "nativeSeriesTitle": ["系列 1"],
            "author": "John Doe",
            "nativeAuthor": "约翰·多伊",
        }

        response = GetTitleDetailsResponseV2.from_dict(data)

        assert response.format_.code == "BK"
        assert response.format_.name == "BOOKS"
        assert response.brn == 99999999
        assert response.digital_id == "overdrive123"
        assert response.other_titles == ["Alternative Title 1"]
        assert response.native_other_titles == ["其他标题 1"]
        assert response.variant_titles == ["Variant 1"]
        assert response.native_variant_titles == ["变体 1"]
        assert response.other_authors == ["Jane Smith"]
        assert response.native_other_authors == ["简·史密斯"]
        assert response.isbns == ["9709999999"]
        assert response.issns == ["9999-9999"]
        assert response.edition == ["First Edition"]
        assert response.native_edition == ["第一版"]
        assert response.publisher == ["Sample Publisher"]
        assert response.native_publisher == ["示例出版社"]
        assert response.publish_date == "2023"
        assert response.subjects == ["Fiction"]
        assert response.physical_description == ["300 pages"]
        assert response.native_physical_description == ["300页"]
        assert response.summary == ["A story"]
        assert response.native_summary == ["故事"]
        assert response.contents == ["Chapter 1"]
        assert response.native_contents == ["第一章"]
        assert response.thesis == ["PhD Thesis"]
        assert response.native_thesis == ["博士论文"]
        assert response.notes == ["Special Edition"]
        assert response.native_notes == ["特别版"]
        assert response.allow_reservation is True
        assert response.is_restricted is False
        assert response.active_reservations_count == 3
        assert response.audience == ["General", "Adult"]
        assert response.audience_imda == ["NC16", "PG"]
        assert response.language == ["English", "Chinese"]
        assert response.serial is False
        assert response.volume_note == ["Volume 1"]
        assert response.native_volume_note == ["第一卷"]
        assert response.frequency == ["Monthly"]
        assert response.native_frequency == ["每月"]
        assert response.credits_ == ["Editor: John"]
        assert response.native_credits == ["编辑：约翰"]
        assert response.performers == ["Actor: Jane"]
        assert response.native_performers == ["演员：简"]
        assert response.availability is True
        assert response.source == "Library"
        assert response.volumes == ["2023 issue 1"]
        assert response.title == "Sample Book"
        assert response.native_title == "样本书"
        assert response.series_title == ["Series 1"]
        assert response.native_series_title == ["系列 1"]
        assert response.author == "John Doe"
        assert response.native_author == "约翰·多伊"

    def test_from_dict_required_only(self):
        """Test creating object from dictionary with required fields only"""
        data = {
            "format": {"code": "BK", "name": "BOOKS"},
        }

        response = GetTitleDetailsResponseV2.from_dict(data)

        assert response.format_.code == "BK"
        assert response.format_.name == "BOOKS"
        assert response.brn is UNSET
        assert response.digital_id is UNSET
        assert response.other_titles is UNSET
        assert response.native_other_titles is UNSET
        assert response.variant_titles is UNSET
        assert response.native_variant_titles is UNSET
        assert response.other_authors is UNSET
        assert response.native_other_authors is UNSET
        assert response.isbns is UNSET
        assert response.issns is UNSET
        assert response.edition is UNSET
        assert response.native_edition is UNSET
        assert response.publisher is UNSET
        assert response.native_publisher is UNSET
        assert response.publish_date is UNSET
        assert response.subjects is UNSET
        assert response.physical_description is UNSET
        assert response.native_physical_description is UNSET
        assert response.summary is UNSET
        assert response.native_summary is UNSET
        assert response.contents is UNSET
        assert response.native_contents is UNSET
        assert response.thesis is UNSET
        assert response.native_thesis is UNSET
        assert response.notes is UNSET
        assert response.native_notes is UNSET
        assert response.allow_reservation is UNSET
        assert response.is_restricted is UNSET
        assert response.active_reservations_count is UNSET
        assert response.audience is UNSET
        assert response.audience_imda is UNSET
        assert response.language is UNSET
        assert response.serial is UNSET
        assert response.volume_note is UNSET
        assert response.native_volume_note is UNSET
        assert response.frequency is UNSET
        assert response.native_frequency is UNSET
        assert response.credits_ is UNSET
        assert response.native_credits is UNSET
        assert response.performers is UNSET
        assert response.native_performers is UNSET
        assert response.availability is UNSET
        assert response.source is UNSET
        assert response.volumes is UNSET
        assert response.title is UNSET
        assert response.native_title is UNSET
        assert response.series_title is UNSET
        assert response.native_series_title is UNSET
        assert response.author is UNSET
        assert response.native_author is UNSET

    def test_from_dict_with_none(self):
        """Test creating object from dictionary with None values"""
        data = {
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
            "audience": None,
            "audienceImda": None,
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
            "nativeTitle": None,
            "seriesTitle": None,
            "nativeSeriesTitle": None,
            "nativeAuthor": None,
        }

        response = GetTitleDetailsResponseV2.from_dict(data)

        assert response.format_.code == "BK"
        assert response.format_.name == "BOOKS"
        assert response.digital_id is None
        assert response.other_titles is None
        assert response.native_other_titles is None
        assert response.variant_titles is None
        assert response.native_variant_titles is None
        assert response.other_authors is None
        assert response.native_other_authors is None
        assert response.issns is None
        assert response.edition is None
        assert response.native_edition is None
        assert response.native_publisher is None
        assert response.native_physical_description is None
        assert response.summary is None
        assert response.native_summary is None
        assert response.contents is None
        assert response.native_contents is None
        assert response.thesis is None
        assert response.native_thesis is None
        assert response.native_notes is None
        assert response.audience is None
        assert response.audience_imda is None
        assert response.volume_note is None
        assert response.native_volume_note is None
        assert response.frequency is None
        assert response.native_frequency is None
        assert response.credits_ is None
        assert response.native_credits is None
        assert response.performers is None
        assert response.native_performers is None
        assert response.source is None
        assert response.volumes is None
        assert response.native_title is None
        assert response.series_title is None
        assert response.native_series_title is None
        assert response.native_author is None

    def test_from_dict_with_invalid_values(self):
        """Test creating object from dictionary with invalid field types"""
        data = {
            "format": {"code": "BK", "name": "BOOKS"},
            "otherTitles": "Not a list",
            "nativeOtherTitles": "Not a list",
            "variantTitles": "Not a list",
            "nativeVariantTitles": "Not a list",
            "otherAuthors": "Not a list",
            "nativeOtherAuthors": "Not a list",
            "isbns": "Not a list",
            "issns": "Not a list",
            "edition": "Not a list",
            "nativeEdition": "Not a list",
            "publisher": "Not a list",
            "nativePublisher": "Not a list",
            "subjects": "Not a list",
            "physicalDescription": "Not a list",
            "nativePhysicalDescription": "Not a list",
            "summary": "Not a list",
            "nativeSummary": "Not a list",
            "contents": "Not a list",
            "nativeContents": "Not a list",
            "thesis": "Not a list",
            "nativeThesis": "Not a list",
            "notes": "Not a list",
            "nativeNotes": "Not a list",
            "audience": "Not a list",
            "audienceImda": "Not a list",
            "language": "Not a list",
            "volumeNote": "Not a list",
            "nativeVolumeNote": "Not a list",
            "frequency": "Not a list",
            "nativeFrequency": "Not a list",
            "credits": "Not a list",
            "nativeCredits": "Not a list",
            "performers": "Not a list",
            "nativePerformers": "Not a list",
            "volumes": "Not a list",
            "seriesTitle": "Not a list",
            "nativeSeriesTitle": "Not a list",
            "brn": "Not an integer",
            "activeReservationsCount": "Not an integer",
            "allowReservation": "Not a boolean",
            "isRestricted": "Not a boolean",
            "serial": "Not a boolean",
            "availability": "Not a boolean",
        }

        response = GetTitleDetailsResponseV2.from_dict(data)

        # Verify invalid list fields are returned as-is
        assert response.other_titles == "Not a list"
        assert response.native_other_titles == "Not a list"
        assert response.variant_titles == "Not a list"
        assert response.native_variant_titles == "Not a list"
        assert response.other_authors == "Not a list"
        assert response.native_other_authors == "Not a list"
        assert response.isbns == "Not a list"
        assert response.issns == "Not a list"
        assert response.edition == "Not a list"
        assert response.native_edition == "Not a list"
        assert response.publisher == "Not a list"
        assert response.native_publisher == "Not a list"
        assert response.subjects == "Not a list"
        assert response.physical_description == "Not a list"
        assert response.native_physical_description == "Not a list"
        assert response.summary == "Not a list"
        assert response.native_summary == "Not a list"
        assert response.contents == "Not a list"
        assert response.native_contents == "Not a list"
        assert response.thesis == "Not a list"
        assert response.native_thesis == "Not a list"
        assert response.notes == "Not a list"
        assert response.native_notes == "Not a list"
        assert response.audience == "Not a list"
        assert response.audience_imda == "Not a list"
        assert response.language == "Not a list"
        assert response.volume_note == "Not a list"
        assert response.native_volume_note == "Not a list"
        assert response.frequency == "Not a list"
        assert response.native_frequency == "Not a list"
        assert response.credits_ == "Not a list"
        assert response.native_credits == "Not a list"
        assert response.performers == "Not a list"
        assert response.native_performers == "Not a list"
        assert response.volumes == "Not a list"
        assert response.series_title == "Not a list"
        assert response.native_series_title == "Not a list"

        # Verify invalid numeric fields are returned as-is
        assert response.brn == "Not an integer"
        assert response.active_reservations_count == "Not an integer"

        # Verify invalid boolean fields are returned as-is
        assert response.allow_reservation == "Not a boolean"
        assert response.is_restricted == "Not a boolean"
        assert response.serial == "Not a boolean"
        assert response.availability == "Not a boolean"

        # Verify required format field is still properly parsed
        assert response.format_.code == "BK"
        assert response.format_.name == "BOOKS"
