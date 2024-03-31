from app.utils import generate_test_email, send_email
from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

router = APIRouter()
