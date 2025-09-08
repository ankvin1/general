# Google Ads Automation

This project provides a simple Python script to automate basic tasks in the Google Ads API. The `google_ads_automation.py` script lists campaigns for a given customer ID.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your Google Ads credentials by creating a `google-ads.yaml` file as described in the [Google Ads API documentation](https://developers.google.com/google-ads/api/docs/client-libs/python/configuration).

## Usage

List campaigns for a customer:

```bash
python google_ads_automation.py --config path/to/google-ads.yaml <CUSTOMER_ID>
```

Replace `<CUSTOMER_ID>` with your Google Ads customer ID.

