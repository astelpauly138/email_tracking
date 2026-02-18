from fastapi import FastAPI
from fastapi.responses import Response
import base64
import json
from supabase_client import supabase

app = FastAPI()

@app.get("/track")
async def track_email(data: str):

    # Decode hidden UUIDs
    decoded = json.loads(
        base64.urlsafe_b64decode(data.encode()).decode()
    )

    user_id = decoded["u"]
    campaign_id = decoded["c"]
    lead_id = decoded["l"]

    # ✅ Update only status
    response = supabase.table("email_events") \
        .update({"status": "opened"}) \
        .eq("lead_id", lead_id) \
        .eq("user_id", user_id) \
        .eq("campaign_id", campaign_id) \
        .execute()

    print("Updated:", response.data)

    # Return 1x1 transparent pixel
    pixel = base64.b64decode(
        "R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw=="
    )

    return Response(content=pixel, media_type="image/gif")
