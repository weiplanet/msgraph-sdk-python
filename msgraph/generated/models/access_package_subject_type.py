from enum import Enum

class AccessPackageSubjectType(Enum):
    NotSpecified = "notSpecified",
    User = "user",
    ServicePrincipal = "servicePrincipal",
    UnknownFutureValue = "unknownFutureValue",

