# [Nomad-Nation](https://nomad-nation-23b17dd0a6b5.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/AshLaw96/Nomad-Nation)](https://www.github.com/AshLaw96/Nomad-Nation/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/AshLaw96/Nomad-Nation)](https://www.github.com/AshLaw96/Nomad-Nation/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/AshLaw96/Nomad-Nation)](https://www.github.com/AshLaw96/Nomad-Nation)

The Caravan-themed website/app will allow users to explore, book, and manage caravan trips. It will feature a user-friendly interface for browsing caravan options, booking itineraries, and managing accounts, along with admin capabilities to manage caravans and bookings.

When a user first opens the app, they will land on the home page, where they will see a brief overview of the app's purpose and features. This introduction will include links to direct new users to the registration page and existing users to the login page. At the top of the home page, there will be a navigation icon that users can click to open a navigation bar with links to other sections of the app.

Once a user has either created a new account or logged into an existing one, they will be redirected to the dashboard. The dashboard layout will vary depending on whether the user is a customer or an owner but will follow the same overall structure, with tailored content for each role. After logging in, a secondary navigation bar will appear, providing quick access to tabs such as Account, Bookings, Listings, and Notifications. The dashboard's main section will feature various content areas, each accompanied by a slideshow of images and links to corresponding pages. A search bar will also be available, allowing users to quickly find specific actions, such as editing their personal details, contacting another user, or booking a caravan stay.

On the Account page, users will be able to update their personal information, modify payment details, change preferences, or review the app’s privacy and data management policies alongside other information. Customers can then proceed to the Caravan Listings page, where they will be able to browse all available caravans. Each listing will include a detailed description and a gallery of images that users can scroll through. To help customers narrow their search, filters will be available, allowing them to focus on specific criteria, such as the caravan’s size, location, or available amenities. Additionally, a search bar will enable customers to input a specific caravan ID to be taken directly to that caravan’s details.

For owners, the Listings page will also include a section showcasing all of their currently listed caravans, with options to edit or delete them. Owners will also have access to a feature for adding new caravan listings, including details and images.

When a customer decides to book a caravan, they can click the "Book Now" button to be redirected to the booking page. This page will feature a booking form where customers can provide their personal details, select dates for their stay, and include any additional information or questions for the owner. An aside section will display the customer’s current and previous bookings for easy reference. Once the booking request is submitted, the customer will receive a confirmation message informing them that the owner will review their request and respond within a specified time-frame.

On the owner’s side, the Bookings page will display all pending booking requests, along with the details submitted by customers. Owners will be able to review these details, add any further information or questions, and choose to either accept or decline the booking request. Once a decision has been made, a message will be sent to the customer notifying them of the outcome.

All notifications and messages, such as booking updates or admin communications, will be sent to the Notifications page. Users can also choose to enable email notifications in their account preferences, in which case they will receive email updates for important events alongside in-app notifications.

The main navigation bar will include a Contact tab accessible to all users. This page will feature a contact form where users can input their personal details and submit any questions or inquiries. The contact form will serve multiple purposes, such as owners reaching out to the admin, customers contacting owners, or even guest users requesting additional information about the application. This ensures streamlined communication for all users of the app.

Additionally, the application will include a 404 error page to handle instances where users attempt to access a non-existent or broken link. The error page will display a clear message explaining that an error has occurred and provide options to either navigate back to a specific page or wait to be automatically redirected to the homepage or dashboard. Consistency will be maintained across all pages in terms of structure and design, ensuring users can easily navigate the app without confusion.

![screenshot](documentation/mockup.png)

