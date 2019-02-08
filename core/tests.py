from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from core.models import Book


class BookTest(APITestCase):

    def setUp(self):
        self.valid_books = [
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002},
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013}
        ]

    # Title field

    def test_it_is_possible_to_sort_books_by_title_asc(self):
        """
        Ensure we can order books by title in ascending order
        """
        url = f"{reverse('book-list')}?ordering=title"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002},
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    def test_it_is_possible_to_sort_books_by_title_desc(self):
        """
        Ensure we can order books by title in descending order
        """
        url = f"{reverse('book-list')}?ordering=-title"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013},
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002},
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    def test_it_is_possible_to_sort_books_by_case_insensitive_title_asc(self):
        """
        Ensure we can order books by case insensitive title in ascending order
        """
        url = f"{reverse('book-list')}?ordering=title&case_insensitive=true"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002},
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    def test_it_is_possible_to_sort_books_by_case_insensitive_title_desc(self):
        """
        Ensure we can order books by case insensitive title in descending order
        """
        url = f"{reverse('book-list')}?ordering=-title&case_insensitive=true"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013},
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002},
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    # Author field

    def test_it_is_possible_to_sort_books_by_author_asc(self):
        """
        Ensure we can order books by author in ascending order
        """
        url = f"{reverse('book-list')}?ordering=author"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002},
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    def test_it_is_possible_to_sort_books_by_author_desc(self):
        """
        Ensure we can order books by author in descending order
        """
        url = f"{reverse('book-list')}?ordering=-author"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013},
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002},
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    def test_it_is_possible_to_sort_books_by_case_insensitive_author_asc(self):
        """
        Ensure we can order books by case insensitive author in asc order
        """
        url = f"{reverse('book-list')}?ordering=author&case_insensitive=true"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013},
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    def test_it_is_possible_to_sort_books_by_case_insensitive_author_desc(self):
        """
        Ensure we can order books by case insensitive author desc order
        """
        url = f"{reverse('book-list')}?ordering=-author&case_insensitive=true"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002},
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    # Edition year field

    def test_it_is_possible_to_sort_books_by_edition_year_asc(self):
        """
        Ensure we can order books by edition year in ascending order
        """
        url = f"{reverse('book-list')}?ordering=edition_year"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002},
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    def test_it_is_possible_to_sort_books_by_edition_year_desc(self):
        """
        Ensure we can order books by edition year in descending order
        """
        url = f"{reverse('book-list')}?ordering=-edition_year"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013},
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    # Multiple fields at once

    def test_it_is_possible_to_sort_by_multiple_fields(self):
        """
        Ensure we can order books by multiple fields
        """
        url = f"{reverse('book-list')}?ordering=-edition_year,-author,title"
        response = self.client.post(url, data=self.valid_books, format='json')

        expected_result = [
            {"title": "thinking, Fast and Slow", "author": "daniel Kahneman", "edition_year": 2013},
            {"title": "Internet & World Wide Web: How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Java How to Program", "author": "Deitel & Deitel", "edition_year": 2007},
            {"title": "Head First Desing Patterns", "author": "Elisabeth Freeman", "edition_year": 2004},
            {"title": "Patterns of Enterprise Application", "author": "Martin Fowler", "edition_year": 2002}
        ]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 0)
        self.assertListEqual(response.json(), expected_result)

    def test_it_is_not_possible_to_sort_by_invalid_field(self):
        """
        Ensure a exception is raised when the user inputs a invalid field to
        sort.
        """
        url = f"{reverse('book-list')}?ordering=name"
        response = self.client.post(url, data=self.valid_books, format='json')

        excepted_result = ['The ordering value "name" is not allowed.']

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.exception)
        self.assertEqual(response.json(), excepted_result)

    def test_it_is_not_possible_to_sort_without_ordering(self):
        """
        Ensure a exception is raised when the user does not input a ordering
        param.
        """
        url = f"{reverse('book-list')}"
        response = self.client.post(url, data=self.valid_books, format='json')

        excepted_result = ['You must pass on the querystring the "ordering" param.']

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue(response.exception)
        self.assertEqual(response.json(), excepted_result)
