from fastapi import APIRouter

from api.endpoints import location

router = APIRouter()
router.include_router(location.router, tags=["location"])
