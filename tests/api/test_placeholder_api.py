import allure
from data.api.placeholder_posts_data import *
from extensions.api_verifications import APIVerify
from workflows.api.placeholder_posts_workflows import PlaceholderPostsApiFlows




class TestPlaceholderPostsApi:



    @allure.title("Verify user can create a new post successfully")
    @allure.description("Validate that a new post is created successfully and returns status 201 with generated ID.")
    def test01_verify_create_post(self,post_flows:PlaceholderPostsApiFlows):
        response = post_flows.create_post(POST_1)
        response_data = response.json()
        APIVerify.status_code(response,STATUS_POST_CREATED)   
        APIVerify.json_contains(response_data,POST_1)
        APIVerify.json_key_exists(response_data,keys=POST_KEYS)



    @allure.title("Verify GET post by ID")
    @allure.description("Fetch a post by a fixed ID and validate status code and required JSON keys.")
    def test02_verify_get_post_by_id(self,post_flows:PlaceholderPostsApiFlows):
        response = post_flows.get_post_by_id(POST_ID)
        APIVerify.status_code(response,STATUS_OK)
        APIVerify.json_key_exists(response.json(),keys=POST_KEYS)



    @allure.title("Verify GET all posts")
    @allure.description("Fetch all posts, validate status code, ensure response is a list, and check required JSON keys for first 10 posts.")
    def test03_verify_get_all_posts(self,post_flows:PlaceholderPostsApiFlows):
        response = post_flows.get_all_posts()
        APIVerify.status_code(response,STATUS_OK)
        posts = response.json()
        APIVerify.is_list(posts,"Expected a list of posts")
        for post in posts[:10]:
            APIVerify.json_key_exists(post, keys=POST_KEYS)



    @allure.title("Verify partial update of a post (PATCH)")
    @allure.description("Patch the title of an existing post by a fixed ID and validate status code and JSON keys. Fake API, so data is not persisted.")
    def test04_verify_patch_post(self,post_flows:PlaceholderPostsApiFlows):
        response = post_flows.patch_post(POST_GET_EXISTING_ID,POST_UPDATE_PARTIAL)
        APIVerify.status_code(response,STATUS_OK)
        APIVerify.json_key_exists(response.json(),keys=POST_KEYS)
        APIVerify.json_contains(response.json(),POST_UPDATE_PARTIAL)
    


    @allure.title("Verify PATCH with invalid payload on existing post")
    @allure.description("Send PATCH request with invalid payload to an existing post ID, validate status code, JSON keys, and value types.")
    def test05_verify_patch_invalid_payload(self,post_flows:PlaceholderPostsApiFlows):
        response = post_flows.patch_post(POST_GET_EXISTING_ID,POST_UPDATE_INVALID)
        APIVerify.status_code(response,STATUS_OK)
        APIVerify.json_keys_and_types(response.json(),EXPECTED_TYPES)



    @allure.title("Verify Post Update")
    @allure.description("Checks that the post was updated and all fields in the response match the request.")
    def test06_verify_update_post_put(self,post_flows:PlaceholderPostsApiFlows):
        response = post_flows.update_post_put(POST_ID,POST_UPDATE_FULL)
        APIVerify.status_code(response, STATUS_OK)
        APIVerify.json_contains(response.json(), POST_UPDATE_FULL)
             


    @allure.title("Delete Post")
    @allure.description("Verifies that a post can be deleted and the API returns the expected status code.")
    def test07_verify_delete_post(self,post_flows:PlaceholderPostsApiFlows):
        response = post_flows.delete_post(POST_ID)
        APIVerify.status_code(response, STATUS_OK)
      


    @allure.title("Negative Test - Get Non-Existing Post")
    @allure.description("Checks that a non-existing post returns 404 or empty response") 
    def test08_verfiy_get_invalid_post(self,post_flows:PlaceholderPostsApiFlows):
        response = post_flows.get_post_invalid(INVALID_POST_ID)
        print(response)
        APIVerify.status_code(response,NOT_FOUND)



    @allure.title("Invalid Endpoint Request")
    @allure.description("Requesting a non-existent endpoint returns 404.")   
    def test09_invalid_endpoint(self,post_flows:PlaceholderPostsApiFlows):
         response = post_flows.get_invalid_endpoint(INVALID_ENDPOINT)
         APIVerify.status_code(response, NOT_FOUND)
    
    

    @allure.title("Post with Empty payload")
    @allure.description("Verifies that creating a post with an empty payload returns an error.")
    def test10_post_with_empty_payload(self, post_flows: PlaceholderPostsApiFlows):
        response = post_flows.create_post(EMPTY_PAYLOAD)
        print(response.json())
        APIVerify.status_code(response,STATUS_POST_CREATED)
        APIVerify.json_key_exists(response.json(), keys=POST_KEYS)