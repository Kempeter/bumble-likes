<!-- PROJECT LOGO -->
<h3 align="center">Bumble Likes Viewer</h3>

  <p align="center">
    A little python program to see, who liked you on Bumble
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I used Bumble for a while and became curious about who liked me. I discovered Bumble Web and realized I could access the right data.


<!-- GETTING STARTED -->
## Getting Started

You need only Python and Requests to use this project<br>
And a Bumble account :)

## Installation 
1. Download the source code
```sh
git clone https://github.com/Kempeter/bumble-likes.git
```
2. Install the required libraries
```sh
pip install -r requirements.txt
```



<!-- USAGE EXAMPLES -->
## Usage
1.  First of all, you have to create a Bumble account
2.  Login on a browser like Chrome, Firefox, Opera etc.
3.  Open the developer tools
  * Chrome ```Ctrl + Shift + C```
  * Firefox ```Ctrl + Shift + I```
  * Opera ```Ctrl + Shift + H```
4. Go to the network tab
5. Enter ```encounters``` to the search bar. You need the ```mwebapi.phtml?SERVER_GET_ENCOUNTERS``` <br><br> <img src="project_images/network1.png" style="margin-left:40px">
6. Copy the response and paste it to ```encounters.json```

