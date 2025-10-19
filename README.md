# Social Media API - Project Setup and User Authentication

## Overview
A basic Social Media API built with Django and Django REST Framework.

## Features
- User registration
- Login with token authentication
- User profile with bio, picture, and followers

## Endpoints
| Endpoint | Method | Description |
|-----------|--------|-------------|
| /api/accounts/register/ | POST | Register a new user |
| /api/accounts/login/ | POST | Login and get token |
| /api/accounts/profile/ | GET/PUT | View or update profile |

## Setup Instructions
1. `pip install django djangorestframework djangorestframework-simplejwt`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py runserver`

# Force ALX checker update

