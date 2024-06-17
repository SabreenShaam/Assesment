# Project Setup Guidelines

#### Assumptions
- Used inbuilt login provided by Django Rest Framework.
- Player height in cm.

### Technologies Used

- Python 3.12 with Django Rest framework
- Sqlite db
- Pytest

#### Covered
- Backend development only completed.
- Added all the endpoints mentioned in the assessment guidelines.
- Followed python best practices as much possible.
- Exception handled.
- Pagination added.
- Validation added as much possible.
- Pytest added for happy path.
- Added management command to generate sample data using Faker lib.

#### Prerequisites
- Docker & docker-compose

#### To Setup and Start
```
  docker-compose up --build
  docker-compose exec web python manage.py inject_data
```

#### Note-1: 
- Better to use inbuilt Django Rest Framework UI, where we have all the facility & easy to use.

#### Note-2: 
- If you use postman,
1. Make get call to `http://127.0.0.1:8000/api-auth/login` endpoint and get csrftoken from cookies.
2. Again make get call to `http://127.0.0.1:8000/api-auth/login` endpoint with username, password & csrftoken in Body form data.
3. Now you can call your endpoint (eg `http://127.0.0.1:8000/scorecard`) by giving username & password in Authorization BasicAuth section.

#### Note-3: 
- Create a superuser with command or migration file.
- In the app we have 3 type os user namely Admin, Coach & Player
- All the users' password has been hardcoded as 'password' to make test easier.
- Admin username is set to 'admin177' & password is 'password'
- You can log in by using superuser credentials & view the all the models & data from the admin panel.


#### Endpoints with description

- View available urls in the app
- `http://127.0.0.1:8000`


- Login
- `http://127.0.0.1:8000/api-auth/login/`


