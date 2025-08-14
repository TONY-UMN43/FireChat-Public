# FireChat-Public
A Full-Stack Project that has core Messaging app features such as user authentication, one-to-one conversations, and group chats.
## License
This project is for **viewing purposes only**.  
Do not copy, modify, or redistribute any part of this code without explicit permission.  
© 2025 Tony Akinyemi. All rights reserved.



## Description
FireChat is a messaging project that was inspired by Instagram.

1. Create an account or log in with an existing one.

2. See all conversations.

3. View Friends and joined Communities 

4. Connect with other users by using the friend request system.

The responsive CSS design was assisted by Google Gemini, which provided layout suggestions and styling guidance. The CSS was then optimized for the final design to ensure that it worked seamlessly across mobile, tablet, laptop, and desktop devices.

## Live Demo
- [Live Site](https://messaging-demo-umber.vercel.app/)

## Features
- User Authentication using OAuth2 & JWT
- Real-Time Messaging
- User Hobbies
- User-created communities
  - Each community has a central hobby
  - Allow users to meet new people with common hobbies
- Friend Request system between users
- Ability for users to search up other users
- Ability for users to edit their profiles and hobbies
  
## Tech-stack
- Frontend: React
- Backend: FastAPI
- Database: PostgreSQL
- Messaging: Firebase RealTime Database


## How to Run (Only for Recruiters)

Because the backend contains sensitive business logic, the full repository is private. Recruiters can request access by emailing me (contact info below)

Get Files
```Terminal
git clone git@github.com:NAME/FireBase.git
```
Install FastAPI Dependencies
```Terminal
cd FireBase
cd Backend
pip install -r requirements.txt
```
Install React Dependencies
```Terminal
cd ../frontend
npm install
```
Set Environment Variable
- Create .env file and create these variables
  
  - `DATABASE = "my_database_connection"`
  - `REACT_APP_API_BASE = http://localhost:8000`
Start the Frontend Client
```Terminal
npm start
```
Start the Backend Server
```Terminal
cd Backend
python3 -m venv venv
source ./venv/bin/activate"
uvicorn main:app --reload
```
Run the application from there

## Project Impact
FireChat showcases my ability to design, develop, and deploy a full-stack production-ready product for users.

It shows skills in every area of full-stack - building a secure backend with FastAPI, creating a PostgreSQL database to store persistent data, and developing an optimized React frontend with the help of Google Gemini.

Used real-life features such as JWT authentication, Firebase RealTime Database, and profile editing, which updates the database.

This project reflects the process of turning high-level System Design ideas into a polished program. It also reflects being able to use Google Gemini when there are technical constraints.

# Screenshots
| User Profile | User Feed |
|--------------|-----------|
| ![User-Profile Page](assets/Screen-shot-user-profile.png) | ![User-Feed Page](assets/Screen-shot-user-feed.png) |

| Home Page |
|-----------|
| ![Home Page](assets/Screen-shot-home.png) | ![Mobile View](assets/mobile.png) |


## Future Improvements
- **Performance**: Implement a Redis cache system to decrease latency and load times
- **Roles**: Add role-specific privileges for members of a group chat 
  - Creators of a group chat are assigned the admin of the group chat
  - Admins are the only ones who can add and remove members
  - Handle the edge case of the admin leaving the group chat
- **User Experience**
  - Add Typing Indicators
  - Add Last Read Indicators
- **Images**: Use AWS to allow users to upload profile pictures


## Contact Me
- Email: tony.akinyemi5@gmail.com
- LinkedIn: [Tony Akinyemi](https://www.linkedin.com/in/tony-akinyemi/)
