import logging
from unittest import TestCase

from data import MovieSearchResult
from tables.builders import MovieSearchTableBuilder
from tables.rows.builders import MovieSearchRowBuilder

logging.basicConfig(level=logging.DEBUG)


class IntegrationTest(TestCase):
    movie_search_result = MovieSearchResult(name="name",
                                            year="year",
                                            rotten_tomatoes_score=1,
                                            cast=["Jae", "Baebae"])
    another_movie_search_result = MovieSearchResult(name="another name",
                                                    year="another year",
                                                    rotten_tomatoes_score=100,
                                                    cast=["Another Jae", "Another Baebae"])
    movies = [another_movie_search_result, movie_search_result]
    table_builder = MovieSearchTableBuilder(MovieSearchRowBuilder())

    def test_should_return_table_output(self):
        expected = """(0lqqqqqqqqqqqqqqwqqqqqqqwqqqqqqqqqqqqqqwqqqqqqqqqqqqqqqqk(B
(0x(B [4m[1mFilm[0m         (0x(B [4m[1mScore[0m (0x(B     [4m[1mYear[0m     (0x(B [4m[1mCast[0m           (0x(B
(0tqqqqqqqqqqqqqqnqqqqqqqnqqqqqqqqqqqqqqnqqqqqqqqqqqqqqqqu(B
(0x(B [1manother name[0m (0x(B [31m100% [0m (0x(B another year (0x(B Another Jae    (0x(B
(0x(B              (0x(B       (0x(B              (0x(B Another Baebae (0x(B
(0tqqqqqqqqqqqqqqnqqqqqqqnqqqqqqqqqqqqqqnqqqqqqqqqqqqqqqqu(B
(0x(B [1mname[0m         (0x(B [36m1% [0m   (0x(B     year     (0x(B Jae            (0x(B
(0x(B              (0x(B       (0x(B              (0x(B Baebae         (0x(B
(0mqqqqqqqqqqqqqqvqqqqqqqvqqqqqqqqqqqqqqvqqqqqqqqqqqqqqqqj(B"""
        output = self.table_builder.build(self.movies)

        logging.debug("Expected Movie Search Table:\n{expected}".format(expected=expected))
        logging.debug("Actual Movie Search Table:\n{output}".format(output=output))

        self.assertEqual(expected, output)

