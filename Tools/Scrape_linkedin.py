import os
import requests


def scrape_linkedin_profile():
    """
    Scrape information from the linkedin prfile
    Manually scrape the information from linkedin profile
    """

    # Let's extract the data from the provided URL
    response = requests.get(
        "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    )

    raw_data = response.json()
    raw_data = {
        key: value
        for key, value in raw_data.items()
        if value not in ([], "", "", None)
        and key not in ["people_also_viewed", "certifications"]
    }
    if raw_data.get("groups"):
        for group_dict in raw_data.get("groups"):
            group_dict.pop("profile_pic_url")

    return raw_data


if __name__ == "__main__":
    print(scrape_linkedin_profile())
