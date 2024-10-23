from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bib_format import BibFormat


T = TypeVar("T", bound="NewArrivalTitle")


@_attrs_define
class NewArrivalTitle:
    """
    Attributes:
        format_ (BibFormat): Bibliographic Formats. Please refer to code list C001.
        brn (Union[Unset, int]): Bibliographic reference number. Example: 99999999.
        digital_id (Union[None, Unset, str]): For external query purpose, to get the title or reserve the title in
            Overdrive Example: Overdrive Id.
        other_titles (Union[List[str], None, Unset]): Other titles.
        native_other_titles (Union[List[str], None, Unset]): Other titles(Native language).
        variant_titles (Union[List[str], None, Unset]): Varying Form of Title.
        native_variant_titles (Union[List[str], None, Unset]): Varying Form of Title(Native language).
        other_authors (Union[List[str], None, Unset]): List of other authors.
        native_other_authors (Union[List[str], None, Unset]): List of other authors(Native language).
        isbns (Union[Unset, List[str]]): Bibliographic International Standard Book Number identifiers. Example:
            ['9709999999'].
        issns (Union[List[str], None, Unset]): Bibliographic International Standard Serial Number identifiers. Example:
            ['9999-9999'].
        edition (Union[List[str], None, Unset]): Information relating to the edition of a work. Example: ['Di 1 ban'].
        native_edition (Union[List[str], None, Unset]): Information relating to the edition of a work(Native language).
            Example: ['第1版'].
        publisher (Union[Unset, List[str]]): Published by. Example: ["[Xi'an] : Wei lai chu ban she"].
        native_publisher (Union[List[str], None, Unset]): Published by(Native language). Example: ['[西安] : 未来出版社'].
        publish_date (Union[Unset, str]): publish date or year. Example: 2019-.
        subjects (Union[Unset, List[str]]): subjects. Example: ['Science -- Experiments -- Juvenile films'].
        physical_description (Union[Unset, List[str]]): Title physical dimensions. Example: ['283 p. : ill. ; 22 cm'].
        native_physical_description (Union[List[str], None, Unset]): Title physical dimensions(Native language).
            Example: ['283页 : 插图 ; 22公分'].
        summary (Union[List[str], None, Unset]): Summary of the bibliographic content.
        native_summary (Union[List[str], None, Unset]): Summary of the bibliographic content(Native language).
        contents (Union[List[str], None, Unset]): Formatted Contents Note.
        native_contents (Union[List[str], None, Unset]): Formatted Contents Note(Native language).
        thesis (Union[List[str], None, Unset]): Dissertation Note.
        native_thesis (Union[List[str], None, Unset]): Dissertation Note(Native language).
        notes (Union[Unset, List[str]]): notes.
        native_notes (Union[List[str], None, Unset]): Native notes of the bibliographic record.
        allow_reservation (Union[Unset, bool]): Allow to place reservation or not. Default: True.
        is_restricted (Union[Unset, bool]): true, when title is marked as restricted publication. Default: False.
        active_reservations_count (Union[Unset, int]): Number of reservations placed and in queue, not fullfilled and
            not expired. Example: 3.
        audience (Union[List[str], None, Unset]): Target audience - Marc tag 521 (all).
        audience_imda (Union[List[str], None, Unset]): target audience - Marc tag 521 Ind 3 - Specific to highlight in
            display. Example: ['IMDA Advisory: Parental Guidance recommended.'].
        language (Union[Unset, List[str]]): Languages Example: ['Chinese'].
        serial (Union[Unset, bool]): serial indicator. Default: False.
        volume_note (Union[List[str], None, Unset]): Volume information. Example: ['Vol. 1 (Jul. 1859)-'].
        native_volume_note (Union[List[str], None, Unset]): Volume information(Native language).
        frequency (Union[List[str], None, Unset]): Publish frequency. Example: ['Monthly'].
        native_frequency (Union[List[str], None, Unset]): Publish frequency(Native language).
        credits_ (Union[List[str], None, Unset]): Creation/Production Credits Note.
        native_credits (Union[List[str], None, Unset]): Creation/Production Credits Note(Native language).
        performers (Union[List[str], None, Unset]): Participant or Performer Note.
        native_performers (Union[List[str], None, Unset]): Participant or Performer Note(Native language).
        availability (Union[Unset, bool]): true when at least 1 item is "available" status.
        source (Union[None, Unset, str]): Source of the title Example: Overdrive.
        volumes (Union[List[str], None, Unset]): Volume name. Example: ['2023 issue 2'].
        title (Union[Unset, str]): Full title (with author info suffixed by /) of the bibliographic record.
        native_title (Union[None, Unset, str]): Full title (with author info suffixed by /) of the bibliographic
            record(Native language).
        series_title (Union[List[str], None, Unset]): Series titles. Example: ['123 Zhima Jie'].
        native_series_title (Union[List[str], None, Unset]): Series titles(Native language). Example: ['123芝麻街'].
        author (Union[Unset, str]): Author name in english. Example: Song bing wu de yi xiang shi jie..
        native_author (Union[None, Unset, str]): Bibliographic title(Native language). Example: 松饼屋的异想世界.
    """

    format_: "BibFormat"
    brn: Union[Unset, int] = UNSET
    digital_id: Union[None, Unset, str] = UNSET
    other_titles: Union[List[str], None, Unset] = UNSET
    native_other_titles: Union[List[str], None, Unset] = UNSET
    variant_titles: Union[List[str], None, Unset] = UNSET
    native_variant_titles: Union[List[str], None, Unset] = UNSET
    other_authors: Union[List[str], None, Unset] = UNSET
    native_other_authors: Union[List[str], None, Unset] = UNSET
    isbns: Union[Unset, List[str]] = UNSET
    issns: Union[List[str], None, Unset] = UNSET
    edition: Union[List[str], None, Unset] = UNSET
    native_edition: Union[List[str], None, Unset] = UNSET
    publisher: Union[Unset, List[str]] = UNSET
    native_publisher: Union[List[str], None, Unset] = UNSET
    publish_date: Union[Unset, str] = UNSET
    subjects: Union[Unset, List[str]] = UNSET
    physical_description: Union[Unset, List[str]] = UNSET
    native_physical_description: Union[List[str], None, Unset] = UNSET
    summary: Union[List[str], None, Unset] = UNSET
    native_summary: Union[List[str], None, Unset] = UNSET
    contents: Union[List[str], None, Unset] = UNSET
    native_contents: Union[List[str], None, Unset] = UNSET
    thesis: Union[List[str], None, Unset] = UNSET
    native_thesis: Union[List[str], None, Unset] = UNSET
    notes: Union[Unset, List[str]] = UNSET
    native_notes: Union[List[str], None, Unset] = UNSET
    allow_reservation: Union[Unset, bool] = True
    is_restricted: Union[Unset, bool] = False
    active_reservations_count: Union[Unset, int] = UNSET
    audience: Union[List[str], None, Unset] = UNSET
    audience_imda: Union[List[str], None, Unset] = UNSET
    language: Union[Unset, List[str]] = UNSET
    serial: Union[Unset, bool] = False
    volume_note: Union[List[str], None, Unset] = UNSET
    native_volume_note: Union[List[str], None, Unset] = UNSET
    frequency: Union[List[str], None, Unset] = UNSET
    native_frequency: Union[List[str], None, Unset] = UNSET
    credits_: Union[List[str], None, Unset] = UNSET
    native_credits: Union[List[str], None, Unset] = UNSET
    performers: Union[List[str], None, Unset] = UNSET
    native_performers: Union[List[str], None, Unset] = UNSET
    availability: Union[Unset, bool] = UNSET
    source: Union[None, Unset, str] = UNSET
    volumes: Union[List[str], None, Unset] = UNSET
    title: Union[Unset, str] = UNSET
    native_title: Union[None, Unset, str] = UNSET
    series_title: Union[List[str], None, Unset] = UNSET
    native_series_title: Union[List[str], None, Unset] = UNSET
    author: Union[Unset, str] = UNSET
    native_author: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        format_ = self.format_.to_dict()

        brn = self.brn

        digital_id: Union[None, Unset, str]
        if isinstance(self.digital_id, Unset):
            digital_id = UNSET
        else:
            digital_id = self.digital_id

        other_titles: Union[List[str], None, Unset]
        if isinstance(self.other_titles, Unset):
            other_titles = UNSET
        elif isinstance(self.other_titles, list):
            other_titles = self.other_titles

        else:
            other_titles = self.other_titles

        native_other_titles: Union[List[str], None, Unset]
        if isinstance(self.native_other_titles, Unset):
            native_other_titles = UNSET
        elif isinstance(self.native_other_titles, list):
            native_other_titles = self.native_other_titles

        else:
            native_other_titles = self.native_other_titles

        variant_titles: Union[List[str], None, Unset]
        if isinstance(self.variant_titles, Unset):
            variant_titles = UNSET
        elif isinstance(self.variant_titles, list):
            variant_titles = self.variant_titles

        else:
            variant_titles = self.variant_titles

        native_variant_titles: Union[List[str], None, Unset]
        if isinstance(self.native_variant_titles, Unset):
            native_variant_titles = UNSET
        elif isinstance(self.native_variant_titles, list):
            native_variant_titles = self.native_variant_titles

        else:
            native_variant_titles = self.native_variant_titles

        other_authors: Union[List[str], None, Unset]
        if isinstance(self.other_authors, Unset):
            other_authors = UNSET
        elif isinstance(self.other_authors, list):
            other_authors = self.other_authors

        else:
            other_authors = self.other_authors

        native_other_authors: Union[List[str], None, Unset]
        if isinstance(self.native_other_authors, Unset):
            native_other_authors = UNSET
        elif isinstance(self.native_other_authors, list):
            native_other_authors = self.native_other_authors

        else:
            native_other_authors = self.native_other_authors

        isbns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.isbns, Unset):
            isbns = self.isbns

        issns: Union[List[str], None, Unset]
        if isinstance(self.issns, Unset):
            issns = UNSET
        elif isinstance(self.issns, list):
            issns = self.issns

        else:
            issns = self.issns

        edition: Union[List[str], None, Unset]
        if isinstance(self.edition, Unset):
            edition = UNSET
        elif isinstance(self.edition, list):
            edition = self.edition

        else:
            edition = self.edition

        native_edition: Union[List[str], None, Unset]
        if isinstance(self.native_edition, Unset):
            native_edition = UNSET
        elif isinstance(self.native_edition, list):
            native_edition = self.native_edition

        else:
            native_edition = self.native_edition

        publisher: Union[Unset, List[str]] = UNSET
        if not isinstance(self.publisher, Unset):
            publisher = self.publisher

        native_publisher: Union[List[str], None, Unset]
        if isinstance(self.native_publisher, Unset):
            native_publisher = UNSET
        elif isinstance(self.native_publisher, list):
            native_publisher = self.native_publisher

        else:
            native_publisher = self.native_publisher

        publish_date = self.publish_date

        subjects: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subjects, Unset):
            subjects = self.subjects

        physical_description: Union[Unset, List[str]] = UNSET
        if not isinstance(self.physical_description, Unset):
            physical_description = self.physical_description

        native_physical_description: Union[List[str], None, Unset]
        if isinstance(self.native_physical_description, Unset):
            native_physical_description = UNSET
        elif isinstance(self.native_physical_description, list):
            native_physical_description = self.native_physical_description

        else:
            native_physical_description = self.native_physical_description

        summary: Union[List[str], None, Unset]
        if isinstance(self.summary, Unset):
            summary = UNSET
        elif isinstance(self.summary, list):
            summary = self.summary

        else:
            summary = self.summary

        native_summary: Union[List[str], None, Unset]
        if isinstance(self.native_summary, Unset):
            native_summary = UNSET
        elif isinstance(self.native_summary, list):
            native_summary = self.native_summary

        else:
            native_summary = self.native_summary

        contents: Union[List[str], None, Unset]
        if isinstance(self.contents, Unset):
            contents = UNSET
        elif isinstance(self.contents, list):
            contents = self.contents

        else:
            contents = self.contents

        native_contents: Union[List[str], None, Unset]
        if isinstance(self.native_contents, Unset):
            native_contents = UNSET
        elif isinstance(self.native_contents, list):
            native_contents = self.native_contents

        else:
            native_contents = self.native_contents

        thesis: Union[List[str], None, Unset]
        if isinstance(self.thesis, Unset):
            thesis = UNSET
        elif isinstance(self.thesis, list):
            thesis = self.thesis

        else:
            thesis = self.thesis

        native_thesis: Union[List[str], None, Unset]
        if isinstance(self.native_thesis, Unset):
            native_thesis = UNSET
        elif isinstance(self.native_thesis, list):
            native_thesis = self.native_thesis

        else:
            native_thesis = self.native_thesis

        notes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes

        native_notes: Union[List[str], None, Unset]
        if isinstance(self.native_notes, Unset):
            native_notes = UNSET
        elif isinstance(self.native_notes, list):
            native_notes = self.native_notes

        else:
            native_notes = self.native_notes

        allow_reservation = self.allow_reservation

        is_restricted = self.is_restricted

        active_reservations_count = self.active_reservations_count

        audience: Union[List[str], None, Unset]
        if isinstance(self.audience, Unset):
            audience = UNSET
        elif isinstance(self.audience, list):
            audience = self.audience

        else:
            audience = self.audience

        audience_imda: Union[List[str], None, Unset]
        if isinstance(self.audience_imda, Unset):
            audience_imda = UNSET
        elif isinstance(self.audience_imda, list):
            audience_imda = self.audience_imda

        else:
            audience_imda = self.audience_imda

        language: Union[Unset, List[str]] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language

        serial = self.serial

        volume_note: Union[List[str], None, Unset]
        if isinstance(self.volume_note, Unset):
            volume_note = UNSET
        elif isinstance(self.volume_note, list):
            volume_note = self.volume_note

        else:
            volume_note = self.volume_note

        native_volume_note: Union[List[str], None, Unset]
        if isinstance(self.native_volume_note, Unset):
            native_volume_note = UNSET
        elif isinstance(self.native_volume_note, list):
            native_volume_note = self.native_volume_note

        else:
            native_volume_note = self.native_volume_note

        frequency: Union[List[str], None, Unset]
        if isinstance(self.frequency, Unset):
            frequency = UNSET
        elif isinstance(self.frequency, list):
            frequency = self.frequency

        else:
            frequency = self.frequency

        native_frequency: Union[List[str], None, Unset]
        if isinstance(self.native_frequency, Unset):
            native_frequency = UNSET
        elif isinstance(self.native_frequency, list):
            native_frequency = self.native_frequency

        else:
            native_frequency = self.native_frequency

        credits_: Union[List[str], None, Unset]
        if isinstance(self.credits_, Unset):
            credits_ = UNSET
        elif isinstance(self.credits_, list):
            credits_ = self.credits_

        else:
            credits_ = self.credits_

        native_credits: Union[List[str], None, Unset]
        if isinstance(self.native_credits, Unset):
            native_credits = UNSET
        elif isinstance(self.native_credits, list):
            native_credits = self.native_credits

        else:
            native_credits = self.native_credits

        performers: Union[List[str], None, Unset]
        if isinstance(self.performers, Unset):
            performers = UNSET
        elif isinstance(self.performers, list):
            performers = self.performers

        else:
            performers = self.performers

        native_performers: Union[List[str], None, Unset]
        if isinstance(self.native_performers, Unset):
            native_performers = UNSET
        elif isinstance(self.native_performers, list):
            native_performers = self.native_performers

        else:
            native_performers = self.native_performers

        availability = self.availability

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        volumes: Union[List[str], None, Unset]
        if isinstance(self.volumes, Unset):
            volumes = UNSET
        elif isinstance(self.volumes, list):
            volumes = self.volumes

        else:
            volumes = self.volumes

        title = self.title

        native_title: Union[None, Unset, str]
        if isinstance(self.native_title, Unset):
            native_title = UNSET
        else:
            native_title = self.native_title

        series_title: Union[List[str], None, Unset]
        if isinstance(self.series_title, Unset):
            series_title = UNSET
        elif isinstance(self.series_title, list):
            series_title = self.series_title

        else:
            series_title = self.series_title

        native_series_title: Union[List[str], None, Unset]
        if isinstance(self.native_series_title, Unset):
            native_series_title = UNSET
        elif isinstance(self.native_series_title, list):
            native_series_title = self.native_series_title

        else:
            native_series_title = self.native_series_title

        author = self.author

        native_author: Union[None, Unset, str]
        if isinstance(self.native_author, Unset):
            native_author = UNSET
        else:
            native_author = self.native_author

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "format": format_,
            }
        )
        if brn is not UNSET:
            field_dict["brn"] = brn
        if digital_id is not UNSET:
            field_dict["digitalId"] = digital_id
        if other_titles is not UNSET:
            field_dict["otherTitles"] = other_titles
        if native_other_titles is not UNSET:
            field_dict["nativeOtherTitles"] = native_other_titles
        if variant_titles is not UNSET:
            field_dict["variantTitles"] = variant_titles
        if native_variant_titles is not UNSET:
            field_dict["nativeVariantTitles"] = native_variant_titles
        if other_authors is not UNSET:
            field_dict["otherAuthors"] = other_authors
        if native_other_authors is not UNSET:
            field_dict["nativeOtherAuthors"] = native_other_authors
        if isbns is not UNSET:
            field_dict["isbns"] = isbns
        if issns is not UNSET:
            field_dict["issns"] = issns
        if edition is not UNSET:
            field_dict["edition"] = edition
        if native_edition is not UNSET:
            field_dict["nativeEdition"] = native_edition
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if native_publisher is not UNSET:
            field_dict["nativePublisher"] = native_publisher
        if publish_date is not UNSET:
            field_dict["publishDate"] = publish_date
        if subjects is not UNSET:
            field_dict["subjects"] = subjects
        if physical_description is not UNSET:
            field_dict["physicalDescription"] = physical_description
        if native_physical_description is not UNSET:
            field_dict["nativePhysicalDescription"] = native_physical_description
        if summary is not UNSET:
            field_dict["summary"] = summary
        if native_summary is not UNSET:
            field_dict["nativeSummary"] = native_summary
        if contents is not UNSET:
            field_dict["contents"] = contents
        if native_contents is not UNSET:
            field_dict["nativeContents"] = native_contents
        if thesis is not UNSET:
            field_dict["thesis"] = thesis
        if native_thesis is not UNSET:
            field_dict["nativeThesis"] = native_thesis
        if notes is not UNSET:
            field_dict["notes"] = notes
        if native_notes is not UNSET:
            field_dict["nativeNotes"] = native_notes
        if allow_reservation is not UNSET:
            field_dict["allowReservation"] = allow_reservation
        if is_restricted is not UNSET:
            field_dict["isRestricted"] = is_restricted
        if active_reservations_count is not UNSET:
            field_dict["activeReservationsCount"] = active_reservations_count
        if audience is not UNSET:
            field_dict["audience"] = audience
        if audience_imda is not UNSET:
            field_dict["audienceImda"] = audience_imda
        if language is not UNSET:
            field_dict["language"] = language
        if serial is not UNSET:
            field_dict["serial"] = serial
        if volume_note is not UNSET:
            field_dict["volumeNote"] = volume_note
        if native_volume_note is not UNSET:
            field_dict["nativeVolumeNote"] = native_volume_note
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if native_frequency is not UNSET:
            field_dict["nativeFrequency"] = native_frequency
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if native_credits is not UNSET:
            field_dict["nativeCredits"] = native_credits
        if performers is not UNSET:
            field_dict["performers"] = performers
        if native_performers is not UNSET:
            field_dict["nativePerformers"] = native_performers
        if availability is not UNSET:
            field_dict["availability"] = availability
        if source is not UNSET:
            field_dict["source"] = source
        if volumes is not UNSET:
            field_dict["volumes"] = volumes
        if title is not UNSET:
            field_dict["title"] = title
        if native_title is not UNSET:
            field_dict["nativeTitle"] = native_title
        if series_title is not UNSET:
            field_dict["seriesTitle"] = series_title
        if native_series_title is not UNSET:
            field_dict["nativeSeriesTitle"] = native_series_title
        if author is not UNSET:
            field_dict["author"] = author
        if native_author is not UNSET:
            field_dict["nativeAuthor"] = native_author

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bib_format import BibFormat

        d = src_dict.copy()
        format_ = BibFormat.from_dict(d.pop("format"))

        brn = d.pop("brn", UNSET)

        def _parse_digital_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        digital_id = _parse_digital_id(d.pop("digitalId", UNSET))

        def _parse_other_titles(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                other_titles_type_0 = cast(List[str], data)

                return other_titles_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        other_titles = _parse_other_titles(d.pop("otherTitles", UNSET))

        def _parse_native_other_titles(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_other_titles_type_0 = cast(List[str], data)

                return native_other_titles_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_other_titles = _parse_native_other_titles(d.pop("nativeOtherTitles", UNSET))

        def _parse_variant_titles(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variant_titles_type_0 = cast(List[str], data)

                return variant_titles_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        variant_titles = _parse_variant_titles(d.pop("variantTitles", UNSET))

        def _parse_native_variant_titles(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_variant_titles_type_0 = cast(List[str], data)

                return native_variant_titles_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_variant_titles = _parse_native_variant_titles(d.pop("nativeVariantTitles", UNSET))

        def _parse_other_authors(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                other_authors_type_0 = cast(List[str], data)

                return other_authors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        other_authors = _parse_other_authors(d.pop("otherAuthors", UNSET))

        def _parse_native_other_authors(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_other_authors_type_0 = cast(List[str], data)

                return native_other_authors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_other_authors = _parse_native_other_authors(d.pop("nativeOtherAuthors", UNSET))

        isbns = cast(List[str], d.pop("isbns", UNSET))

        def _parse_issns(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                issns_type_0 = cast(List[str], data)

                return issns_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        issns = _parse_issns(d.pop("issns", UNSET))

        def _parse_edition(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                edition_type_0 = cast(List[str], data)

                return edition_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        edition = _parse_edition(d.pop("edition", UNSET))

        def _parse_native_edition(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_edition_type_0 = cast(List[str], data)

                return native_edition_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_edition = _parse_native_edition(d.pop("nativeEdition", UNSET))

        publisher = cast(List[str], d.pop("publisher", UNSET))

        def _parse_native_publisher(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_publisher_type_0 = cast(List[str], data)

                return native_publisher_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_publisher = _parse_native_publisher(d.pop("nativePublisher", UNSET))

        publish_date = d.pop("publishDate", UNSET)

        subjects = cast(List[str], d.pop("subjects", UNSET))

        physical_description = cast(List[str], d.pop("physicalDescription", UNSET))

        def _parse_native_physical_description(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_physical_description_type_0 = cast(List[str], data)

                return native_physical_description_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_physical_description = _parse_native_physical_description(d.pop("nativePhysicalDescription", UNSET))

        def _parse_summary(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                summary_type_0 = cast(List[str], data)

                return summary_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_native_summary(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_summary_type_0 = cast(List[str], data)

                return native_summary_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_summary = _parse_native_summary(d.pop("nativeSummary", UNSET))

        def _parse_contents(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contents_type_0 = cast(List[str], data)

                return contents_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        contents = _parse_contents(d.pop("contents", UNSET))

        def _parse_native_contents(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_contents_type_0 = cast(List[str], data)

                return native_contents_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_contents = _parse_native_contents(d.pop("nativeContents", UNSET))

        def _parse_thesis(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                thesis_type_0 = cast(List[str], data)

                return thesis_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        thesis = _parse_thesis(d.pop("thesis", UNSET))

        def _parse_native_thesis(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_thesis_type_0 = cast(List[str], data)

                return native_thesis_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_thesis = _parse_native_thesis(d.pop("nativeThesis", UNSET))

        notes = cast(List[str], d.pop("notes", UNSET))

        def _parse_native_notes(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_notes_type_0 = cast(List[str], data)

                return native_notes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_notes = _parse_native_notes(d.pop("nativeNotes", UNSET))

        allow_reservation = d.pop("allowReservation", UNSET)

        is_restricted = d.pop("isRestricted", UNSET)

        active_reservations_count = d.pop("activeReservationsCount", UNSET)

        def _parse_audience(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                audience_type_0 = cast(List[str], data)

                return audience_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        audience = _parse_audience(d.pop("audience", UNSET))

        def _parse_audience_imda(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                audience_imda_type_0 = cast(List[str], data)

                return audience_imda_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        audience_imda = _parse_audience_imda(d.pop("audienceImda", UNSET))

        language = cast(List[str], d.pop("language", UNSET))

        serial = d.pop("serial", UNSET)

        def _parse_volume_note(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                volume_note_type_0 = cast(List[str], data)

                return volume_note_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        volume_note = _parse_volume_note(d.pop("volumeNote", UNSET))

        def _parse_native_volume_note(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_volume_note_type_0 = cast(List[str], data)

                return native_volume_note_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_volume_note = _parse_native_volume_note(d.pop("nativeVolumeNote", UNSET))

        def _parse_frequency(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                frequency_type_0 = cast(List[str], data)

                return frequency_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        frequency = _parse_frequency(d.pop("frequency", UNSET))

        def _parse_native_frequency(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_frequency_type_0 = cast(List[str], data)

                return native_frequency_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_frequency = _parse_native_frequency(d.pop("nativeFrequency", UNSET))

        def _parse_credits_(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                credits_type_0 = cast(List[str], data)

                return credits_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        credits_ = _parse_credits_(d.pop("credits", UNSET))

        def _parse_native_credits(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_credits_type_0 = cast(List[str], data)

                return native_credits_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_credits = _parse_native_credits(d.pop("nativeCredits", UNSET))

        def _parse_performers(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                performers_type_0 = cast(List[str], data)

                return performers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        performers = _parse_performers(d.pop("performers", UNSET))

        def _parse_native_performers(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_performers_type_0 = cast(List[str], data)

                return native_performers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_performers = _parse_native_performers(d.pop("nativePerformers", UNSET))

        availability = d.pop("availability", UNSET)

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_volumes(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                volumes_type_0 = cast(List[str], data)

                return volumes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        volumes = _parse_volumes(d.pop("volumes", UNSET))

        title = d.pop("title", UNSET)

        def _parse_native_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        native_title = _parse_native_title(d.pop("nativeTitle", UNSET))

        def _parse_series_title(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                series_title_type_0 = cast(List[str], data)

                return series_title_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        series_title = _parse_series_title(d.pop("seriesTitle", UNSET))

        def _parse_native_series_title(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                native_series_title_type_0 = cast(List[str], data)

                return native_series_title_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        native_series_title = _parse_native_series_title(d.pop("nativeSeriesTitle", UNSET))

        author = d.pop("author", UNSET)

        def _parse_native_author(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        native_author = _parse_native_author(d.pop("nativeAuthor", UNSET))

        new_arrival_title = cls(
            format_=format_,
            brn=brn,
            digital_id=digital_id,
            other_titles=other_titles,
            native_other_titles=native_other_titles,
            variant_titles=variant_titles,
            native_variant_titles=native_variant_titles,
            other_authors=other_authors,
            native_other_authors=native_other_authors,
            isbns=isbns,
            issns=issns,
            edition=edition,
            native_edition=native_edition,
            publisher=publisher,
            native_publisher=native_publisher,
            publish_date=publish_date,
            subjects=subjects,
            physical_description=physical_description,
            native_physical_description=native_physical_description,
            summary=summary,
            native_summary=native_summary,
            contents=contents,
            native_contents=native_contents,
            thesis=thesis,
            native_thesis=native_thesis,
            notes=notes,
            native_notes=native_notes,
            allow_reservation=allow_reservation,
            is_restricted=is_restricted,
            active_reservations_count=active_reservations_count,
            audience=audience,
            audience_imda=audience_imda,
            language=language,
            serial=serial,
            volume_note=volume_note,
            native_volume_note=native_volume_note,
            frequency=frequency,
            native_frequency=native_frequency,
            credits_=credits_,
            native_credits=native_credits,
            performers=performers,
            native_performers=native_performers,
            availability=availability,
            source=source,
            volumes=volumes,
            title=title,
            native_title=native_title,
            series_title=series_title,
            native_series_title=native_series_title,
            author=author,
            native_author=native_author,
        )

        return new_arrival_title
