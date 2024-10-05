# Database Design for Kahoot Clone with Social Media Login, Multiple Answer Questions, and Scoreboard

## Overview
The database design for the Kahoot clone will use MongoDB Atlas, a managed NoSQL database service. The design will focus on scalability, performance, and data integrity. The primary collections will include users, quizzes, questions, options, answers, and results. Additionally, the users collection will be extended to support OAuth2 tokens and social media profiles. The design will also support multiple answer questions and a scoreboard.

## Collections and Schema

### 1. Users Collection
Stores information about the users of the application, including OAuth2 tokens and social media profiles.

#### Schema
```json
{
  "_id": "ObjectId",
  "username": "string",
  "email": "string",
  "passwordHash": "string",
  "profilePicture": "string",
  "oauthProviders": [
    {
      "providerName": "string", // e.g., "google", "facebook"
      "providerId": "string", // Unique ID from the OAuth provider
      "accessToken": "string",
      "refreshToken": "string",
      "tokenExpiry": "ISODate"
    }
  ],
  "createdAt": "ISODate",
  "updatedAt": "ISODate"
}```

### 2. Quizzes Collection
Stores information about the quizzes created by users.

#### Schema
```json
{
  "_id": "ObjectId",
  "title": "string",
  "description": "string",
  "creatorId": "ObjectId",
  "questions": ["ObjectId"],
  "createdAt": "ISODate",
  "updatedAt": "ISODate"
}
```

### 3. Questions Collection
Stores information about the questions in each quiz.

#### Schema
```json
{
  "_id": "ObjectId",
  "quizId": "ObjectId",
  "questionText": "string",
  "questionType": "string", // e.g., "multiple-choice", "true-false", "short-answer", "multiple-answer"
  "media": {
    "imageUrl": "string",
    "videoUrl": "string"
  },
  "options": ["ObjectId"],
  "timeLimit": "number", // Time limit in seconds for the question
  "createdAt": "ISODate",
  "updatedAt": "ISODate"
}
```

### 4. Options Collection
Stores information about the options for each question.

#### Schema
``` json
{
  "_id": "ObjectId",
  "questionId": "ObjectId",
  "optionText": "string",
  "isCorrect": "boolean",
  "createdAt": "ISODate",
  "updatedAt": "ISODate"
}
```

### 5. Answers Collection
Stores the answers submitted by users during quizzes.

#### Schema
```json
{
  "_id": "ObjectId",
  "quizId": "ObjectId",
  "questionId": "ObjectId",
  "userId": "ObjectId",
  "selectedOptions": ["string"], // Array of selected options for multiple-answer questions
  "isCorrect": "boolean",
  "submittedAt": "ISODate"
}
```
### 6. Results Collection
Stores the results of quizzes taken by users.

#### Schema
```json
{
  "_id": "ObjectId",
  "quizId": "ObjectId",
  "userId": "ObjectId",
  "score": "number",
  "totalQuestions": "number",
  "correctAnswers": "number",
  "createdAt": "ISODate"
}
```

### 7. Scoreboard Collection
Stores the real-time scoreboard data for quizzes.

#### Schema
```json
{
  "_id": "ObjectId",
  "quizId": "ObjectId",
  "userId": "ObjectId",
  "username": "string",
  "score": "number",
  "rank": "number",
  "updatedAt": "ISODate"
}
```

### 8. Media Collection
Stores information about the media (images and videos) used in quizzes and questions.

#### Schema
```json
{
  "_id": "ObjectId",
  "mediaType": "string", // e.g., "image", "video"
  "url": "string",
  "createdAt": "ISODate",
  "updatedAt": "ISODate"
}
```
