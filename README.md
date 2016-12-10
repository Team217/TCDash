Thunderchickens have a custom Dashboard? Apparently...

After a solid two days of work we have started developing our very own custom dashboard.Written in Python the dashboard uses Kivy for all things GUI and pynetworktables to transfer data to the robot.Also incuded is robotTable a program that simulates a robot feeding/reading values so you don't even need a robot to test this out. Simply set the ip of the network table as <127.0.0.1> and you are set, for competitions use the static ip of the rio at <10.xx.xx.2> .

Currently we have a working auton selector and a working read of the hood,arm,cogx, and cogy. The rest of the sensors will be put in shortly but are basically mirrors of the habove. Also we need to beautify it to make it easily readable.
