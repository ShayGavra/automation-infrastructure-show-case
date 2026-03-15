import allure
from playwright.sync_api import APIRequestContext, APIResponse

from data.api.placeholder_posts_data import *
from extensions.api_actions import APIActions
from extensions.api_verifications import APIVerify


class PlaceholderPostsApiFlows:


    def __init__(self,request_context:APIRequestContext):
        self.api = APIActions(request_context)



    @allure.step("Create post")
    def create_post(self,data):
        return self.api.post(POSTS_ENDPOINT,data)
    


    @allure.step("Get Post by ID")
    def get_post_by_id(self,ID):
        return self.api.get(f"{POSTS_ENDPOINT}/{ID}")
    


    @allure.step("Get all posts")
    def get_all_posts(self):
        return self.api.get(POSTS_ENDPOINT)
    


    @allure.step("Patch a post by ID")
    def patch_post(self,post_id,data):
        return self.api.patch(f"{POSTS_ENDPOINT}/{post_id}",data)
    

    @allure.step("Update post")
    def update_post_put(self,post_id , data):
        return self.api.put(f"{POSTS_ENDPOINT}/{post_id}",data)
    

    @allure.step("Delete post")
    def delete_post(self,post_id: int):
        return self.api.delete(f"{POSTS_ENDPOINT}/{post_id}")
    

    @allure.step("Get post with invalid ID")
    def get_post_invalid(self,invalid_id):
        return self.api.get(f"{POSTS_ENDPOINT}/{invalid_id}")
    

    @allure.step("Get request to an invalid endpoint")
    def get_invalid_endpoint(self,invalid_endpoint):
        return self.api.get(f"{POSTS_ENDPOINT}/{invalid_endpoint}")
    

    @allure.step("Create/Update post with empty title")
    def Post_with_empty_title(self,data):
        return self.api.post(f"{POSTS_ENDPOINT}",data)