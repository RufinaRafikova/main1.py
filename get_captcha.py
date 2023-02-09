import requests


def get_captcha():
    # Your Captchas.net API Key
    api_key = "YOUR_API_KEY"

    # Endpoint to get a new CAPTCHA
    endpoint = "https://api.captchas.net/captcha"

    # Send the request to the endpoint and receive the response
    response = requests.get(endpoint, params={"key": api_key})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()

        # Check if the CAPTCHA was generated successfully
        if data["success"]:
            # Return the CAPTCHA image URL
            return data["captcha_url"]
        else:
            # Return None if there was an error generating the CAPTCHA
            return None
    else:
        # Return None if the request was not successful
        return None
