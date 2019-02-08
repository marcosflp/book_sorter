from rest_framework.exceptions import ValidationError


class OrderingParamNotFoundException(ValidationError):
    default_detail = 'You must pass on the querystring the "ordering" param.'


class OrderingFieldNotAllowedException(ValidationError):
    default_detail = 'The ordering value "{field}" is not allowed.'

    def __init__(self, field, detail=None, code=None):
        self.default_detail = self.default_detail.format(field=field)
        super(OrderingFieldNotAllowedException, self).__init__(detail, code)


class CaseInsensitiveValueNotAllowedException(ValidationError):
    default_detail = ('The only values accepted on the query param '
                      '"case_insensitive" is "true" or "false"')
