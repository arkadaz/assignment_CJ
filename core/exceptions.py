class MysticaException(Exception):
    """Base exception for Mystica Oracle"""

    pass


class ExtractionError(MysticaException):
    """Error during message extraction"""

    pass


class FortuneGenerationError(MysticaException):
    """Error during fortune generation"""

    pass


class HandprintAnalysisError(MysticaException):
    """Error during handprint analysis"""

    pass


class ProductRecommendationError(MysticaException):
    """Error during product recommendation"""

    pass


class WorkflowError(MysticaException):
    """Error in workflow orchestration"""

    pass
