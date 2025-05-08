from repositories import userRepository
from models.userModel import User
from fastapi import HTTPException
async def create_user(user: User):
    if await get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="User already exists")
    return await userRepository.create_user(user)

async def get_user_by_email(email: str):
    return await userRepository.get_user_by_email(email)

async def delete_user_by_email(email: str):
    return await userRepository.delete_user_by_email(email)

async def get_all_users():
    return await userRepository.get_all_users()
