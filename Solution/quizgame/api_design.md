API Design for Kahoot App with Media Support
# Overview

This API design outlines the endpoints and data structures required for a Kahoot-like application. The API will support user management, quiz creation, participation, real-time interactions, and media (image and video) support.

**Base URL:** `https://api.kahoot-clone.com/v1`

## Endpoints

### User Management

#### 1.1 Register User
- **Endpoint:** `/users/register`
- **Method:** `POST`
- **Description:** Registers a new user.
- **Request Body:**
    ```json
    {
        "username": "string",
        "email": "string",
        "password": "string"
    }
    ```
- **Response:**
    ```json
    {
        "userId": "string",
        "username": "string",
        "email": "string",
        "profilePicture": "string",
        "createdAt": "ISODate"
    }
    ```

```yaml
  /users/register:
    post:
      summary: Registers a new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                email:
                  type: string
                password:
                  type: string
      responses:
        '200':
          description: User registered successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  userId:
                    type: string
                  username:
                    type: string
                  email:
                    type: string
                  profilePicture:
                    type: string
                  createdAt:
                    type: string
                    format: date-time
```

#### 1.2 Login User
- **Endpoint:** `/users/login`
- **Method:** `POST`
- **Description:** Logs in a user.
- **Request Body:**
    ```json
    {
        "email": "string",
        "password": "string"
    }
    ```
- **Response:**
    ```json
    {
        "token": "string",
        "userId": "string",
        "username": "string",
        "email": "string",
        "profilePicture": "string"
    }
    ```

```yaml
  /users/login:
    post:
      summary: Logs in a user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                email:
                  type: string
                password:
                  type: string
      responses:
        '200':
          description: User logged in successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  token:
                    type: string
                  userId:
                    type: string
                  username:
                    type: string
                  email:
                    type: string
                  profilePicture:
                    type: string
```

#### 1.3 Social Media Login
- **Endpoint:** `/users/oauth/login`
- **Method:** `POST`
- **Description:** Logs in a user using OAuth2.
- **Request Body:**
    ```json
    {
        "provider": "string", // e.g., "google", "facebook"
        "accessToken": "string"
    }
    ```
- **Response:**
    ```json
    {
        "token": "string",
        "userId": "string",
        "username": "string",
        "email": "string",
        "profilePicture": "string"
    }
    ```

```yaml
  /users/oauth/login:
    post:
      summary: Logs in a user using OAuth2
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                provider:
                  type: string
                accessToken:
                  type: string
      responses:
        '200':
          description: User logged in successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  token:
                    type: string
                  userId:
                    type: string
                  username:
                    type: string
                  email:
                    type: string
                  profilePicture:
                    type: string
```

### Quiz Management

#### 2.1 Create Quiz
- **Endpoint:** `/quizzes`
- **Method:** `POST`
- **Description:** Creates a new quiz.
- **Request Body:**
    ```json
    {
        "title": "string",
        "description": "string",
        "questions": [
            {
                "questionText": "string",
                "questionType": "string", // e.g., "multiple-choice", "true-false", "short-answer", "multiple-answer"
                "media": {
                    "imageUrl": "string",
                    "videoUrl": "string"
                },
                "options": [
                    {
                        "optionText": "string",
                        "isCorrect": "boolean"
                    }
                ],
                "timeLimit": "number" // Time limit in seconds for the question
            }
        ]
    }
    ```
- **Response:**
    ```json
    {
        "quizId": "string",
        "title": "string",
        "description": "string",
        "creatorId": "string",
        "questions": [
            {
                "questionId": "string",
                "questionText": "string",
                "questionType": "string",
                "media": {
                    "imageUrl": "string",
                    "videoUrl": "string"
                },
                "options": [
                    {
                        "optionId": "string",
                        "optionText": "string",
                        "isCorrect": "boolean"
                    }
                ],
                "timeLimit": "number"
            }
        ],
        "createdAt": "ISODate"
    }
    ```

#### 2.2 Get Quiz
- **Endpoint:** `/quizzes/{quizId}`
- **Method:** `GET`
- **Description:** Retrieves a quiz by its ID.
- **Response:**
    ```json
    {
        "quizId": "string",
        "title": "string",
        "description": "string",
        "creatorId": "string",
        "questions": [
            {
                "questionId": "string",
                "questionText": "string",
                "questionType": "string",
                "media": {
                    "imageUrl": "string",
                    "videoUrl": "string"
                },
                "options": [
                    {
                        "optionId": "string",
                        "optionText": "string",
                        "isCorrect": "boolean"
                    }
                ],
                "timeLimit": "number"
            }
        ],
        "createdAt": "ISODate"
    }
    ```

