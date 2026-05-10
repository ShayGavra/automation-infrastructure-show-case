import allure
import google.genai as genai
from playwright.sync_api import Page
from data.web.brains_data import *



class AiFlow:
    def __init__(self, page:Page):
        self.page = page



    @allure.step("Verify page title using AI")
    def verify_title(self, expected_title:str) -> bool:
        try:
            self.page.wait_for_selector(f"text={expected_title}", timeout=10000)
        except Exception:
            print(f"Warning: Title '{expected_title}' not found in DOM after 10s")

        # 2. צילום screenshot
        client = genai.Client(api_key=GEMINI_API_KEY)
        screenshot_bytes = self.page.screenshot(type="png")

        # בניית prompt ל-AI
        prompt = (
            f"Examine the screenshot. Does the main page title equal '{expected_title}'? "
            "Respond with 'Yes' or 'No', and include only the title you detected."
        )

        # שליחה ל-Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                prompt,
                genai.types.Part.from_bytes(
                    data=screenshot_bytes,
                    mime_type="image/png"
                )
            ]
        )

        result = response.text.strip().lower()
        print("\nThe result from AI:", result)

        return "yes" in result