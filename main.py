from fastapi import FastAPI, Request
from fastapi.responses import Response
from supabase_client import supabase
import base64

app = FastAPI()

@app.get("/track")
async def track_email(
    u: str,
    c: str,
    l: str
):

    print("User:", u)
    print("Campaign:", c)
    print("Lead:", l)

    response = supabase.table("email_events") \
        .update({"event_type": "opened"}) \
        .eq("lead_id", l) \
        .eq("user_id", u) \
        .eq("campaign_id", c) \
        .execute()

    print("Supabase response:", response.data)

    # 1x1 pixel
    pixel = base64.b64decode(
        "R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw=="
    )

    return Response(content=pixel, media_type="image/gif")
