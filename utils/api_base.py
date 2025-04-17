from playwright.sync_api import Playwright

create_order_payload = {
    "orders": [
        {
            "country": "Chile",
            "productOrderedId": "6678cdf0ae2afd4c0b096956"
        }
    ]
}

login_payload = {
    "userEmail": "fenix@gmail.com",
    "userPassword": "Rise123!"
}


class ApiUtils:

    def get_token(self, playwright: Playwright, user_credentials):
        user_email = user_credentials["user_email"]
        user_password = user_credentials["user_password"]

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/auth/login",
                                            data={
                                                "userEmail": user_email,
                                                "userPassword": user_password
                                            })
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def create_order(self, playwright: Playwright, user_credentials):
        token = self.get_token(playwright, user_credentials)

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=create_order_payload,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"})
        response_json = response.json()
        print(response_json)
        response_body = response.json()
        return response_body["orders"][0]
