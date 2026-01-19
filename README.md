# FastAPI Student Message API with MongoDB & CI/CD

This project is a REST API built with FastAPI and MongoDB Atlas. It includes automated CI/CD testing via GitHub Actions and features basic sentiment analysis.

## Features
- **GET /**: Welcome message.
- **GET /add_message**: Adds a message to MongoDB and calculates sentiment (positive/negative).
- **GET /messages**: Retrieves all messages from the database.
- **GET /analyze**: Calculates the mode sentiment and allows grouping by class or subject.
- **CI/CD**: Automated deployment testing via GitHub Actions.

## Tech Stack
- **Framework**: FastAPI
- **Database**: MongoDB Atlas (Cloud)
- **Async Driver**: Motor
- **CI/CD**: GitHub Actions

## API Usage & Examples

### 1. Add a Message
`GET /add_message?message=The math exam was good&subject=Math&class_name=A`

### 2. Get All Messages
`GET /messages`

### 3. Analyze Sentiment (Overall)
`GET /analyze`

### 4. Analyze Sentiment (Grouped)
`GET /analyze?group_by=class_name`

## Setup & Deployment
1. Install dependencies: `pip install -r requirements.txt`
2. Set your `MONGO_URL` in `main.py`.
3. Run locally: `uvicorn main:app --reload`
4. GitHub Actions will automatically test the build on every push to the `main` branch.