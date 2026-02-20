from fastapi import FastAPI
from fastapi.responses import Response, RedirectResponse
from supabase_client import supabase
import base64

app = FastAPI()


# -----------------------
# OPEN TRACKING
# -----------------------
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
        .eq("event_type", "sent") \
        .execute()

    print("Supabase response:", response.data)

    # 1x1 pixel
    pixel = base64.b64decode(
        "R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw=="
    )

    return Response(content=pixel, media_type="image/gif")


# -----------------------
# CLICK TRACKING
# -----------------------
@app.get("/click")
async def track_click(
    u: str,
    c: str,
    l: str,
    redirect: str
):

    print("CLICKED:")
    print("User:", u)
    print("Campaign:", c)
    print("Lead:", l)

    response = supabase.table("email_events") \
        .update({"event_type": "clicked"}) \
        .eq("lead_id", l) \
        .eq("user_id", u) \
        .eq("campaign_id", c) \
        .eq("event_type", "opened") \
        .execute()

    print("Supabase click response:", response.data)

    # Redirect to actual website
    return RedirectResponse(url=redirect)