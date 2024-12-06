# Student Synergy - Affordable Housing Locator for Students

**Lead Developer**: Eric Paiz (Lead Developer, Database Architect, Documentation)
**Lead Designer & Developer**: Ligia Cerna (Lead Designer, Developer, Testing, Integration Needed)
**Database Developer & System Design**: Karla Cardenas (Database Developer, SQL Code)
**Communications Expert & Systems Design, Documentation**: Scott Balzer

## Overview
This project, **Student Synergy - Affordable Housing Locator for Students**, was originally developed as part of a class assignment to help students locate affordable housing near their campuses. It addresses the challenges faced by students in urban or high-demand areas by offering a platform that helps them find housing options within their budget, connect with potential roommates, and understand tenant rights and responsibilities. The current iteration of the project includes functional user registration, login, and search features, while several features still need to be built out to make the project fully functional. Our GitHub repository can be found here: [Student Synergy on GitHub](https://github.com/erpzz/Student-Synergy).

## Problem Statement
Many students struggle to find affordable housing, especially in urban or high-cost areas. The goal of this project is to develop a web-based or mobile application that helps students find affordable housing options, connect with potential roommates, and provide educational resources about tenant rights and responsibilities.

## Project Objective
Develop a user-friendly platform to:
- **Search for Housing**: Students can search for housing by rent, location, housing type, etc.
- **Find Roommates**: Connect with potential roommates based on compatibility.
- **Learn Tenant Rights**: Provide access to educational resources about tenant rights and lease agreements.

## Key Features
1. **Housing Search Functionality**: Students can filter housing listings by rent, location, and other criteria (e.g., proximity to campus).
2. **Roommate Finder**: Connect students with potential roommates based on budget, interests, and lifestyle compatibility.
3. **Educational Resources**: Provide students with information about tenant rights, lease agreements, and general renting tips.
4. **User Profiles**: Allow students to create personalized profiles to improve the roommate matching process.

## Team Contributions
- **Eric Paiz**: Responsible for the overall development, including database architecture and writing documentation. Created registration, login, and preference matcher mockups, as well as registration form code. Designed the database and coordinated integration between different modules.
- **Ligia Cerna**: Contributed to design, testing, and development. Developed user cases, created test plans, ensured the quality and usability of the system, and contributed code that still needs integration into the main repository. Ligia was also one of the primary developers, focusing on creating cohesive user experiences.
- **Karla Cardenas**: Worked on database development and system design, focusing particularly on the SQL code for database tables and activity diagrams. Although her SQL code is not currently included in this repository, it was submitted separately to our professor and may be integrated in the near future.
- **Scott Balzer**: Focused on communications, system design, and documentation. He also handled the logical system structure.

## Presentation Responsibilities
Each team member was responsible for presenting part of the project:
- **Eric**: Presented the code, features, and major milestones.
- **Karla**: Presented the database, including activity diagrams and SQL code.
- **Scott**: Presented the system's logical architecture and structure.
- **Ligia**: Presented user cases and testing plans.

## Project Plan
### Phases:
1. **Requirements Gathering & Design Mockups**: Initial planning and creation of user interface mockups.
2. **Database Design**: Developing tables for users, housing listings, roommate matches, reviews, and messaging.
3. **Feature Implementation**: Developing user registration, profile management, search functionality, roommate finder, and educational resources.
4. **Testing & Bug Fixing**: Conducting functional, UI/UX, and performance testing. Fixing bugs to ensure a stable product.
5. **Final Documentation & Submission**: Finalizing the project and submitting it for review.

## Modules Overview
1. **User Management**: Registration, login, password recovery, and profile setup.
2. **Housing Search**: Filter and search available housing options with location integration.
3. **Messaging System**: Communication between students and landlords.
4. **Favorites & Recommendations**: Save favorite listings and receive recommendations.
5. **Educational Resources**: Information about tenant rights.
6. **Security**: Password hashing and data encryption for secure user experience.

## User Stories
1. As a student, I want to view detailed housing listings, including images and descriptions, so that I can get an overview of my options before contacting the landlord.
2. As a student, I want to be able to filter listings by price, amenities, distance from campus, and more to easily find what I need.
3. As a student, I want to connect with compatible roommates to share rent and expenses.
4. As a student, I want to receive notifications when listings that match my preferences become available.
5. As a student, I want to communicate directly with landlords through the platform.

## System Design
- **Activity Diagrams**: Outline the flow of actions such as user registration, housing search, and profile creation.
- **Entity-Relationship Diagrams (ERD)**: Shows the relationships between key components such as users, housing listings, roommates, and messaging.
- **Sequence Diagrams**: Describes user interactions like adding a listing to favorites or sending a message to a landlord.

## Wireframes
The wireframes provide a visual guide for the main screens, including:
- **Housing Listings**
- **Roommate Search**
- **User Registration/Login**

## Installation and Setup
### Requirements
- Python 3.x
- Flask
- JSON library
### How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/erpzz/Student-Synergy.git
   ```
2. Navigate to the project folder and install dependencies.
   ```sh
   cd Student-Synergy
   pip install -r requirements.txt
   ```
3. Run the Flask server:
   ```sh
   python app.py
   ```
4. Visit `http://127.0.0.1:5000/` in your browser.

## Features Yet to Be Built
- **Roommate Matching Algorithm**: An algorithm that calculates compatibility scores for potential roommates based on their profiles.
- **Interactive Map Integration**: Integrate a map to visualize property locations and their proximity to campuses.
- **Notifications**: Implement notifications to alert students of new listings or roommate requests.
- **Secure Payment Integration**: Allow for secure online payments for deposits.
- **Ratings & Reviews**: Enable users to rate properties and provide reviews to help other students.
- **Integrating Full Code-Base**: Currently we only have portions of the codebase on this repo, but plan to integrate Ligia's code as well.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


## Contact
For questions, suggestions, or collaborations, please reach out via GitHub at [@erpzz](https://github.com/erpzz).

We hope this project helps students find housing more easily and contributes to a more comfortable college experience.

