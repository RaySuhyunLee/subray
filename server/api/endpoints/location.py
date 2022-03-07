from fastapi import APIRouter

router = APIRouter()


@router.get('/subway/locations')
def get_subway_locations():
    return ""
