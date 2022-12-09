# Restaurant Booking System

## Introduction
Welcome to my fourth project. This project is a simple appointment booking system for a Marketing that allows clients to book appointment with the agency. This will use languages such as Django, Python, HTML, CSS and JavaScript.

This project will show the use of CRUD functionality (Create, Read, Update, Delete). The user will be able create, read, update and delete their appoinmenta.

A live website can be found [here](https://top-chef-kelvin.herokuapp.com/).

![website preview]()

# Table of Contents

-   [1. UX](#ux)
    -   [1.1. Strategy](#strategy)
        -   [Project Goals](#project-goals)
            -   [User Goals:](#user-goals)
            -   [User Expectations:](#user-expectations)
            -   [Trends of Modern Websites](#trends-of-modern-websites)
            -   [Strategy Table](#strategy-table)
    -   [1.2. Structure](#structure)
    -   [1.3. Skeleton](#skeleton)
    -   [1.4. Surface](#surface)
-   [2. Features](#features)
-   [3. Technologies Used](#technologies-used)
-   [4. Testing](#testing)
-   [5. Development Cycle](#development-cycle)
-   [6. Deployment](#deployment)
-   [7. End Product](#end-product)
-   [8. Known Bugs](#known-bugs)
-   [9. Credits](#credits)

<a name="ux"></a>

# 1. UX

[Go to the top](#table-of-contents)

The application was developed to cater new startup digital marketing agency in order to increase their online visibility and to cater their client. My objective was to create a website that can offer simplicity and a user frienly appointment booking system to the user.

This project will showcase simplicity and ease to create an appointment, update an appointment and cancel an appointment to the user.

<a name="strategy"></a>

## 1.1. Strategy

[Go to the top](#table-of-contents)

### Project Goals
The main goal of this project is to allow the user to sign up, sign in/out, create/update a user appoitnments in a simple and effective process.

### User Goals:
First Time Visitor Goals
-   As a first-time visitor, I want to an appointment at my chosen date and time.
-   As a first-time visitor, I want to be able to get the contact details of the restaurant with ease.

Returning Visitor Goals
-   As a Returning Visitor, I want to update my appointment details.
-   As a Returning Visitor, I want to cancel a booking I have already made.


### User Expectations:
The system should have a simple user interface, with the navigation to each section clear and concise.

-   The menu is clear to read.
-   The user interface is easy to navigate.
-   The website is responsive on all devices.
-   To have the ability to contact the agency for any enquiries.

### User Stories
Throughout the project I used the GitHub projects board to log all user stories as my project management tool. This helped me keep focus on the necesarry tasks as I would move them to the "in progress lane" as I'm working on the story. I would then move them to the "done" lane once the story has been completed.

![user_story_board](documentation_assets/images/project_board.png)

### Strategy Table
Opportunity/Problem/Feature| Importance| Viability/Feasibility
------------ | -------------------------|---------
Account registration | 5 | 5
User profile | 5 | 5
Responsive design | 5 | 5
Ability to create an appointment | 5 | 4
Ability to update a appointment | 5 | 4
Ability to cancel a appointment | 5 | 4
Total | 30 | 27

## Scope
As I am unable to include all of the features from the strategy table. I will phase this project in multiple phases. Phase 1 will be what I have identified as a minimum viable product. Please find below the plans I have for each phase.

### Phase 1
- Allow users to register for an account
- Responsive design
- Ability to create an appointment
- Ability to update a appointment
- Ability to cancel a appointment

### Phase 2
- Contact form model, so messages are saved to the database

<a name="structure"></a>

## 1.2. Structure

[Go to the top](#table-of-contents)

It is really important to include responsive design in this project as many users are using different devices (mobile, tablet, laptop/PC). This gives the user the best experience on their device.

- Responsive on all device sizes
- Easy navigation through labelled buttons
- Footer at the bottom of the index page that links to the social media website.
- All elements will be consistent including font size, font family, colour scheme.

### Database Model
Planned database structure:
![database_model](documentation_assets/images/database_model.png)

Final database structure:

```python
class BookAppointmentModel(models.Model):

    '''
    Model shows what fields are created to book an appointment
    for the user.
    '''
    user_title = [
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('miss', 'Miss')
    ]
    title = models.CharField(max_length=5, choices=user_title)
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_booking', null=True)
    name = models.CharField(max_length=40)
    company_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    appointment_date = models.DateField()
    appointment_time = models.TimeField(default=timezone.now)
    appointment_comments = models.TextField(max_length=200, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    admin_decision = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return str(self.name)
```

<a name="skeleton"></a>

## 1.3. Skeleton

[Go to the top](#table-of-contents)

### Wire-frames

Home/Landing Page Desktop:
![home_page_desktop](documentation_assets/wireframes/home_desktop.png)

Menu Page Desktop:
![menu_page_desktop](documentation_assets/wireframes/menu_desktop.png)

Register Page Desktop:
![register_page_desktop](documentation_assets/wireframes/register_desktop.png)

Login Page Desktop:
![login_page_desktop](documentation_assets/wireframes/login_desktop.png)

User Logged In Desktop:
![user_logged_in_desktop](documentation_assets/wireframes/user_logged_in_desktop.png)

Online Booking Page Desktop:
![online_booking_page_desktop](documentation_assets/wireframes/online_booking_desktop.png)

Contact Page Desktop:
![contact_page_desktop](documentation_assets/wireframes/contact_desktop.png)

Edit Profile Page Desktop:
![edit_profile_page_desktop](documentation_assets/wireframes/edit_profile_desktop.png)

Manage Booking Page Desktop:
![manage_booking_page_desktop](documentation_assets/wireframes/manage_booking_desktop.png)

From left to right home > navigation bar > menu mobile:
![home_navbar_menu_mobile](documentation_assets/wireframes/home_navbar_menu_mobile.png)

From left to right online bookings > contact form part 1 > contact form part 2 mobile:
![online-booking_contact-1_contact_2_mobile](documentation_assets/wireframes/online-booking_contact-1_contact-2.png)

From left to right edit profile > manage bookings mobile:
![edit-profile_manage-bookings_mobile](documentation_assets/wireframes/edit-profile_manage-bookings.png)

From left to right resgister > navigation bar when user is logged in mobile:
![register_login_logged-in-navbar_mobile](documentation_assets/wireframes/register_login_logged-in-navbar.png)

<a name="surface"></a>

## 1.4. Surface

[Go to the top](#table-of-contents)

### Colours

Please find the colours schemes that I used [here](https://coolors.co/bd3c31-000000-ffffff-212529).

# 2. Features

[Go to the top](#table-of-contents)

### All Pages
- The navigation bar is placed at the top of all pages. The navigation bar is dynamic in that meaning depending on if the user is logged in or not the options will change.
- If the user is not logged in the navigation bar will look like this:
![user_not_logged_in](documentation_assets/images/navbar_not_logged_in.png)
- If the user is logged in the navigation bar will look like this:
![user_logged_in](documentation_assets/images/navbar_logged_in.png)
- The footer is placed at the bottom of each page with social media icons.

- The agency logo is also placed at the top of all pages. Clicking on it will also direct the user to the home page.