#### 2.3 Update Quiz
- **Endpoint:** `/quizzes/{quizId}`
- **Method:** `PUT`
- **Description:** Updates an existing quiz.
- **Request Body:**
    ```json
    {
        "title": "string",
        "description": "string",
        "questions": [
            {
                "questionId": "string",
                "questionText": "string",
                "questionType": "string",
                "media": {
                    "imageUrl": "string",
                    "videoUrl": "string"
                },
                "options": [
                    {
                        "optionId": "string",
                        "optionText": "string",
                        "isCorrect": "boolean"
                    }
                ],
                "timeLimit": "number"
            }
        ]
    }
    ```
- **Response:**
    ```json
    {
        "quizId": "string",
        "title": "string",
        "description": "string",
        "creatorId": "string",
        "questions": [
            {
                "questionId": "string",
                "questionText": "string",
                "questionType": "string",
                "media": {
                    "imageUrl": "string",
                    "videoUrl": "string"
                },
                "options": [
                    {
                        "optionId": "string",
                        "optionText": "string",
                        "isCorrect": "boolean"
                    }
                ],
                "timeLimit": "number"
            }
        ],
        "updatedAt": "ISODate"
    }
    ```

#### 2.4 Delete Quiz
- **Endpoint:** `/quizzes/{quizId}`
- **Method:** `DELETE`
- **Description:** Deletes a quiz by its ID.
- **Response:**
    ```json
    {
        "message": "Quiz deleted successfully"
    }
    ```

### Participation

#### 3.1 Join Quiz
- **Endpoint:** `/quizzes/{quizId}/join`
- **Method:** `POST`
- **Description:** Joins a quiz.
- **Request Body:**
    ```json
    {
        "userId": "string"
    }
    ```
- **Response:**
    ```json
    {
        "message": "User joined the quiz successfully"
    }
    ```

#### 3.2 Submit Answer
- **Endpoint:** `/quizzes/{quizId}/questions/{questionId}/answers`
- **Method:** `POST`
- **Description:** Submits an answer for a question.
- **Request Body:**
    ```json
    {
        "userId": "string",
        "selectedOptions": ["string"] // Array of selected options for multiple-answer questions
    }
    ```
- **Response:**
    ```json
    {
        "answerId": "string",
        "isCorrect": "boolean",
        "submittedAt": "ISODate"
    }
    ```

### Results and Scoreboard

#### 4.1 Get Results
- **Endpoint:** `/quizzes/{quizId}/results`
- **Method:** `GET`
- **Description:** Retrieves the results of a quiz.
- **Response:**
    ```json
    {
        "quizId": "string",
        "results": [
            {
                "userId": "string",
                "score": "number",
                "totalQuestions": "number",
                "correctAnswers": "number",
                "createdAt": "ISODate"
            }
        ]
    }
    ```

#### 4.2 Get Scoreboard
- **Endpoint:** `/quizzes/{quizId}/scoreboard`
- **Method:** `GET`
- **Description:** Retrieves the real-time scoreboard for a quiz.
- **Response:**
    ```json
    {
        "quizId": "string",
        "scoreboard": [
            {
                "userId": "string",
                "username": "string",
                "score": "number",
                "rank": "number",
                "updatedAt": "ISODate"
            }
        ]
    }
    ```

### Media Management

#### 5.1 Upload Image
- **Endpoint:** `/media/upload/image`
- **Method:** `POST`
- **Description:** Uploads an image for a quiz or question.
- **Request Body:**
    ```json
    {
        "file": "binary"
    }
    ```
- **Response:**
    ```json
    {
        "imageUrl": "string"
    }
    ```

#### 5.2 Upload Video
- **Endpoint:** `/media/upload/video`
- **Method:** `POST`
- **Description:** Uploads a video for a quiz or question.
- **Request Body:**
    ```json
    {
        "file": "binary"
    }
    ```
- **Response:**
    ```json
    {
        "videoUrl": "string"
    }
    ```

## Conclusion

This API design provides a comprehensive set of endpoints for managing users, quizzes, participation, real-time interactions, and media (image and video) support in a Kahoot-like application. The design ensures scalability, performance, and data integrity, making it suitable for a high-traffic application.