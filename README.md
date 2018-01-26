# Introduction

This repo contains the code needed to expose the [SOMA Smart Shade](https://uk.somasmarthome.com) device over HTTP.
The APIs have been designed to work well with this [Homebridge/Homekit plugin](https://github.com/paolotremadio/homebridge-minimal-http-blinds).

---

# Items needed to make it work

* 1x iOS 10+ device running [Apple's Home App](http://www.apple.com/uk/ios/home/)
* 1x Roller Blind with continuous loop cord (no junction)
* 1x SOMA Smart Shade
* 1x Raspberry Pi 3 Model B

---

# Mount your Smart Shade.

<img src="images/smartshadebig.png">

Install and setup your Smart Shade into your desired location as normal using the [Smart Shades](https://itunes.apple.com/us/app/smart-shades/id1016406862?mt=8) app, a guide for doing this can be found here: https://youtu.be/9DTAcZiiFYU

---

# Configuration.

#### Copy the files to the Raspberry Pi.

* Download this repo and put it under `/home/pi/webshades/`

#### Find the Bluetooth MAC address of the Smart Shade.

You need to find the Bluetooth MAC address of the SOMA Smart Shade so your Raspberry Pi can communicate with it.

  * Enable your Bluetooth adaptor on the Raspberry Pi using the command:

        sudo hciconfig hci0 up

  * Now scan for your Smart Shade (it will normally be identified with the name RISExxx) using the command:

        sudo hcitool lescan

  * Make a note of the Smart Shades MAC address.


#### Run the APIs

Run the `webshades.py` script. 

#### Check if it works

Open `http://<YOUR RASPBERRY PI IP ADDRESS>:8080/getbattery/<YOUR SOMA MAC ADDRESS>` (E.g. http://192.168.1.2:8080/getbattery/F6:AA:BB:CC:DD:EE)

You should get a response with a number from 1 to 100 (where 100 is a battery fully charged).

---

# Finish

Now that everything is installed and configured, your SOMA smarth shade is available over HTTP.

Install this [Homebridge plugin](https://github.com/paolotremadio/homebridge-minimal-http-blinds) by running:

`npm install -g https://github.com/paolotremadio/homebridge-minimal-http-blinds`

Configure Homebridge accordingly. Here's an example:

````json
{
    "accessories": [
        {
            "name": "Kitchen Blinds",
            "accessory": "MinimalisticHttpBlinds",
  
            "get_current_position_url": "http://192.168.1.2:8080/getposition/F6:AA:BB:CC:DD:EE",
            "set_target_position_url": "http://192.168.1.2:8080/setposition/F6:AA:BB:CC:DD:EE/%position%",
            "set_target_position_method": "GET",
            "get_current_position_polling_millis": "300000"
        }
    ]
}
````
 
---

# Credits
Based on the Python control script from [jeremynoel476](https://bitbucket.org/jeremynoel476/smartblinds-diy)
and the ["official" python integration instrucitons](http://www.instructables.com/id/Connect-Soma-Smart-Shades-From-Web-With-Raspberry-/)

