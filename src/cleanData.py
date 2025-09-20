import re

HEADER_PATTERN = '^@.*\n'
UTTERNANCE_INFO_PATTERN = '^%.*'
SPEAKER_TAG_PATTERN = '^\\*.*:'
REPLACE_WITH_IS_PATTERN = r"\b(?:he|she|it|what|that|this|there|who|where|when|how)'s\b"
REPEAT_PATTERN = r'\b([a-zA-Z])\1+\b'


def removeHeaders(fileStr):
    cleaned = re.sub(HEADER_PATTERN, "", fileStr, flags=re.MULTILINE)
    return cleaned


def removeUtternaceInfo(fileStr):
    cleaned = re.sub(UTTERNANCE_INFO_PATTERN, "", fileStr, flags=re.MULTILINE)
    return cleaned


def removeSpeakerTag(fileStr):
    cleaned = re.sub(SPEAKER_TAG_PATTERN, "", fileStr, flags=re.MULTILINE)
    return cleaned


def removeSpecialChar(fileStr):
    specialCharRange = []
    controlCharRange = []
    controlCharRange.extend(range(0, 31))
    specialCharRange.extend(range(35, 38))
    specialCharRange.extend(range(40, 43))
    specialCharRange.append(45)
    specialCharRange.append(46)
    specialCharRange.extend(range(47, 57))
    specialCharRange.extend(range(59, 62))
    specialCharRange.append(63)
    specialCharRange.append(64)
    specialCharRange.extend(range(91, 96))
    specialCharRange.extend(range(123, 126))
    specialCharRange.extend(range(166, 180))
    specialCharRange.extend(range(184, 197))
    specialCharRange.extend(range(200, 206))
    specialCharRange.extend(range(217, 221))
    specialCharRange.append(223)
    specialCharRange.extend(range(238, 255))

    cleaned = fileStr
    for controlChar in controlCharRange:
        # remove texts between special characters
        controlCharPattern = "{control}.*?{control}".format(control=re.escape(chr(controlChar)))
        cleaned = re.sub(controlCharPattern, "", cleaned, flags=re.MULTILINE)

    for specialChar in specialCharRange:
        # remove single special characters
        cleaned = re.sub(re.escape(chr(specialChar)), "", cleaned, flags=re.MULTILINE)

    return cleaned

#def replaceConstraction(fileStr):
    # cleaned = re.sub(REPLACE_WITH_IS_PATTERN, " ", fileStr, flags=re.MULTILINE)
    return re.sub(REPLACE_WITH_IS_PATTERN, lambda m: m.group(0)[:-2] + " is", fileStr, flags=re.IGNORECASE)
    return cleaned

def removeRepeats(fileStr):
    cleaned = re.sub(REPEAT_PATTERN, "", fileStr, flags=re.MULTILINE | re.IGNORECASE)
    return cleaned

#fake change 2