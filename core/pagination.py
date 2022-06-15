from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = "page_size"
    max_page_size = 10000


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


"""
The PageNumberPagination class includes a number of attributes that may be overridden to modify the pagination style.

To set these attributes you should override the PageNumberPagination class, and then enable your custom pagination class as above.

django_paginator_class - The Django Paginator class to use. Default is django.core.paginator.Paginator, which should be fine for most use cases.
page_size - A numeric value indicating the page size. If set, this overrides the PAGE_SIZE setting. Defaults to the same value as the PAGE_SIZE settings key.
page_query_param - A string value indicating the name of the query parameter to use for the pagination control.
page_size_query_param - If set, this is a string value indicating the name of a query parameter that allows the client to set the page size on a per-request basis. Defaults to None, indicating that the client may not control the requested page size.
max_page_size - If set, this is a numeric value indicating the maximum allowable requested page size. This attribute is only valid if page_size_query_param is also set.
last_page_strings - A list or tuple of string values indicating values that may be used with the page_query_param to request the final page in the set. Defaults to ('last',)
template - The name of a template to use when rendering pagination controls in the browsable API. May be overridden to modify the rendering style, or set to None to disable HTML pagination controls completely. Defaults to "rest_framework/pagination/numbers.html".
"""
