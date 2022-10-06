from urllib import request
from src.feature_8 import feature_8

def test_list_data_known_user_returns_non_empty_list():
    request = {
        'title' : None,
        'order' : None,
        'order_by' : None,
        'genre' : None,
        'release_date' : None,
        'tag' : None,
        'rating' : 'all',
        'user' : 609,
    }

    data = feature_8(request)
    expected_result = [
        {
            "title": "Toy Story",
            "release_date": "1995",
            "genres": [
                "Adventure",
                "Animation",
                "Children",
                "Comedy",
                "Fantasy"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:10:25 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "GoldenEye",
            "release_date": "1995",
            "genres": [
                "Action",
                "Adventure",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:08:57 PM",
                    "rating": "4.0"
                }
            ]
        },
        {
            "title": "Braveheart",
            "release_date": "1995",
            "genres": [
                "Action",
                "Drama",
                "War"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:09:50 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Anne Frank Remembered",
            "release_date": "1995",
            "genres": [
                "Documentary"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:10:25 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Man of the Year",
            "release_date": "1995",
            "genres": [
                "Documentary"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:10:54 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Apollo 13",
            "release_date": "1995",
            "genres": [
                "Adventure",
                "Drama",
                "IMAX"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:06:42 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Crimson Tide",
            "release_date": "1995",
            "genres": [
                "Drama",
                "Thriller",
                "War"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:08:57 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Net, The",
            "release_date": "1995",
            "genres": [
                "Action",
                "Crime",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:08:57 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Waterworld",
            "release_date": "1995",
            "genres": [
                "Action",
                "Adventure",
                "Sci-Fi"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:08:57 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Dumb & Dumber (Dumb and Dumber)",
            "release_date": "1994",
            "genres": [
                "Adventure",
                "Comedy"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:07:49 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Interview with the Vampire: The Vampire Chronicles",
            "release_date": "1994",
            "genres": [
                "Drama",
                "Horror"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:09:50 PM",
                    "rating": "4.0"
                }
            ]
        },
        {
            "title": "Natural Born Killers",
            "release_date": "1994",
            "genres": [
                "Action",
                "Crime",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:09:50 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Outbreak",
            "release_date": "1995",
            "genres": [
                "Action",
                "Drama",
                "Sci-Fi",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:08:27 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Pulp Fiction",
            "release_date": "1994",
            "genres": [
                "Comedy",
                "Crime",
                "Drama",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:06:42 PM",
                    "rating": "4.0"
                }
            ]
        },
        {
            "title": "Shawshank Redemption, The",
            "release_date": "1994",
            "genres": [
                "Crime",
                "Drama"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:08:27 PM",
                    "rating": "4.0"
                }
            ]
        },
        {
            "title": "Star Trek: Generations",
            "release_date": "1994",
            "genres": [
                "Adventure",
                "Drama",
                "Sci-Fi"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:08:27 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "While You Were Sleeping",
            "release_date": "1995",
            "genres": [
                "Comedy",
                "Romance"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:08:57 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Forrest Gump",
            "release_date": "1994",
            "genres": [
                "Comedy",
                "Drama",
                "Romance",
                "War"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:07:49 PM",
                    "rating": "4.0"
                }
            ]
        },
        {
            "title": "Cliffhanger",
            "release_date": "1993",
            "genres": [
                "Action",
                "Adventure",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:08:27 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Firm, The",
            "release_date": "1993",
            "genres": [
                "Drama",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:09:50 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Fugitive, The",
            "release_date": "1993",
            "genres": [
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:07:23 PM",
                    "rating": "4.0"
                }
            ]
        },
        {
            "title": "Jurassic Park",
            "release_date": "1993",
            "genres": [
                "Action",
                "Adventure",
                "Sci-Fi",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:08:27 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Terminator 2: Judgment Day",
            "release_date": "1991",
            "genres": [
                "Action",
                "Sci-Fi"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:09:50 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Dances with Wolves",
            "release_date": "1990",
            "genres": [
                "Adventure",
                "Drama",
                "Western"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:06:42 PM",
                    "rating": "4.0"
                }
            ]
        },
        {
            "title": "Batman",
            "release_date": "1989",
            "genres": [
                "Action",
                "Crime",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:06:42 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Jane Eyre",
            "release_date": "1996",
            "genres": [
                "Drama",
                "Romance"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:10:25 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Moll Flanders",
            "release_date": "1996",
            "genres": [
                "Drama"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:11:20 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Heaven's Prisoners",
            "release_date": "1996",
            "genres": [
                "Crime",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:10:25 PM",
                    "rating": "4.0"
                }
            ]
        },
        {
            "title": "Thinner",
            "release_date": "1996",
            "genres": [
                "Horror",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:10:54 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Eraser",
            "release_date": "1996",
            "genres": [
                "Action",
                "Drama",
                "Thriller"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:10:25 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Adventures of Pinocchio, The",
            "release_date": "1996",
            "genres": [
                "Adventure",
                "Children"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:10:54 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "High School High",
            "release_date": "1996",
            "genres": [
                "Comedy"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:11:20 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Twelfth Night",
            "release_date": "1996",
            "genres": [
                "Comedy",
                "Drama",
                "Romance"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:11:20 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Jude",
            "release_date": "1996",
            "genres": [
                "Drama"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:11:20 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "William Shakespeare's Romeo + Juliet",
            "release_date": "1996",
            "genres": [
                "Drama",
                "Romance"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:10:54 PM",
                    "rating": "3.0"
                }
            ]
        },
        {
            "title": "Return of Martin Guerre, The (Retour de Martin Guerre, Le)",
            "release_date": "1982",
            "genres": [
                "Drama"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:10:54 PM",
                    "rating": "4.0"
                }
            ]
        },
        {
            "title": "Tin Drum, The (Blechtrommel, Die)",
            "release_date": "1979",
            "genres": [
                "Drama",
                "War"
            ],
            "ratings": [
                {
                    "date_time": "Tuesday, November 11, 1996 3:11:20 PM",
                    "rating": "4.0"
                }
            ]
        }
    ]

    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'
    assert len(data) > 0, 'expected non empty list'
    assert data == expected_result, 'The result is not correct'


def test_list_data_not_exist_user_returns_empty_list():
    request = {
        'title' : None,
        'order' : None,
        'order_by' : None,
        'genre' : None,
        'release_date' : None,
        'tag' : None,
        'rating' : 'all',
        'user' : 1000,
    }
    data = feature_8(request)
    assert data is not None, 'expected non null list'
    assert type(data) is list, 'expected a list'
    assert len(data) == 0, 'expected empty list'