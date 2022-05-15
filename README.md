#### Pitch-Me
The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

## Technology used
1. Python
2. Flask
3. HTML
4. CSS3
5. PostgresSQL

## Requirements
An IDE such as VS code with Python version 3 installed,a terminal and a browser. 

## Setup and Instruction
1. Clone the repository at [here](https://github.com/emmakamau/Pitch-Me.git).
2. Extract and open the folder on VS code or navigate to the folder on your terminal.
3. On the terminal, create a virtual environment `python3 -m venv virtual` and activate it `source virtual/bin/activate`. NB **virtual** is the name of the environment.
4. Pip install dependancies highlighted on the **requirements.txt** by running `pip install -r requirements.txt`
5. Create a **start.sh** file in the root directory of the folder and define the **secret key,email address and email password**.
6. Run `chmod +x start.sh` and `./start.sh` respectively on the terminal.
7. View the application on your browser through `http://127.0.0.1:5000`.

## Behaviour Driven Development

BDD focuses on how the user will interact with the application.
What you will see and experience:
1. A landing page with a quote, navigation bar and an option to create a pitch.
2. The Navbar has three routes to view pitches based on category. Also includes a route to sign in to the application.
3. Click on the sign in, if user does not have an account, they can click on sign up.
4. On the sign up form, the user is required to enter an email,unique username and a password. Upon registration the user receives a welcome email and is redirected to the sign in page.
5. After the user sign in, they can navigate to their profile through teh navbar and update their profile pic and bio. They can add a new pitch as well.
6. On the category pages, a user can view other pitches, upvote or downvote a pitch. Click on the view comments to get redirected to a particular pitch with comments from other users displayed.
7. Click on the new comment and add a comment as well.
8. Click on signout to logout of the application.

## Development
To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request

## Known Bugs
- A user can vote more than once.

If you find a bug or would like to request a new function, reach out to me via Email: emmaculatewkamau@gmail.com or on [LinkedIn](https://www.linkedin.com/in/emmaculate-k-987353104/)

## Future Plans
- Ensure a user can only vote once for a particular pitch.
- Display the owner of the pitch.
- Ability to navigate to other users profiles.

## License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2022 **Emmaculate Kamau**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.