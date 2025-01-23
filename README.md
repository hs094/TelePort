# TCCS - TelePort
TelePort is a Online Delivery Management Software where a customer can send,receive and track orders in a single place. The Software computerizes any delivery company’s book keeping activities associated with its operation with an efficient Truck Allotement and Dispatch Algorithm to ensure productivity resources available.

<div style="margin: 10px 0;" align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" style="margin-right: 10px"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" style="margin-right: 10px"/>
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" style="margin-right: 10px"/>
  <img src="https://img.shields.io/badge/SQLAlchemy-CA4245?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" style="margin-right: 10px"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Bcrypt-2A2A2A?style=for-the-badge&logo=lock&logoColor=white" alt="Bcrypt" style="margin-right: 10px"/>
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" alt="Render"/>
</div>

## Visit the Site
The Webiste is Hosted on Render, you can view the website by clicking [here](https://teleport-g0vz.onrender.com/) 

## Remote Usage
To remotely use the codebase to host the website on your system, clone the repository on your system and do the Following Steps -

1.  Create a `.env` file according to the instructions:
```yaml
host=<host-of-psql-server>
port=<port-of-psql-server>
database=<psql-db-name>
secret_key=<secret-key-for-bcrypt>
user=<psql-db-user>
pool_mode=<psql-pool-mode>
password=<psql-password>

```
2.  Execute the Following line in the root folder to install all the requirements
```bash
pip install -r requirements.txt
```
3.  To Finally Run the Codebase, in the root directory, run the following command in the terminal
```python
python app.py
```

## Project Structure
```
teleport/
├── app.py                     # Main Flask application
├── forms.py                   # Form definitions
├── models.py                  # Database models
├── requirements.txt           # Project dependencies
├── routes.py                  # Application routes
├── .env                       # Environment variables
│
├── migrations/                # Database migrations
│   ├── versions/
│   ├── alembic.ini
│   ├── env.py
│   └── script.py.mako
│
├── static/
│   ├── images/                # Image assets
│   └── styles/
│       ├── about.css
│       └── login.css
│
└── templates/                 # HTML templates
    ├── base.html              # Base template
    ├── index.html         
    ├── login/             
    │   ├── login.html
    │   └── signup.html
    ├── customer/
    │   └── dashboard.html
    ├── employee/
    │   └── dashboard.html
    └── manager/
        └── dashboard.html
```

## Application Screenshots

<table>
  <tr>
    <td align="center">
      <img src="./ScreenShots/HomePage.PNG" width="600px"/><br/>
      <b>Home Page</b> - Landing page with login options
    </td>
    <td align="center">
      <img src="./ScreenShots/ManagerDashBoard.PNG" width="600px"/><br/>
      <b>Manager Dashboard</b> - Overview of operations
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="./ScreenShots/BranchStatistics.PNG" width="600px"/><br/>
      <b>Branch Statistics</b> - Performance metrics by location
    </td>
    <td align="center">
      <img src="./ScreenShots/CustomerDashboard.PNG" width="600px"/><br/>
      <b>Customer Dashboard</b> - Order management interface
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="./ScreenShots/TruckIdleStatistics.PNG" width="600px"/><br/>
      <b>Truck Idle Statistics</b> - Fleet utilization analysis
    </td>
    <td align="center">
      <img src="./ScreenShots/CustomerOrderHistory.PNG" width="600px"/><br/>
      <b>Customer Order History</b> - Past orders and tracking
    </td>
  </tr>
</table>
