from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck")
async def healthcheck():
    """Health check."""
    return {"success": True}
