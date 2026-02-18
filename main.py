from fastapi import FastAPI, Request
from fastapi.responses import Response
from datetime import datetime
import base64

app = FastAPI()

@app.get("/track")
async def track_email(request: Request, u: str, c: str, l: str):

    print("Email Opened!")
    print("User ID:", u)
    print("Campaign ID:", c)
    print("Lead ID:", l)
    print("Time:", datetime.utcnow())
    print("IP:", request.client.host)
    print("User-Agent:", request.headers.get("user-agent"))

    # Return 1x1 transparent pixel
    pixel = base64.b64decode(
        "R0lGODlhAQABAIAAAAAAAP///ywAAAAAAQABAAACAUwAOw=="
    )

    return Response(content=pixel, media_type="image/gif")
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)