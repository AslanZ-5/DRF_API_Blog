from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination

)


class PostLimitPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10


class PaginationNumber(PageNumberPagination):
    page_size = 3
