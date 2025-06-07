
from nlb_catalogue_client.models.bib_format import BibFormat
from nlb_catalogue_client.models.new_arrival_title import NewArrivalTitle
from nlb_catalogue_client.types import UNSET


class TestNewArrivalTitle:
    def setup_method(self):
        """Setup common test objects"""
        self.format_ = BibFormat(code="BK", name="BOOKS")

    def test_basic_initialization(self):
        title = NewArrivalTitle(
            format_=self.format_,
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
        )

        assert title.format_ == self.format_
        assert title.title == "Sample Book"
        assert title.native_title == "样本书"
        assert title.series_title == ["Series 1", "Series 2"]
        assert title.native_series_title == ["系列 1", "系列 2"]
        assert title.author == "John Doe"
        assert title.native_author == "约翰·多伊"
        assert title.other_authors == ["Jane Smith", "Bob Wilson"]
        assert title.native_other_authors == ["简·史密斯", "鲍勃·威尔逊"]
        assert title.language == ["English", "Chinese"]
        assert title.audience == ["General", "Adult"]
        assert title.audience_imda == ["NC16", "PG"]
        assert title.brn == 99999999
        assert title.digital_id == "overdrive123"
        assert title.other_titles == ["Alternative Title 1", "Alternative Title 2"]
        assert title.native_other_titles == ["其他标题 1", "其他标题 2"]
        assert title.variant_titles == ["Variant 1", "Variant 2"]
        assert title.native_variant_titles == ["变体 1", "变体 2"]
        assert title.isbns == ["9709999999"]
        assert title.issns == ["9999-9999"]
        assert title.edition == ["First Edition"]
        assert title.native_edition == ["第一版"]
        assert title.publisher == ["Sample Publisher"]
        assert title.native_publisher == ["示例出版社"]
        assert title.publish_date == "2023"
        assert title.subjects == ["Fiction", "Adventure"]
        assert title.physical_description == ["300 pages"]
        assert title.native_physical_description == ["300页"]
        assert title.summary == ["A fascinating story"]
        assert title.native_summary == ["一个引人入胜的故事"]
        assert title.contents == ["Chapter 1", "Chapter 2"]
        assert title.native_contents == ["第一章", "第二章"]
        assert title.thesis == ["PhD Thesis"]
        assert title.native_thesis == ["博士论文"]
        assert title.notes == ["Special Edition"]
        assert title.native_notes == ["特别版"]
        assert title.active_reservations_count == 3
        assert title.volume_note == ["Volume 1"]
        assert title.native_volume_note == ["第一卷"]
        assert title.frequency == ["Monthly"]
        assert title.native_frequency == ["每月"]
        assert title.credits_ == ["Editor: John Smith"]
        assert title.native_credits == ["编辑：约翰·史密斯"]
        assert title.performers == ["Actor: Jane Doe"]
        assert title.native_performers == ["演员：简·多伊"]
        assert title.availability is True
        assert title.source == "Library"
        assert title.volumes == ["2023 issue 1"]

    def test_initialization_with_required_only(self):
        title = NewArrivalTitle(format_=self.format_)
        assert title.format_ == self.format_
        assert title.title is UNSET
        assert title.native_title is UNSET
        assert title.series_title is UNSET
        assert title.native_series_title is UNSET
        assert title.author is UNSET
        assert title.native_author is UNSET
        assert title.other_authors is UNSET
        assert title.native_other_authors is UNSET
        assert title.language is UNSET
        assert title.audience is UNSET
        assert title.audience_imda is UNSET

    def test_with_none_values(self):
        """Test initialization with None values"""
        title = NewArrivalTitle(
            format_=self.format_,
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
        )
        assert title.format_ == self.format_
        assert title.title == "Sample Book"
        assert title.native_title is None
        assert title.series_title is None
        assert title.native_series_title is None
        assert title.native_author is None
        assert title.other_authors is None
        assert title.native_other_authors is None
        assert title.audience is None
        assert title.audience_imda is None
        assert title.digital_id is None
        assert title.other_titles is None
        assert title.native_other_titles is None
        assert title.variant_titles is None
        assert title.native_variant_titles is None
        assert title.issns is None
        assert title.edition is None
        assert title.native_edition is None
        assert title.native_publisher is None
        assert title.native_physical_description is None
        assert title.summary is None
        assert title.native_summary is None
        assert title.contents is None
        assert title.native_contents is None
        assert title.thesis is None
        assert title.native_thesis is None
        assert title.native_notes is None
        assert title.volume_note is None
        assert title.native_volume_note is None
        assert title.frequency is None
        assert title.native_frequency is None
        assert title.credits_ is None
        assert title.native_credits is None
        assert title.performers is None
        assert title.native_performers is None
        assert title.source is None
        assert title.volumes is None

    def test_to_dict_full(self):
        title = NewArrivalTitle(
            format_=self.format_,
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
        )

        expected = {
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
        assert title.to_dict() == expected

    def test_to_dict_required(self):
        """Test converting to dictionary with only required fields"""
        title = NewArrivalTitle(format_=self.format_)

        expected = {
            "format": {"code": "BK", "name": "BOOKS"},
            "allowReservation": True,
            "isRestricted": False,
            "serial": False,
        }
        assert title.to_dict() == expected

    def test_to_dict_with_none(self):
        """Test converting to dictionary with None values"""
        title = NewArrivalTitle(
            format_=self.format_,
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
        )

        expected = {
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
        assert title.to_dict() == expected

    def test_from_dict_full(self):
        data = {
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

        title = NewArrivalTitle.from_dict(data)
        assert title.format_.code == "BK"
        assert title.format_.name == "BOOKS"
        assert title.title == "Sample Book"
        assert title.native_title == "样本书"
        assert title.series_title == ["Series 1", "Series 2"]
        assert title.native_series_title == ["系列 1", "系列 2"]
        assert title.author == "John Doe"
        assert title.native_author == "约翰·多伊"
        assert title.other_authors == ["Jane Smith", "Bob Wilson"]
        assert title.native_other_authors == ["简·史密斯", "鲍勃·威尔逊"]
        assert title.language == ["English", "Chinese"]
        assert title.audience == ["General", "Adult"]
        assert title.audience_imda == ["NC16", "PG"]
        assert title.brn == 99999999
        assert title.digital_id == "overdrive123"
        assert title.other_titles == ["Alternative Title 1", "Alternative Title 2"]
        assert title.native_other_titles == ["其他标题 1", "其他标题 2"]
        assert title.variant_titles == ["Variant 1", "Variant 2"]
        assert title.native_variant_titles == ["变体 1", "变体 2"]
        assert title.isbns == ["9709999999"]
        assert title.issns == ["9999-9999"]
        assert title.edition == ["First Edition"]
        assert title.native_edition == ["第一版"]
        assert title.publisher == ["Sample Publisher"]
        assert title.native_publisher == ["示例出版社"]
        assert title.publish_date == "2023"
        assert title.subjects == ["Fiction", "Adventure"]
        assert title.physical_description == ["300 pages"]
        assert title.native_physical_description == ["300页"]
        assert title.summary == ["A fascinating story"]
        assert title.native_summary == ["一个引人入胜的故事"]
        assert title.contents == ["Chapter 1", "Chapter 2"]
        assert title.native_contents == ["第一章", "第二章"]
        assert title.thesis == ["PhD Thesis"]
        assert title.native_thesis == ["博士论文"]
        assert title.notes == ["Special Edition"]
        assert title.native_notes == ["特别版"]
        assert title.active_reservations_count == 3
        assert title.volume_note == ["Volume 1"]
        assert title.native_volume_note == ["第一卷"]
        assert title.frequency == ["Monthly"]
        assert title.native_frequency == ["每月"]
        assert title.credits_ == ["Editor: John Smith"]
        assert title.native_credits == ["编辑：约翰·史密斯"]
        assert title.performers == ["Actor: Jane Doe"]
        assert title.native_performers == ["演员：简·多伊"]
        assert title.availability is True
        assert title.source == "Library"
        assert title.volumes == ["2023 issue 1"]

    def test_from_dict_required_only(self):
        """Test creating object from dictionary with only required fields"""
        data = {"format": {"code": "BK", "name": "BOOKS"}}

        title = NewArrivalTitle.from_dict(data)

        # Verify required field is properly set
        assert title.format_.code == "BK"
        assert title.format_.name == "BOOKS"

        # Verify all optional fields are UNSET
        assert title.brn is UNSET
        assert title.digital_id is UNSET
        assert title.other_titles is UNSET
        assert title.native_other_titles is UNSET
        assert title.variant_titles is UNSET
        assert title.native_variant_titles is UNSET
        assert title.other_authors is UNSET
        assert title.native_other_authors is UNSET
        assert title.isbns is UNSET
        assert title.issns is UNSET
        assert title.edition is UNSET
        assert title.native_edition is UNSET
        assert title.publisher is UNSET
        assert title.native_publisher is UNSET
        assert title.publish_date is UNSET
        assert title.subjects is UNSET
        assert title.physical_description is UNSET
        assert title.native_physical_description is UNSET
        assert title.summary is UNSET
        assert title.native_summary is UNSET
        assert title.contents is UNSET
        assert title.native_contents is UNSET
        assert title.thesis is UNSET
        assert title.native_thesis is UNSET
        assert title.notes is UNSET
        assert title.native_notes is UNSET
        assert title.active_reservations_count is UNSET
        assert title.audience is UNSET
        assert title.audience_imda is UNSET
        assert title.language is UNSET
        assert title.volume_note is UNSET
        assert title.native_volume_note is UNSET
        assert title.frequency is UNSET
        assert title.native_frequency is UNSET
        assert title.credits_ is UNSET
        assert title.native_credits is UNSET
        assert title.performers is UNSET
        assert title.native_performers is UNSET

    def test_from_dict_with_none(self):
        """Test creating object from dictionary with None values"""
        data = {
            "format": {"code": "BK", "name": "BOOKS"},
            "title": "Sample Book",
            "nativeTitle": None,
            "seriesTitle": None,
            "nativeSeriesTitle": None,
            "author": None,
            "nativeAuthor": None,
            "otherAuthors": None,
            "nativeOtherAuthors": None,
            "language": None,
            "audience": None,
            "audienceImda": None,
            "brn": None,
            "digitalId": None,
            "otherTitles": None,
            "nativeOtherTitles": None,
            "variantTitles": None,
            "nativeVariantTitles": None,
            "isbns": None,
            "issns": None,
            "edition": None,
            "nativeEdition": None,
            "publisher": None,
            "nativePublisher": None,
            "publishDate": None,
            "subjects": None,
            "physicalDescription": None,
            "nativePhysicalDescription": None,
            "summary": None,
            "nativeSummary": None,
            "contents": None,
            "nativeContents": None,
            "thesis": None,
            "nativeThesis": None,
            "notes": None,
            "nativeNotes": None,
            "activeReservationsCount": None,
            "volumeNote": None,
            "nativeVolumeNote": None,
            "frequency": None,
            "nativeFrequency": None,
            "credits": None,
            "nativeCredits": None,
            "performers": None,
            "nativePerformers": None,
            "availability": None,
            "source": None,
            "volumes": None,
            "allowReservation": True,
            "isRestricted": False,
            "serial": False,
        }

        title = NewArrivalTitle.from_dict(data)

        # Verify required fields and non-None value
        assert title.format_.code == "BK"
        assert title.format_.name == "BOOKS"
        assert title.title == "Sample Book"

        # Verify all None values are properly deserialized
        assert title.native_title is None
        assert title.series_title is None
        assert title.native_series_title is None
        assert title.author is None
        assert title.native_author is None
        assert title.other_authors is None
        assert title.native_other_authors is None
        assert title.language is None
        assert title.audience is None
        assert title.audience_imda is None
        assert title.brn is None
        assert title.digital_id is None
        assert title.other_titles is None
        assert title.native_other_titles is None
        assert title.variant_titles is None
        assert title.native_variant_titles is None
        assert title.isbns is None
        assert title.issns is None
        assert title.edition is None
        assert title.native_edition is None
        assert title.publisher is None
        assert title.native_publisher is None
        assert title.publish_date is None
        assert title.subjects is None
        assert title.physical_description is None
        assert title.native_physical_description is None
        assert title.summary is None
        assert title.native_summary is None
        assert title.contents is None
        assert title.native_contents is None
        assert title.thesis is None
        assert title.native_thesis is None
        assert title.notes is None
        assert title.native_notes is None
        assert title.active_reservations_count is None
        assert title.volume_note is None
        assert title.native_volume_note is None
        assert title.frequency is None
        assert title.native_frequency is None
        assert title.credits_ is None
        assert title.native_credits is None
        assert title.performers is None
        assert title.native_performers is None
        assert title.availability is None
        assert title.source is None
        assert title.volumes is None

        # Verify default boolean values
        assert title.allow_reservation is True
        assert title.is_restricted is False
        assert title.serial is False

    def test_from_dict_with_invalid_list_fields(self):
        """Test creating object from dictionary with invalid list field types and verify TypeError handling"""
        data = {
            "format": {"code": "BK", "name": "BOOKS"},
            "title": "Sample Book",
            # Test all list fields with invalid types
            "seriesTitle": "Not a list",
            "nativeSeriesTitle": 123,
            "otherAuthors": {"key": "value"},
            "nativeOtherAuthors": True,
            "otherTitles": 456,
            "nativeOtherTitles": "Not a list",
            "variantTitles": {"key": "value"},
            "nativeVariantTitles": 789,
            "isbns": "Not a list",
            "issns": {"key": "value"},
            "edition": True,
            "nativeEdition": 101,
            "publisher": "Not a list",
            "nativePublisher": {"key": "value"},
            "subjects": True,
            "physicalDescription": 102,
            "nativePhysicalDescription": "Not a list",
            "summary": {"key": "value"},
            "nativeSummary": 103,
            "contents": "Not a list",
            "nativeContents": {"key": "value"},
            "thesis": True,
            "nativeThesis": 104,
            "notes": "Not a list",
            "nativeNotes": {"key": "value"},
            "volumeNote": True,
            "nativeVolumeNote": 105,
            "frequency": "Not a list",
            "nativeFrequency": {"key": "value"},
            "credits": True,
            "nativeCredits": 106,
            "performers": "Not a list",
            "nativePerformers": {"key": "value"},
            "volumes": True,
            "audience": 107,
            "audienceImda": "Not a list",
            "language": {"key": "value"},
        }

        # Test normal initialization with invalid list fields
        title = NewArrivalTitle.from_dict(data)

        # Verify required fields are still properly set
        assert title.format_.code == "BK"
        assert title.format_.name == "BOOKS"
        assert title.title == "Sample Book"

        # Verify all invalid list fields are returned as-is
        assert title.series_title == "Not a list"
        assert title.native_series_title == 123
        assert title.other_authors == {"key": "value"}
        assert title.native_other_authors is True
        assert title.other_titles == 456
        assert title.native_other_titles == "Not a list"
        assert title.variant_titles == {"key": "value"}
        assert title.native_variant_titles == 789
        assert title.isbns == "Not a list"
        assert title.issns == {"key": "value"}
        assert title.edition is True
        assert title.native_edition == 101
        assert title.publisher == "Not a list"
        assert title.native_publisher == {"key": "value"}
        assert title.subjects is True
        assert title.physical_description == 102
        assert title.native_physical_description == "Not a list"
        assert title.summary == {"key": "value"}
        assert title.native_summary == 103
        assert title.contents == "Not a list"
        assert title.native_contents == {"key": "value"}
        assert title.thesis is True
        assert title.native_thesis == 104
        assert title.notes == "Not a list"
        assert title.native_notes == {"key": "value"}
        assert title.volume_note is True
        assert title.native_volume_note == 105
        assert title.frequency == "Not a list"
        assert title.native_frequency == {"key": "value"}
        assert title.credits_ is True
        assert title.native_credits == 106
        assert title.performers == "Not a list"
        assert title.native_performers == {"key": "value"}
        assert title.volumes is True
        assert title.audience == 107
        assert title.audience_imda == "Not a list"
        assert title.language == {"key": "value"}

        # Test invalid types for non-list fields
        invalid_data = {
            "format": {"code": "BK", "name": "BOOKS"},
            "brn": "not an integer",
            "availability": "not a boolean",
            "allowReservation": "not a boolean",
            "isRestricted": "not a boolean",
            "serial": "not a boolean",
            "activeReservationsCount": "not an integer",
        }

        title = NewArrivalTitle.from_dict(invalid_data)

        # Verify non-list fields with invalid types are stored as-is
        assert title.brn == "not an integer"
        assert title.availability == "not a boolean"
        assert title.allow_reservation == "not a boolean"
        assert title.is_restricted == "not a boolean"
        assert title.serial == "not a boolean"
        assert title.active_reservations_count == "not an integer"
