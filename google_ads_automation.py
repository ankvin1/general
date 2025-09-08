"""Simple Google Ads automation script to list campaigns."""

import argparse
from google.ads.googleads.client import GoogleAdsClient

def list_campaigns(client: GoogleAdsClient, customer_id: str) -> None:
    """Lists campaigns for the specified customer ID."""
    ga_service = client.get_service("GoogleAdsService")
    query = "SELECT campaign.id, campaign.name FROM campaign ORDER BY campaign.id"

    stream = ga_service.search_stream(customer_id=customer_id, query=query)
    for batch in stream:
        for row in batch.results:
            print(f"Campaign ID {row.campaign.id} name {row.campaign.name}")

def main() -> None:
    parser = argparse.ArgumentParser(description="List Google Ads campaigns")
    parser.add_argument("customer_id", help="Google Ads customer ID")
    parser.add_argument(
        "--config",
        default="google-ads.yaml",
        help="Path to google-ads.yaml configuration file",
    )
    args = parser.parse_args()

    client = GoogleAdsClient.load_from_storage(path=args.config)
    list_campaigns(client, args.customer_id)

if __name__ == "__main__":
    main()
