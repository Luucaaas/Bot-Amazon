from google.cloud import bigquery
from datetime import datetime
from zoneinfo import ZoneInfo


def send_kpi_to_bigquery(event_type, account_id, product_url, message=None):
    client = bigquery.Client()
    
    table_id = "amazon-bot-kpi.bot_metrics.kpi_table"  
    
    rows_to_insert = [{
        "timestamp": datetime.now(ZoneInfo("Europe/Paris")).isoformat(),
        "event_type": event_type,
        "account_id": account_id,
        "product_url": product_url,
        "message": message
    }]
    
    errors = client.insert_rows_json(table_id, rows_to_insert)
    
    if errors:
        print("❌ Erreur lors de l'envoi du KPI à BigQuery :", errors)
    else:
        print("✅ KPI envoyé avec succès à BigQuery.")