1) View Scorecard
- endpoint
- `http://127.0.0.1:8000/scorecard`
- Request Curl
- `curl --location --request GET 'http://127.0.0.1:8000/scorecard' \
--header 'Authorization: Basic YWRtaW4xNzc6cGFzc3dvcmQ=' \
--header 'Cookie: csrftoken=FpBFbRAThCPZFHxKlNg3fMRNDuPoD660' \
--form 'username="admin177"' \
--form 'password="password"' \
--form 'csrfmiddliewaretoken="FpBFbRAThCPZFHxKlNg3fMRNDuPoD660"'`
- Response
- `{
    "game": [
        {
            "id": 1,
            "host_score": 60,
            "guest_score": 54,
            "round_number": "QF",
            "host": {
                "id": 2,
                "name": "car-food-become"
            },
            "guest": {
                "id": 1,
                "name": "wrong-way-reflect"
            },
            "winner": {
                "id": 2,
                "name": "car-food-become"
            }
        },
        {
            "id": 2,
            "host_score": 46,
            "guest_score": 69,
            "round_number": "QF",
            "host": {
                "id": 4,
                "name": "employee-husband"
            },
            "guest": {
                "id": 3,
                "name": "light-yes"
            },
            "winner": {
                "id": 3,
                "name": "light-yes"
            }
        },
        {
            "id": 3,
            "host_score": 37,
            "guest_score": 48,
            "round_number": "QF",
            "host": {
                "id": 6,
                "name": "other-company"
            },
            "guest": {
                "id": 5,
                "name": "mission-less"
            },
            "winner": {
                "id": 5,
                "name": "mission-less"
            }
        },
        {
            "id": 4,
            "host_score": 51,
            "guest_score": 134,
            "round_number": "QF",
            "host": {
                "id": 8,
                "name": "without-black-early"
            },
            "guest": {
                "id": 7,
                "name": "especially-per"
            },
            "winner": {
                "id": 7,
                "name": "especially-per"
            }
        },
        {
            "id": 5,
            "host_score": 82,
            "guest_score": 179,
            "round_number": "QF",
            "host": {
                "id": 10,
                "name": "laugh-other-moment"
            },
            "guest": {
                "id": 9,
                "name": "particular-describe"
            },
            "winner": {
                "id": 9,
                "name": "particular-describe"
            }
        },
        {
            "id": 6,
            "host_score": 44,
            "guest_score": 132,
            "round_number": "QF",
            "host": {
                "id": 12,
                "name": "ever-so-walk-name"
            },
            "guest": {
                "id": 11,
                "name": "science-partner"
            },
            "winner": {
                "id": 11,
                "name": "science-partner"
            }
        },
        {
            "id": 7,
            "host_score": 153,
            "guest_score": 107,
            "round_number": "QF",
            "host": {
                "id": 14,
                "name": "foot-tree-cause"
            },
            "guest": {
                "id": 13,
                "name": "number-here-pm"
            },
            "winner": {
                "id": 14,
                "name": "foot-tree-cause"
            }
        },
        {
            "id": 8,
            "host_score": 168,
            "guest_score": 25,
            "round_number": "QF",
            "host": {
                "id": 16,
                "name": "election-sure"
            },
            "guest": {
                "id": 15,
                "name": "movement-drug"
            },
            "winner": {
                "id": 16,
                "name": "election-sure"
            }
        },
        {
            "id": 9,
            "host_score": 28,
            "guest_score": 163,
            "round_number": "SF",
            "host": {
                "id": 3,
                "name": "light-yes"
            },
            "guest": {
                "id": 2,
                "name": "car-food-become"
            },
            "winner": {
                "id": 2,
                "name": "car-food-become"
            }
        },
        {
            "id": 10,
            "host_score": 47,
            "guest_score": 159,
            "round_number": "SF",
            "host": {
                "id": 7,
                "name": "especially-per"
            },
            "guest": {
                "id": 5,
                "name": "mission-less"
            },
            "winner": {
                "id": 5,
                "name": "mission-less"
            }
        },
        {
            "id": 11,
            "host_score": 168,
            "guest_score": 54,
            "round_number": "SF",
            "host": {
                "id": 11,
                "name": "science-partner"
            },
            "guest": {
                "id": 9,
                "name": "particular-describe"
            },
            "winner": {
                "id": 11,
                "name": "science-partner"
            }
        },
        {
            "id": 12,
            "host_score": 114,
            "guest_score": 80,
            "round_number": "SF",
            "host": {
                "id": 16,
                "name": "election-sure"
            },
            "guest": {
                "id": 14,
                "name": "foot-tree-cause"
            },
            "winner": {
                "id": 16,
                "name": "election-sure"
            }
        },
        {
            "id": 13,
            "host_score": 25,
            "guest_score": 143,
            "round_number": "FI",
            "host": {
                "id": 5,
                "name": "mission-less"
            },
            "guest": {
                "id": 2,
                "name": "car-food-become"
            },
            "winner": {
                "id": 2,
                "name": "car-food-become"
            }
        },
        {
            "id": 14,
            "host_score": 133,
            "guest_score": 132,
            "round_number": "FI",
            "host": {
                "id": 16,
                "name": "election-sure"
            },
            "guest": {
                "id": 11,
                "name": "science-partner"
            },
            "winner": {
                "id": 16,
                "name": "election-sure"
            }
        },
        {
            "id": 15,
            "host_score": 160,
            "guest_score": 156,
            "round_number": "WI",
            "host": {
                "id": 16,
                "name": "election-sure"
            },
            "guest": {
                "id": 2,
                "name": "car-food-become"
            },
            "winner": {
                "id": 16,
                "name": "election-sure"
            }
        }
    ],
    "user": {
        "id": 177,
        "is_logged_in": true,
        "role": {
            "id": 1,
            "type": "A"
        }
    }
}`

2) View Player List(Paginated)
- endpoint
- `http://127.0.0.1:8000/player` or `http://127.0.0.1:8000/player?page=1`
- Request Curl
- `curl --location --request GET 'http://127.0.0.1:8000/player' \
--header 'Authorization: Basic YWRtaW4xNzc6cGFzc3dvcmQ=' \
--header 'Cookie: csrftoken=FpBFbRAThCPZFHxKlNg3fMRNDuPoD660' \
--form 'username="admin177"' \
--form 'password="password"' \
--form 'csrfmiddliewaretoken="FpBFbRAThCPZFHxKlNg3fMRNDuPoD660"'`
- Response
- `[
    {
        "id": 1,
        "full_name": "Jonathan Hall",
        "team": "wrong-way-reflect"
    },
    {
        "id": 2,
        "full_name": "Austin Patrick",
        "team": "wrong-way-reflect"
    },
    {
        "id": 3,
        "full_name": "Karen Peterson",
        "team": "wrong-way-reflect"
    },
    {
        "id": 4,
        "full_name": "Amanda Rodriguez",
        "team": "wrong-way-reflect"
    },
    {
        "id": 5,
        "full_name": "Mark White",
        "team": "wrong-way-reflect"
    },
    {
        "id": 6,
        "full_name": "Melissa Sanchez",
        "team": "wrong-way-reflect"
    },
    {
        "id": 7,
        "full_name": "Mandy Harris",
        "team": "wrong-way-reflect"
    },
    {
        "id": 8,
        "full_name": "Kathy Howard",
        "team": "wrong-way-reflect"
    },
    {
        "id": 9,
        "full_name": "Keith Hatfield",
        "team": "wrong-way-reflect"
    },
    {
        "id": 10,
        "full_name": "Wanda Wolf",
        "team": "wrong-way-reflect"
    }
]`



