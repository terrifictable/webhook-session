<p class="infos" align="center">
  <img src="https://img.shields.io/github/contributors/TerrificTable/Roblox-Account-Gen.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/github/forks/TerrificTable/Roblox-Account-Gen.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/github/stars/TerrificTable/Roblox-Account-Gen.svg?style=for-the-badge"/>
  <img src="https://img.shields.io/github/issues/TerrificTable/Roblox-Account-Gen.svg?style=for-the-badge"/>
  <!-- <img src="https://img.shields.io/github/license/TerrificTable/Roblox-Account-Gen.svg?style=for-the-badge"/> -->
</p>

<div align="center">
  <h1>Webhook-Session</h>
  <h3>The "Discord-Webhook-Session" function out of my webhook tools just a bit more useless code and a bit simpler to use
  <br><br>
    
<div align="center">
  <h1>Instructions</h>
  <h3>to make it work at all, install requests (python -m pip install requests)<br><br>
  <h3><details align="center">
    <summary>If you have one webhook</summary>
    <h5>Replace the line with "YOUR FIRST WEBHOOK HERE" inside the b-config.json file with your webhook<br>
      Your b-config.json file should look something like that: <br><div align="left"><pre><code>{
  "webhooks": [
    "https://discord.com/api/webhooks/913484234486870087/51RgnJT0HshyJc5WopMQALbiHdZ87GyOrtGXxhpKyfyJvune1sMywXXM6oOjFnd0LO_C"
  ]
}</code></pre></div><br>
      Now run the dc-webhook-session.py file it will automaticaly select the first webhook and start the session
  </details>
  <h3><details>
    <summary>If you have 2 or more webhooks</summary>
    <h5>Put each webhook inside one line (just replace the first and second filled out line), <br>BUT the webhook has to be in quotation marks ("). <br>For each webhook add a "," at the end of the last line and do the same thing as in the firstline<br><h2>!!! Watch out the last line with your webhook has to have no "," at the end or it will not work<br>
      <h5>Your b-config.json file should look something like that: <br><div align="left"><pre><code>{
  "webhooks": [
    "https://discord.com/api/webhooks/913484234486870087/51RgnJT0HshyJc5WopMQALbiHdZ87GyOrtGXxhpKyfyJvune1sMywXXM6oOjFnd0LO_C",
    "https://discord.com/api/webhooks/925827238274949220/nr7QoFFyu92zzTRdyo6gs7t4G5PsbBoAKa4-b-UKjRxvkKYXvpyFl1R_sdpn35aq9hKJ"
  ]
}</code></pre></div> (depending on how many webhooks you have)
      Now if you run the dc-webhook-session.py file you will be able to choose which webhook you want to use to open a new session<br>
  </details>
  <br><br>
