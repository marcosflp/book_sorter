from django.db import transaction
from django.db.models.functions import Lower
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from core import exceptions
from core.models import Book
from core.serializers import BookCreateSerializer, BookResponseSerializer


class CaseInsensitiveOrderingFilter(OrderingFilter):
    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        if ordering:
            case_insensitive_ordering = []
            for field in ordering:
                if field.startswith('-'):
                    case_insensitive_ordering.append(Lower(field[1:]).desc())
                else:
                    case_insensitive_ordering.append(Lower(field).asc())

            return queryset.order_by(*case_insensitive_ordering)

        return queryset


class BookSorterViewSet(GenericViewSet):
    """
    Book's Sorter ViewSet.

    The approach to sort the books is to use the database to perform the
    ordering. As we don't need to store the books, at the end of each request
    all the books are removed.

    query_params:
        - ordering: 'title', 'order' or 'edition_year'
        - case_insensitive: 'true' or 'false'

        obs: To apply decreasingly order just put a '-' at the beginning of
             each ordering option.

    This View does the following:
        1. Accept only POST requests. Each request must has on the body the
           Book's fields that will be created.
        2. Validates whether the self.request.query_params are valid.
        3. Sets if is a case insensitive ordering.
        4. Sorts the Book's with the fields passed on the param 'ordering`
        5. Creates the response data to be returned to the user
        6. Deletes all the Book's created on each request
    """

    http_method_names = ['post', 'options']
    queryset = Book.objects.none()
    serializer_class = BookCreateSerializer
    ordering_fields = ('title', 'author', 'edition_year')

    books_created_pk = []

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        """
        Handle the creation, ordering, deletion and returning of the ordered
        books.
        """
        self.validates_query_params()

        # Create the books to perform the ordering against.
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Register the created objects id's.
        # Those ids are used on self.get_queryset to filter
        # the objects on the database
        if isinstance(serializer.data, list):
            self.books_created_pk = [book['pk'] for book in serializer.data]
        else:
            self.books_created_pk.append(serializer.data['pk'])

        # Perform the query ordering against the created books
        queryset = self.filter_queryset(self.get_queryset())

        serializer = BookResponseSerializer(queryset, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        # As we don't need to store the books on the database, delete them all!
        queryset.delete()

        return response

    def filter_queryset(self, queryset):
        """
        Given a queryset, filter it with the appropriate backend filter.
        """
        if self.is_ordering_case_insensitive():
            backend = CaseInsensitiveOrderingFilter()
        else:
            backend = OrderingFilter()

        queryset = backend.filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        return Book.objects.filter(pk__in=self.books_created_pk)

    def validates_query_params(self):
        """
        If the `ordering` param is not ok raises an Exception.

        Raises:
             OrderingParamNotFoundException
             OrderingFieldNotAllowedException

        Returns: None
        """
        ordering_param = self.request.query_params.get('ordering')
        if not ordering_param:
            raise exceptions.OrderingParamNotFoundException

        field_list = [param.strip() for param in ordering_param.split(',')]
        for field_name in field_list:
            if field_name.lstrip('-') not in self.ordering_fields:
                raise exceptions.OrderingFieldNotAllowedException(field_name)

        return None

    def is_ordering_case_insensitive(self):
        """
        Check whether the user sets if is a case insensitive ordering.
        """
        case_insensitive = self.request.query_params.get('case_insensitive', '').strip()

        if not case_insensitive or case_insensitive == 'false':
            return False
        elif case_insensitive == 'true':
            return True
        else:
            raise exceptions.CaseInsensitiveValueNotAllowedException