3) View Player Details
- endpoint
- `http://127.0.0.1:8000/player/5`
- Request Curl
- `curl --location --request GET 'http://127.0.0.1:8000/player/5' \
--header 'Authorization: Basic YWRtaW4xNzc6cGFzc3dvcmQ=' \
--header 'Cookie: csrftoken=FpBFbRAThCPZFHxKlNg3fMRNDuPoD660' \
--form 'username="admin177"' \
--form 'password="password"' \
--form 'csrfmiddliewaretoken="FpBFbRAThCPZFHxKlNg3fMRNDuPoD660"'
`
- Redponse
- `{
    "player": "Mark White",
    "player_id": 5,
    "player_height": 241,
    "team": "wrong-way-reflect",
    "games": 1,
    "average_score": 10.0
}`



4) View Team belong to coach
- endpoint
- `http://127.0.0.1:8000/coach/1`
- Request Curl
- Response
- `{
    "team_name": "wrong-way-reflect",
    "average_team_score": 54.0,
    "players": [
        {
            "id": 1,
            "name": "Jonathan Hall"
        },
        {
            "id": 2,
            "name": "Austin Patrick"
        },
        {
            "id": 3,
            "name": "Karen Peterson"
        },
        {
            "id": 4,
            "name": "Amanda Rodriguez"
        },
        {
            "id": 5,
            "name": "Mark White"
        },
        {
            "id": 6,
            "name": "Melissa Sanchez"
        },
        {
            "id": 7,
            "name": "Mandy Harris"
        },
        {
            "id": 8,
            "name": "Kathy Howard"
        },
        {
            "id": 9,
            "name": "Keith Hatfield"
        },
        {
            "id": 10,
            "name": "Wanda Wolf"
        }
    ]
}`

5) View Team List(Paginated)
- endpoint
- `http://127.0.0.1:8000/team` or `http://127.0.0.1:8000/team?page=1`
- Request Curl
- `curl --location --request GET 'http://127.0.0.1:8000/team' \
--header 'Authorization: Basic YWRtaW4xNzc6cGFzc3dvcmQ=' \
--header 'Cookie: csrftoken=FpBFbRAThCPZFHxKlNg3fMRNDuPoD660' \
--form 'username="admin177"' \
--form 'password="password"' \
--form 'csrfmiddliewaretoken="FpBFbRAThCPZFHxKlNg3fMRNDuPoD660"'`
- Response
- `[
    {
        "id": 1,
        "name": "wrong-way-reflect"
    },
    {
        "id": 2,
        "name": "car-food-become"
    },
    {
        "id": 3,
        "name": "light-yes"
    },
    {
        "id": 4,
        "name": "employee-husband"
    },
    {
        "id": 5,
        "name": "mission-less"
    },
    {
        "id": 6,
        "name": "other-company"
    },
    {
        "id": 7,
        "name": "especially-per"
    },
    {
        "id": 8,
        "name": "without-black-early"
    },
    {
        "id": 9,
        "name": "particular-describe"
    },
    {
        "id": 10,
        "name": "laugh-other-moment"
    }
]`



