from cas_metadata_tools.base_constants import BaseConstants

class EXIFConstants(BaseConstants):
    # EXIF Constants
    EXIF_ARTIST = "EXIF:Artist"
    EXIF_COPYRIGHT = "EXIF:Copyright"
    EXIF_CREATE_DATE = "EXIF:CreateDate"
    EXIF_IFD0_IMAGE_DESCRIPTION = "EXIF:IFD0:ImageDescription"
    EXIF_IMAGE_DESCRIPTION = "EXIF:ImageDescription"

    # IDF0 constants
    IFD0_COPYRIGHT = "IFD0:Copyright"

    # IPTC Constants
    IPTC_BY_LINE = "IPTC:By-line"
    IPTC_BY_LINE_TITLE = "IPTC:By-lineTitle"
    IPTC_CAPTION_ABSTRACT = "IPTC:Caption-Abstract"
    IPTC_COPYRIGHT_NOTICE = "IPTC:CopyrightNotice"
    IPTC_CREDIT = "IPTC:Credit"
    IPTC_KEYWORDS = "IPTC:Keywords"

    # Photoshop Constants
    PHOTOSHOP_COPYRIGHT_FLAG = "Photoshop:CopyrightFlag"
    PHOTOSHOP_CREDIT = "XMP-photoshop:Credit"

    # XMP Constants
    XMP_CREATE_DATE = "XMP:CreateDate"
    XMP_CREATOR = "XMP:Creator"
    XMP_CREATOR_ADDRESS = "XMP:CreatorAddress"
    XMP_CREATOR_CITY = "XMP:CreatorCity"
    XMP_CREATOR_COUNTRY = "XMP:CreatorCountry"
    XMP_CREATOR_POSTAL_CODE = "XMP:CreatorPostalCode"
    XMP_CREATOR_REGION = "XMP:CreatorRegion"
    XMP_CREATOR_WORK_URL = "XMP:CreatorWorkURL"
    XMP_CREDIT = "XMP:Credit"
    XMP_DATE_CREATED = "XMP:DateCreated"
    XMP_DC_DESCRIPTION = "XMP-dc:Description"
    XMP_DC_SUBJECT = "XMP-dc:Subject"
    XMP_DESCRIPTION = "XMP:Description"
    XMP_LABEL = "XMP:Label"
    XMP_LR_HIERARCHICAL_SUBJECT = "XMP-lr:HierarchicalSubject"
    XMP_PLUS_IMAGE_SUPPLIER_NAME = "XMP-plus:ImageSupplierName"
    XMP_RIGHTS = "XMP:Rights" # this is the same as XMP-dc:Rights
    XMP_RIGHTS_USAGE_TERMS = "XMP-xmpRights:UsageTerms"
    XMP_TITLE = "XMP:Title"
    XMP_USAGE = "XMP:Usage"
    XMP_USAGE_TERMS = "XMP:UsageTerms"
