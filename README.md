/api/v1/user

    - GET: returns list of all users

    ----
    Example:
        /api/v1/user

    RESPONSE:
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
        {
            "id": 1,
            "login": "user1",
            "sex": "male",
            "birth_date": "2000-09-12",
            "groups": [
                3
            ]
        },
        {
            "id": 2,
            "login": "user2",
            "sex": "female",
            "birth_date": "1990-11-10",
            "groups": [
                3,
                2
            ]
        },
        {
            "id": 3,
            "login": "user3",
            "sex": "male",
            "birth_date": "2000-09-12",
            "groups": [
                3,
                2,
            ]
        }
        ]
    }
    ----------

    - POST: creates a new user

    -------
    Example:
        /api/v1/user

    REQUEST:
    {
        "name": "User1",
        "sex": "male",
        "birth_date": “2001-01-01”
    }

    RESPONSE:
    {
        "id": 1,
        "login": "User1",
        "sex": "male",
        "birth_date": "2001-01-01",
        "groups": []
    }
    -----

/api/v1/user/<user_id>

    - GET: returns information about a specific user

    -----
    Example:
        /api/v1/user/13    
    
    RESPONSE:
    {
        "id": 13,
        "login": "user13",
        "sex": "female",
        "birth_date": "2002-09-21",
        "groups": [
            3
        ]
    }
    -----

    - PATCH: update user

    -----
    Example:
        /api/v1/user/13
    
    REQUEST:
        {
            "sex": "male",
            "login": "User 13"
        }

    RESPONSE:
    {
        "id": 13,
        "login": "User 13",
        "sex": "male",
        "birth_date": "2002-09-21",
        "groups": [
            3
        ]
    }
    -----

    - DELETE: delete user

/api/v1/group

    - GET: returns list of all groups

    ----
    Example of Response:
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "group 1",
                "public": true
            },
            {
                "id": 2,
                "name": "group 2",
                "public": false
            },
            {
                "id": 3,
                "name": "group 3",
                "public": true
            },
        ]
    }
    ----------

    - POST: creates a new group
    
    -----
    Example of REQUEST body for adding group:
    {
        "name": "Group 1",
        "public": true
    }

    Example of RESPONSE:
    {
        "id": 1,
        "name": "Group 1",
        "public": true
    }
    -----

/api/v1/group/<group_id>

    - GET: returns information about a specific group

    -----
    Example:
        /api/v1/group/1

    RESPONSE:
        {
            "id": 1,
            "name": "group 1",
            "public": true
        }
    -----

    - PATCH: update group

    -----
    Example:
        /api/v1/group/1

    REQUEST:
        {
            "public": false
        }

    RESPONSE:
        {
            "id": 1,
            "name": "group 1",
            "public": false
        }
    -----

    - DELETE: delete group


/api/v1/group/<group_id>/users 
    
    - GET: returns list of all users in specific group

    ------
    Example:
        /api/v1/group/2/users

    RESPONSE:
    [
    {
        "id": 15,
        "login": "user15",
        "sex": "female",
        "birth_date": "1990-11-10",
        "groups": [
            3,
            2
        ]
    },
    {
        "id": 16,
        "login": "user16",
        "sex": "male",
        "birth_date": "2000-09-12",
        "groups": [
            3,
            2
        ]
    }
    ]
    ------

    - POST: add user to the group
    
    ------
    Example:
        /api/v1/group/2/users

    REQUEST:
        {
            "user": 13
        }

    RESPONSE:
        {
            "success": 200
        }

/api/v1/group/<group_id>/users/<user_id>
    
    - GET: returns information about a user in the group

    ------
    Example:
        /api/v1/group/2/users/13

    RESPONSE:
    {
        "id": 13,
        "login": "User 13",
        "sex": "male",
        "birth_date": "2002-09-21",
        "groups": [
            3,
            2
        ]
    }

    - DELETE: delete user from the group

    ------
    Example:
        /api/v1/group/2/users/13

     RESPONSE:
        {
            "success": 200
        }