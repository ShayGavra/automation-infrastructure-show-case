PLACEHOLDER_BASE_URL  = "https://jsonplaceholder.typicode.com/"

POSTS_ENDPOINT = "/posts"

NOT_FOUND = 404

POST_ID = 99

INVALID_ENDPOINT= "/posts_invalid"

STATUS_OK = 200

POST_KEYS = ["id", "userId", "title", "body"]

STATUS_POST_CREATED = 201

POST_UPDATE_INVALID = {"userId": "abc", "title": 123, "body": ""}

EXPECTED_TYPES = {"id":int, "userId":int, "title":str, "body":str}


POST_1 = {                   # Regular post (Positive Test)
    "title": "Hello JSONPlaceholder",
    "body": "This is a sample post content.",
    "userId": 1
}

EMPTY_PAYLOAD = {    # Post with empty title (Negative Test)
}

POST_LONG_BODY = {            # Post with long body (Boundary Test)
    "title": "Long Post",
    "body": "A" * 1000,      # 1000 characters
    "userId": 1
}

# --- UPDATE ---
POST_UPDATE_FULL = {          # Full update (PUT)
    "title": "Fully Updated",
    "body": "The content has been fully updated.",
    "userId": 1
}

POST_UPDATE_PARTIAL = {       # Partial update (PATCH)
    "title": "Partially Updated"
}

POST_UPDATE_NOT_EXIST = {     # Update non-existing post (Negative Test)
    "title": "Does Not Exist",
    "body": "Trying to update a post that does not exist.",
    "userId": 1
}

# --- IDs for testing ---
POST_DELETE_EXISTING_ID = 1      # For deleting existing post

POST_DELETE_NOT_EXIST_ID = 9999  # For deleting non-existing post

POST_GET_EXISTING_ID = 1         # For getting existing post

INVALID_POST_ID = 9999     # For getting non-existing post