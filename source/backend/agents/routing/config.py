INTENTS = {
    "troubleshoot": {
        "description": "Help the user troubleshoot entities (client, device, etc.) in their network.",
        "examples": [
            "troubleshoot client connectivity issues", 
            "client unable to connect"]
    }, 
    "query_database": {
        "description": "Help retrieve data from the database based on user queries.",
        "examples": [
            "Show hourly client disconnect events in the last 3 days for site = 'SFO'",
            "Trend of average AP CPU usage by day last week across all Nile Secure sites",
            "Top 5 event types by count yesterday"
            "list <something>"
            "trend <something>"
        ]
    }
}