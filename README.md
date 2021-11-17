# Components
####  1. Software
    1. JS(Fetching data from Firebase cloud and controlling the webpages)
    2. HTML & CSS(Design of webpages for showing the smart parking system)
    3. Python(data collection from sensors and dumping on the cloud)
        a. Pyrebase library for firebase supported by python3

####  2. Hardware
    1. HR-S04 Ultrasonic Sensors(Quantity:3)
                                TRIG    ECHO
        Pin used for Sensor1:    14     15
        Pin used for Sensor2:    20     21
        Pin used for Sensor3:    02     03
    2.Raspberry Pi Model 3 B+

####  3. Cloud
      Firebase Realtime Cloud Services used: Two Configuration were used for webpage and pi.
      Parameters for the config can be obtained from firebase.
      config={
      "apiKey": ,
      "authDomain":,
      "databaseURL": ,
      "projectId": ,
      "storageBucket": ,
      "messagingSenderId": ,
      "appId": ,
      "measurementId": 
    };
    JS Libraries used for firebase are:
    <script src="https://www.gstatic.com/firebasejs/7.20.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/7.20.0/firebase-auth.js"></script>
    <script src="https://www.gstatic.com/firebasejs/7.20.0/firebase-database.js"></script>
    > version(7.20.0)
    > Replace the version by checking with the firebase.
    
