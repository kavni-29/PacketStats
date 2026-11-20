"""PacketStats custom exceptions.

Provides a structured exception hierarchy for input validation, parsing,
configuration, and report generation errors.
"""


class PacketStatsError(Exception):
    """Base exception for all PacketStats errors."""

    pass


class InvalidCaptureError(PacketStatsError):
    """Raised when a capture file does not exist, is empty, or is unreadable."""

    pass


class UnsupportedCaptureFormatError(PacketStatsError):
    """Raised when a capture file format or magic number is not supported."""

    pass


class ParsingError(PacketStatsError):
    """Raised when critical parsing failures occur on a capture file."""

    pass


class ConfigurationError(PacketStatsError):
    """Raised when detection rule or system configuration parameters are invalid."""

    pass


class ExportError(PacketStatsError):
    """Raised when an error occurs during report or summary export."""

    pass


class AnalysisError(PacketStatsError):
    """Raised when an unrecoverable failure occurs during statistical analysis."""

    pass
