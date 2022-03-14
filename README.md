# React-Django Meme Page

This is a social media app for browsing and commenting memes. It is intended to let you post new memes, comment and reply to comments, upvote/downvote, join groups and follow other users, posts comments, and groups, receive push notifications. It should also have a keyword moderation algorithm as well as trackers, to track user info regarding reach, net growth, sentiment, engagement and views, for the moment. Additionally, we should implement a sponsor component on the app and server, and track on the user interaction with it. 

# Version 0.9.1

## Main Features

- A feed to browse memes
- Django REST API implementation
- Frontent/Backend app split, with client side rendering
- Postgres Relational Database, At the moment the tables are: Post, Comment, SubComment, User, and Group
- A basic React implementation, working on improvements and refining
- Added testing implementation
- React components and fetch api calls
- User authentication is implemented, but at this moment it does not change anything

## Work in progress

- React routing implementation
- A better frontend layout
- Add more layouts for different media queries, at this moment only the mobile on the mobile first design is arranged
- Work on testing the frontend with different chrome extensions
- Add comment and subcomment components
- Refine the user authentication and comment permissions
- User landing page
- Web tracking info
- Filtering and ordering option
- Ordering by popular or trending requires viewer tracking
- I have no http error custom views, the user does not want to see that 90s style with Times New Roman font screen, neither know what a 400, 401, 402, or 404 error means.
- Needs preparation of some settings and api calls for future deployment
- Should have used docker to make things easier on deployment, still learning about the cloud and how it works
- Big content paragraphs need overflow cutting down on the frontend and a "see more" button but I have not started yet with that


## Known bugs

- It crashes or shows console errors with some chrome extensions
- Sometimes the frontend app does not shows posts, it barely happens but should never happen in first place.
- Anything other than mobile phone result on a bad user experience
- There should be others but are invisible at this moment

