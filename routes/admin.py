import os
from fastapi import APIRouter, BackgroundTasks, Request
from service.email_service import EmailService

router = APIRouter()

@router.post("/github-webhook")
async def handle_webhook(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()

    user = data.get("user", "Unknown User")
    repo = data.get("repo", "Unknown Repo")
    event = data.get("event", "push")

    background_tasks.add_task(EmailService.send_email_task, user, repo, event)

    return {"status": "success", "message": "Webhook received, email is being sent."}