source: [Nomad-Nation amiresponsive](https://ui.dev/amiresponsive?url=https://nomad-nation-23b17dd0a6b5.herokuapp.com)

## UX

### The 5 Planes of UX

#### 1. Strategy Plane
##### Purpose
- Facilitate Escapes: Offer individuals and families a seamless way to disconnect from their daily routines and immerse themselves in peaceful, scenic environments.
- Curated Experiences: Provide access to a diverse range of caravan rentals in picturesque locations, ensuring users can find the perfect getaway that suits their preferences and needs.
- Easy Planning: Simplify the process of finding, booking, and managing caravan rentals, making it effortless for users to plan their perfect escape.
- Effortless Management: Provide caravan owners with a user-friendly platform to list and manage their caravans, eliminating the stress and complexity of renting.
- Maximize Bookings: Enhance visibility and attract potential renters through a well-designed and efficient marketplace.
- Secure Transactions: Ensure all transactions are secure and trustworthy, giving caravan owners peace of mind.
- Comprehensive Support: Offer tools and resources for owners to handle bookings, communicate with renters, and manage availability and pricing effortlessly.

##### Primary User Needs
- Customers need a simple way to find suitable caravans with clear, informative details about the caravan’s features, availability, and pricing. They also require a secure and user-friendly booking process to check availability, reserve caravans, and complete payments, as well as flexible cancellation and refund policies.
- Customers should be able to communicate with caravan owners to ask questions, discuss specific needs, and receive helpful information.
- Saving and sharing options are important for customers, allowing them to save favorite caravans for future trips or easily share details with friends and family.
- Caravan owners need an intuitive interface to create, edit, and manage their caravan listings. This includes the ability to upload multiple photos, write detailed descriptions, and update caravan availability and pricing effortlessly.
- Owners should have tools to manage bookings and transactions securely, ensuring payments are accurate and safely transferred.
- Effective communication tools are essential for owners to respond to customer questions, provide additional information, and reply to reviews to build trust with renters.
- Owners need the ability to review customer profiles to assess booking requests and approve or decline them, reducing the risk of disputes or other issues.
- All users require a seamless and reliable experience, including a clean and responsive interface that works across all devices, fast loading times, and minimal technical issues. They also need reliable identity verification, secure data handling, privacy protections, and access to responsive customer support for resolving issues, disputes, or refunds.

##### Business Goals
- Attract and retain a large base of both caravan owners and customers to establish a robust marketplace.
- Create a safe and secure platform for both customers and owners by ensuring reliable transactions, secure data handling, and trustworthy reviews.
- Make it easy for customers to book caravans and for owners to list and manage their rentals.
- Encourage users to engage with the platform frequently and provide positive feedback about their experience.

Future Goals:
- Generate revenue through booking fees, subscription plans, or commission-based models.
- Gradually expand the app's reach by targeting more geographic regions or user demographics.
- Automate and streamline business operations to minimize manual intervention and reduce costs.
- Collaborate with complementary businesses such as insurance providers, travel apps, or caravan servicing companies.
- Create a sense of community for users by providing forums, blogs, or events related to caravan travel.
- Continuously improve the platform based on user reviews, complaints, and behavior analytics.

#### 2. Scope Plane
##### Features
- A full list of [Features](#features) can be viewed in detail below.

##### Content Requirements
- Review message management (create, update, delete, and preview).
- Comment moderation and management tools.
- User account features (register, log in, edit/delete comments).
- Notification system for comment approval status.
- 404 error page for lost users.

#### 3. Structure Plane
##### Information Architecture
- **Navigation Menu**:
  - Links to Home/Dashboard, Login/Logout, Registration, Notification, Account, Contact, Caravan listing, Booking.
- **Hierarchy**:
  - Home / Landing page - when a user first arrives on the website will contain a simple navigation bar with links to login or register and a contact page. There will also be a overview of what the app does.
  - Login / Logout page - allow the user to log in to their account where they will then be redirected to their dashboard or if already logged in it will allow them to log out where they will be redirected to the home page.
  - Registration page - will allow a user to create an account whether they are a customer or a caravan owner, where they will be redirected to their dashboard.
  - Dashboard/Home page - serve as the hub for users after logging in, with personalised options based on their role and access to a extra navigation bar with links to account page, caravan listing page, booking page and notification page.
  - Caravan listing page - allow customers to browse and filter caravans based on their needs and allow owners to add, edit and remove their caravans from the listing page.
  - Booking page - customers to finalise caravan booking details and request the booking and for owners to review the request to approve or decline the bookings. 
  - Contact page - This will allow users to contact either admin for things such as technical problems or owners/customers about their bookings.
  - Account page - logged in users can edit their profiles, update preferences and change other personal details.
  - Notification page - logged in users can see all their messages easily and be able to preview and delete any of there messages.

##### User Flow
1. Home/Landing Page (Accessible to All Users)
- Visitors can:
  - View a brief overview of the app's purpose and functionality.
  - Navigate to sign-up, log-in and contact pages
2. User Registration and Login (Accessible to All Users)
- Guest users can:
  - Register for an account as a customer (to book caravans) or an owner (to list caravans).
  - Log in to access personalized features.
  - Reset passwords if needed.
3. Customer Workflow
- Registered customers can:
  - Search for caravans using filters (location, price, availability, features).
  - View caravan details, including descriptions, photos, and brief description of the owner.
  - Save favorite caravans to a wish list for future reference.
  - Send booking requests to caravan owners.
  - Track and manage booking.
  - Leave reviews and write comments for caravans they have stayed in.
4. Caravan Owner Workflow
- Registered owners can:
  - Create, update, and manage caravan listings with detailed descriptions, pricing, and availability.
  - Upload photos to attract potential customers.
  - Block specific dates when the caravan is unavailable.
  - View and respond to customer messages or booking requests.
  - Approve or decline booking requests.
  - Respond to reviews to build trust and improve their service.
5. Admin Workflow
- Admins can:
  - Approve or reject caravan listings to ensure quality and authenticity.
  - Monitor user activity and moderate reviews or comments to remove inappropriate content.
  - Handle disputes between customers and owners.
  - Analyze app usage statistics and generate reports for improvement.
6. Additional Features
- Notifications:
  - Customers receive booking confirmations and reminders.
  - Owners are notified of booking requests or customer messages.
- Secure payment processing for bookings with flexible refund and cancellation policies.
- Error Management
  - 404 error page is included with navigation links and automatic redirection.

#### 4. Skeleton Plane
##### Wireframe Ideas
- A full list of [Wireframes](#wireframes) can be viewed in detail below.

#### 5. Surface Plane
##### Visual Design Elements
- **[Colours](#colour-scheme)**: see below.
- **[Typography](#typography)**: see below.

### Colour Scheme

I used [coolors.co](https://coolors.co/2d2d2d-6a9e6f-f4a261-87ceeb-faf9f6) to generate my color palette.

- `#6A9E6F` primary colour.
- `#87CEEB` primary accent.
- `#F4A261` secondary accent.
- `#FAF9F6` background.
- `#2D2D2D` primary text.

![screenshot](documentation/colour.png)

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```
:root {
  /* p = primary | s = secondary | b = background */
  --p-colour: #6A9E6F;
  --p-accent: #87CEEB;
  --s-accent: #F4A261;
  --b-colour: #FAF9F6;
  --p-text: #2D2D2D;
}
```

### Typography

- [Montserrat](https://fonts.google.com/specimen/Merriweather) was used for all other secondary text.
- [Lato](https://fonts.google.com/specimen/Lato) was used for the primary headers and titles.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a caravan owner | I would like to create a listing for my caravan | so that I can rent it out to customers. |
| As a caravan owner | I would like to upload photos and provide details about my caravan | so that I can attract potential renters. |
| As a caravan owner | I would like to set the availability and pricing for my caravan | so that I can manage when it's rented and how much I earn. |
| As a caravan owner | I would like to approve or decline booking requests | so that I can ensure the caravan is available for trustworthy renters. |
| As a caravan owner | I would like to manage multiple caravan listings | so that I can rent out more than one vehicle. |
| As a caravan owner | I would like to receive notifications about new booking requests | so that I can respond promptly to customers. |
| As a caravan owner | I would like to block specific dates for personal use | so that my caravan is unavailable during those times. |
| As a caravan owner | I would like to respond to customers messages or questions | so that I can provide them with helpful information. |
| As a caravan owner | I would like to view and manage reviews left by customers | so that I can improve my service and attract more renters. |
| As a customer | I would like to filter caravans by location, price, and features | so that I can quickly find one that suits my needs. |
| As a customer | I would like to view detailed information about a caravan | so that I can see photos, amenities, and availability before making a decision. |
| As a customer | I would like to search for caravans near specific destinations | so that I can plan my travel conveniently. |
| As a customer | I would like to book a caravan for a specific date range | so that I can secure it for my trip. |
| As a customer | I would like to receive a confirmation email or notification for my booking | so that I have proof and details of my reservation. |
| As a customer | I would like to cancel or modify my booking | so that I can adjust my plans if necessary. |
| As a customer | I would like to save my favourite caravans to a wish-list | so that I can revisit them later when planning a trip. |
| As a customer | I would like to leave a review and rating for a caravan I rented | so that I can share my experience with others. |
| As a customer | I would like to create an account or log in | so that I can manage my bookings and preferences easily. |
| As a customer | I would like to chat with the caravan owner | so that I can ask specific questions about the rental. |
| As a admin | I would like to view all user accounts | so that I can monitor activity and handle issues if needed. |
| As a admin | I would like to approve or reject caravan listings | so that only high-quality and legitimate caravans are available on the platform. |
| As a admin | I would like to moderate reviews and comments | so that inappropriate content can be removed. |
| As a admin | I would like to analyse app usage statistics | so that I can identify areas for improvement. |
| As a admin | I would like to disable user accounts that violate the terms of service | so that the platform remains safe and trustworthy. |

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Moqups](https://app.moqups.com/dDQLGW13n29lu58kkqxLxu4EKujHh6qx/edit/page/ad64222d5) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframe/signup-mob.png) | ![screenshot](documentation/wireframe/signup-tab.png) | ![screenshot](documentation/wireframe/signup-desk.png) |
| Login | ![screenshot](documentation/wireframe/log-mob.png) | ![screenshot](documentation/wireframe/log-tab.png) | ![screenshot](documentation/wireframe/log-desk.png) |
| Home | ![screenshot](documentation/wireframe/home-mob.png) | ![screenshot](documentation/wireframe/home-tab.png) | ![screenshot](documentation/wireframe/home-desk.png) |
| Dashboard(customer) | ![screenshot](documentation/wireframe/custom-dash-mob.png) | ![screenshot](documentation/wireframe/custom-dash-tab.png) | ![screenshot](documentation/wireframe/custom-dash-desk.png) |
| Dashboard(owner)| ![screenshot](documentation/wireframe/own-dash-mob.png) | ![screenshot](documentation/wireframe/own-dash-tab.png) | ![screenshot](documentation/wireframe/own-dash-desk.png) |
| Listing(customer) | ![screenshot](documentation/wireframe/custom-list-mob.png) | ![screenshot](documentation/wireframe/custom-list-tab.png) | ![screenshot](documentation/wireframe/custom-list-desk.png) |
| Listing(owner) | ![screenshot](documentation/wireframe/own-list-mob.png) | ![screenshot](documentation/wireframe/own-list-tab.png) | ![screenshot](documentation/wireframe/own-list-desk.png) |
| Booking(customer) | ![screenshot](documentation/wireframe/custom-book-mob.png) | ![screenshot](documentation/wireframe/custom-book-tab.png) | ![screenshot](documentation/wireframe/custom-book-desk.png) |
| Booking(owner) | ![screenshot](documentation/wireframe/own-book-mob.png) | ![screenshot](documentation/wireframe/own-book-tab.png) | ![screenshot](documentation/wireframe/own-book-desk.png) |
| Contact | ![screenshot](documentation/wireframe/contact-mob.png) | ![screenshot](documentation/wireframe/contact-tab.png) | ![screenshot](documentation/wireframe/contact-desk.png) |
| Account | ![screenshot](documentation/wireframe/account-mob.png) | ![screenshot](documentation/wireframe/account-tab.png) | ![screenshot](documentation/wireframe/account-desk.png) |
| Notification | ![screenshot](documentation/wireframe/message-mob.png) | ![screenshot](documentation/wireframe/message-tab.png) | ![screenshot](documentation/wireframe/message-desk.png) |
| 404 | ![screenshot](documentation/wireframe/error-mob.png) | ![screenshot](documentation/wireframe/error-tab.png) | ![screenshot](documentation/wireframe/error-desk.png) |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Homepage | Allows all user to log in, sign up and gain a clear understanding of what the app's purpose and features are. | ![screenshot](documentation/feature) |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/feature) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/feature) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/feature) |
| Dashboard | The dashboard will display personalized sections tailored to either the customer or owner, along with image slideshows and links to their corresponding pages. | **customer:** ![screenshot](documentation/feature) **owner:** ![screenshot](documentation/feature) |
| Navigation | The app will feature two separate navigation bars: one for all users, including Home, Log In, Register, and Contact tabs, and another for signed-in users, featuring Account, Listings, Bookings, and Notifications tabs. Both navigation bars can be toggled on and off as needed. | **all users:** ![screenshot](documentation/feature) **signed in users:** ![screenshot](documentation/feature) |
| Pagination | Caravan listings are displayed with six caravans per page, ensuring easy navigation for customers browsing the options. | ![screenshot](documentation/feature) |
| Next arrow | On the listing page, users can browse through the image gallery to view caravans in greater detail. | ![screenshot](documentation/feature) |
| Contact form | All users can use this feature to contact the admin, while customers can reach out to owners and vice versa. | ![screenshot](documentation/feature) |
| Search bar | The search bar allows users to find a specific caravan by its ID on the listing page, or on the dashboard, it can be used to search for actions such as contacting an owner or booking a caravan stay. | **dashboard:** ![screenshot](documentation/feature) **listing page:** ![screenshot](documentation/feature) |
| Filter | Users can filter caravan searches based on their needs, for example, customers can search for caravans with free Wi-Fi, or owners can locate their caravans by a specific location. | ![screenshot](documentation/feature) |
| Account dropdowns | Logged-in users can access dropdown tabs to view detailed information on each topic, as well as edit or delete content as needed. | ![screenshot](documentation/feature) |
| Add caravans | Caravan owners can add new caravans to the listing page, including uploading images and providing detailed information about each caravan. | ![screenshot](documentation/feature) |
| Update caravan details | Caravan owners can update/manage their caravan details from their booking page. | ![screenshot](documentation/feature) |
| Delete caravans | Caravan owners can delete any of their caravans from their booking page. | ![screenshot](documentation/feature) |
| Booking button | Customers can click the 'Book Now' button to navigate to the booking page, where they can reserve their selected caravan. | ![screenshot](documentation/feature) |
| booking form | Customers can complete a form with their personal details, desired dates for their stay, and any additional information or questions for the owner. The owner can review the booking request, provide additional details or ask questions, and choose to accept or decline the request. | **customer form:** ![screenshot](documentation/feature) **owner form:** ![screenshot](documentation/feature) |
| User Feedback | Clear and obvious Django messages are used to provide feedback to user actions. | ![screenshot](documentation/feature) |
| Caravan reviews | Customers can leave reviews and ratings for their previous stays, while owners can respond to reviews to build stronger relationships with customers and attract more potential renters. | **customer review:** ![screenshot](documentation/feature) **owner review:** ![screenshot](documentation/feature) |
| Social media links | The footer section includes links to various social media platforms. | ![screenshot](documentation/feature) |
| Wish-list | Customers can save caravans to a wish list, allowing them to revisit their favorite options later. | ![screenshot](documentation/feature) |
| Notifications | Customers and owners can receive both email and in-app notifications based on their preferences for events like booking requests, reviews, and admin messages. In-app notifications can be deleted manually on the notifications page or automatically after a set period, depending on user preferences. | **email:** ![screenshot](documentation/feature) **in-app:** ![screenshot](documentation/feature) |
| Heroku Deployment | The site is fully deployed to Heroku, making it accessible online and easy to manage. | ![screenshot](documentation/feature) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/feature) |
# Needs adding
| admin features |  | ![screenshot](documentation/feature) |

### Future Features

- **Maps or GPS directions**: Allow users to locate the caravan stay easily.
- **Add more filters**: Add other topics e.g. pet friendly.
- **Add payment method**: Implement a payment gateway, for example PayPal, then install its SDK and add all the required models, views and front-end code.
- **Curated travel itineraries**: Add a section for owners to add travel plans customers can have when they arrive at their destination.
- **Pricing**: Allow owners to set pricing for different days, for example, weekends, weekdays, or holidays.
- **Earning tracker**: Update database models, add a method to calculate the owner's net earnings and add a model for the earnings, and add front-end code so the owner can view it.
- **Add-ons**: Allow the caravan owner to offer add-ons such as camping gear or a BBQ.
- **Manage refunds**: Allow the admin to manage refund requests for cancellations.
- **Notifications**: Allow the admin to send notifications or emails to users about any updates, promotions, or issues.
- **Reports**: Allow the admin to create reports of earnings and transactions so the app's financial performance can be tracked.
- **Fraudulent accounts**: Allow admin to detect any suspicious bookings, to protect their users and the platform.
- **Admin Analytics**: Provide site admins with an integrated location-based analytic so they can see popular destinations and caravans.
- **Custom Themes for Users**: Allow users to customize the visual theme of the site (colors, fonts, etc.) to suit their preferences.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) | Cloud-based IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Jest-grey?logo=jest&logoColor=c21325)](https://jestjs.io) | Automated JavaScript testing. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
⚠️ potential remove ⚠️
| [![badge](https://img.shields.io/badge/Google_Maps_API-grey?logo=googlemaps&logoColor=4285F4)](https://developers.google.com/maps) | Interactive map on my site. |
⚠️ end ⚠️
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |

⚠️ NOTE ⚠️

Want to add more?

- Tutorial: https://shields.io/badges/static-badge
- Icons/Logos: https://simpleicons.org
  - FYI: not all logos are available to use

🛑 --- END --- 🛑

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

<details>
<summary>Click here to see my ERD's</summary>

![screenshot](documentation/erd/book-erd.png)

![screenshot](documentation/erd/caravan-erd.png)

![screenshot](documentation/erd/message-erd.png)

![screenshot](documentation/erd/note-erd.png)

![screenshot](documentation/erd/review-erd.png)

![screenshot](documentation/erd/user-erd.png)

![screenshot](documentation/erd/wish-erd.png)

</details>

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    USER {
        INTEGER ID PK
        STRING Name
        STRING Email
        STRING Password
        ENUM Role
        DATETIME Created_at
        DATETIME Updated_at
    }

    CARAVAN {
        INTEGER ID PK
        INTEGER Owner_ID FK
        STRING Name
        STRING Location
        FLOAT Price
        TEXT Description
        DATETIME Created_at
    }

    BOOKING {
        INTEGER ID PK
        INTEGER User_ID FK
        INTEGER Caravan_ID FK
        DATE Start_date
        DATE End_date
        ENUM Status
    }

    REVIEW {
        INTEGER ID PK
        INTEGER User_ID FK
        INTEGER Caravan_ID FK
        INTEGER Rating
        TEXT Comment
    }

    NOTIFICATION {
        INTEGER ID PK
        INTEGER User_ID FK
        TEXT Message
        BOOLEAN Read
        DATETIME Created_at
    }

    WISH_LIST {
        INTEGER ID PK
        INTEGER User_ID FK
        INTEGER Caravan_ID FK
    }

    MESSAGE {
        INTEGER ID PK
        INTEGER Sender_ID FK
        INTEGER Receiver_ID FK
        TEXT Content
        DATETIME Created_at
    }

    %% Relationships
    USER ||--o{ CARAVAN : "owns"
    USER ||--o{ BOOKING : "makes"
    CARAVAN ||--o{ BOOKING : "is booked in"
    USER ||--o{ REVIEW : "leaves"
    CARAVAN ||--o{ REVIEW : "receives"
    USER ||--o{ NOTIFICATION : "receives"
    USER ||--o{ WISH_LIST : "creates"
    CARAVAN ||--o{ WISH_LIST : "is saved in"
    USER ||--o{ MESSAGE : "sends/receives"

```

source: [Mermaid](https://mermaid.live/edit#pako:eNq1VV1v2jAU_SuWpb7RbaiwibxlwbCokKAktFUVCXmJBxGJjWwD6yj_fXZoQghEo5qaJ-ee4_tx7rW9gxGLCTQg4f0EzznOQgrUN_WRB3aHtf5sJ0BDZbL7YHJ_NPuBZztD4OCMnBlRhpP0zDrBQmwZj48AcqZj4LG04qFvBiiwxwhYnGBJ4hmWF8DpKj4B9yE9LCzTMx9M54r8C7O7pYTPFDi4srgRi7BMGD0Cg5FrBmDCk6jCDtBTAPpERDxZndIbSyyr-O669zrU9VVMxXkRBWZhjjeY1mGdBvAl5nKmxawBiMY1c94sxZdrUUvXQw82evzYbAvYU9rTeU1mi2UZoXUVHTewB7ZlBrbr_GdyeZQxEQLPK4qoNo2QGjaP4Pg97X20_R-zke0HHydZGWuMfN8condE8gmNm2N5JCLJpkEhi1FZ9uE6LW5ulMs0P1BikaxE5Q56fb29ZbvySBsghGxLRQjPOcWB0ZwML0lJKjZf4CUC_GRsSWKQ0Es-36ZaU1OCN40-Kzx-EOdiiifT-C_ycUI0M8rFa4p_ylVVCZVsU1HFOGiqUI0Wn6tpwBbMCFeXd6yehXxiQigXRF2CUG-IMV9q2l7x8Foy_4VG0JB8TVqQs_V8AY1fOBXqb53fz2_PSmldYQqNHfwNje7dp1671-t27rpfO9_anXYLvkDjy74F_zCmNrRz8nO-1v73fwEnVdjV)

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/advanced-erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/AshLaw96/Nomad-Nation/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/AshLaw96/Nomad-Nation/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/AshLaw96/Nomad-Nation)](https://www.github.com/AshLaw96/Nomad-Nation/issues) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/AshLaw96/Nomad-Nation)](https://www.github.com/AshLaw96/Nomad-Nation/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCow" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://nomad-nation-23b17dd0a6b5.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

⚠️ DO NOT update the environment variables to your own! These should never be public; only use the demo values below! ⚠️

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user-inserts-own-cloudinary-url |
| `DATABASE_URL` | user-inserts-own-postgres-database-url |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | any-random-secret-key |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```

### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/AshLaw96/Nomad-Nation).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/AshLaw96/Nomad-Nation.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/AshLaw96/Nomad-Nation)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/AshLaw96/Nomad-Nation).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

⚠️ --- Notes ---⚠️

- Images
    - [Pexels](https://www.pexels.com)
    - [Unsplash](https://unsplash.com)
    - [Pixabay](https://pixabay.com)
    - [Lorem Picsum](https://picsum.photos) (placeholder images)
    - [Wallhere](https://wallhere.com) (wallpaper / backgrounds)
    - [This Person Does Not Exist](https://thispersondoesnotexist.com) (reload to get a new person)
- Audio
    - [Audio Micro](https://www.audiomicro.com/free-sound-effects)
- Video
    - [Videvo](https://www.videvo.net)
- Image Compression
    - [TinyPNG](https://tinypng.com) (for images <5MB)
    - [CompressPNG](https://compresspng.com) (for images >5MB)

⚠️ --- END ---⚠️

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pexels](https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg) | Hero image |
| [Wallhere](https://c.wallhere.com/images/9c/c8/da4b4009f070c8e1dfee43d25f99-2318808.jpg!d) | Background wallpaper |
| [Pixabay](https://cdn.pixabay.com/photo/2017/09/04/16/58/passport-2714675_1280.jpg) | Background wallpaper |
| [DALL-E 3](https://openai.com/index/dall-e-3) | AI generated artwork |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my partner, [Megan Lawrence](linkedin.com/in/megan-lawrence-27431119b) for believing in me, and allowing me to make this transition into software development.