6) View Players in the team
- endpoint
- `http://127.0.0.1:8000/team/1`
- Request Curl
- `curl --location --request GET 'http://127.0.0.1:8000/team/1' \
--header 'Authorization: Basic YWRtaW4xNzc6cGFzc3dvcmQ=' \
--header 'Cookie: csrftoken=FpBFbRAThCPZFHxKlNg3fMRNDuPoD660' \
--form 'username="admin177"' \
--form 'password="password"' \
--form 'csrfmiddliewaretoken="FpBFbRAThCPZFHxKlNg3fMRNDuPoD660"'`
- Response
- `{
    "players": [
        {
            "id": 1,
            "height": 179,
            "user": {
                "id": 1,
                "username": "sarahbuckley1",
                "first_name": "Jonathan",
                "last_name": "Hall",
                "email": "richard70@example.com"
            },
            "team": {
                "id": 1,
                "name": "wrong-way-reflect"
            }
        },
        {
            "id": 2,
            "height": 217,
            "user": {
                "id": 2,
                "username": "kent362",
                "first_name": "Austin",
                "last_name": "Patrick",
                "email": "susan59@example.com"
            },
            "team": {
                "id": 1,
                "name": "wrong-way-reflect"
            }
        },
        {
            "id": 3,
            "height": 200,
            "user": {
                "id": 3,
                "username": "mccarthysarah3",
                "first_name": "Karen",
                "last_name": "Peterson",
                "email": "kanderson@example.net"
            },
            "team": {
                "id": 1,
                "name": "wrong-way-reflect"
            }
        },
        {
            "id": 4,
            "height": 251,
            "user": {
                "id": 4,
                "username": "seth584",
                "first_name": "Amanda",
                "last_name": "Rodriguez",
                "email": "lambertrebecca@example.com"
            },
            "team": {
                "id": 1,
                "name": "wrong-way-reflect"
            }
        },
        {
            "id": 5,
            "height": 241,
            "user": {
                "id": 5,
                "username": "maryharrison5",
                "first_name": "Mark",
                "last_name": "White",
                "email": "zmartinez@example.net"
            },
            "team": {
                "id": 1,
                "name": "wrong-way-reflect"
            }
        },
        {
            "id": 6,
            "height": 206,
            "user": {
                "id": 6,
                "username": "nicolewhite6",
                "first_name": "Melissa",
                "last_name": "Sanchez",
                "email": "mshaw@example.net"
            },
            "team": {
                "id": 1,
                "name": "wrong-way-reflect"
            }
        },
        {
            "id": 7,
            "height": 196,
            "user": {
                "id": 7,
                "username": "gallegosheather7",
                "first_name": "Mandy",
                "last_name": "Harris",
                "email": "tallen@example.com"
            },
            "team": {
                "id": 1,
                "name": "wrong-way-reflect"
            }
        },
        {
            "id": 8,
            "height": 181,
            "user": {
                "id": 8,
                "username": "monroemelissa8",
                "first_name": "Kathy",
                "last_name": "Howard",
                "email": "matthew39@example.com"
            },
            "team": {
                "id": 1,
                "name": "wrong-way-reflect"
            }
        },
        {
            "id": 9,
            "height": 177,
            "user": {
                "id": 9,
                "username": "juansmith9",
                "first_name": "Keith",
                "last_name": "Hatfield",
                "email": "fsmith@example.com"
            },
            "team": {
                "id": 1,
                "name": "wrong-way-reflect"
            }
        },
        {
            "id": 10,
            "height": 178,
            "user": {
                "id": 10,
                "username": "sandy1110",
                "first_name": "Wanda",
                "last_name": "Wolf",
                "email": "andersonangela@example.org"
            },
            "team": {
                "id": 1,
                "name": "wrong-way-reflect"
            }
        }
    ],
    "average_team_score": 54.0
}`

7) View site usage stats
- endpoint
- `http://127.0.0.1:8000/stats`
- Request Curl
- `curl --location --request GET 'http://127.0.0.1:8000/stats' \
--header 'Authorization: Basic YWRtaW4xNzc6cGFzc3dvcmQ=' \
--header 'Cookie: csrftoken=FpBFbRAThCPZFHxKlNg3fMRNDuPoD660' \
--form 'username="admin177"' \
--form 'password="password"' \
--form 'csrfmiddliewaretoken="FpBFbRAThCPZFHxKlNg3fMRNDuPoD660"'`


8) View 90th percentile player in a team
- endpoint
- `http://127.0.0.1:8000/filter/team/1`
- Request Curl
- `curl --location --request GET 'http://127.0.0.1:8000/filter/team/1' \
--header 'Authorization: Basic amVzc2ljYW51bmV6MTc0OnBhc3N3b3Jk' \
--header 'Cookie: csrftoken=FpBFbRAThCPZFHxKlNg3fMRNDuPoD660' \
--form 'username="admin177"' \
--form 'password="password"' \
--form 'csrfmiddliewaretoken="FpBFbRAThCPZFHxKlNg3fMRNDuPoD660"'`
- Response
- `{
    "name": "Mark White",
    "avg_ninety_percentile_score": 10.0,
    "id": 5
}`

9) View the player score percentage in a team
- endpoint
- `http://127.0.0.1:8000/filter/player/7`
- Request Curl
- `curl --location --request GET 'http://127.0.0.1:8000/filter/player/7' \
--header 'Authorization: Basic amVzc2ljYW51bmV6MTc0OnBhc3N3b3Jk' \
--header 'Cookie: csrftoken=FpBFbRAThCPZFHxKlNg3fMRNDuPoD660' \
--form 'username="admin177"' \
--form 'password="password"' \
--form 'csrfmiddliewaretoken="FpBFbRAThCPZFHxKlNg3fMRNDuPoD660"'`
- Response
- `{
    "id": 7,
    "full_name": "Mandy Harris",
    "team": "wrong-way-reflect",
    "score_percentage": 16.666666666666664
}`