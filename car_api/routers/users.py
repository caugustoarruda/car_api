from fastapi import APIRouter, status


router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
async def list_users():
    return {
        'users': [
            {'id': 1, 'email': 'carlos@gmail.com'},
            {'id': 2, 'email': 'carlos1@gmail.com'},
            {'id': 3, 'email': 'carlos2@gmail.com'},
        ]
    }