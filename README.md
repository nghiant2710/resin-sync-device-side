## Resin Sync Base Image
This base image allows you to sync a folder on your host machine to a resin.io device.

To get started, first install the resin CLI
```
sudo npm install -g resin-cli
```
then go and clone the [resin-plugin-watch](https://github.com/shaunmulligan/resin-plugin-watch)
```
git clone https://github.com/shaunmulligan/resin-plugin-watch
```
next we need this plugin available to the resin cli, so we need to `npm link` it.
```
cd resin-plugin-watch && npm link
```
Now when you run `resin help` you should see the `watch` plugin listed at the bottom of the list of commands.

Next we need to push this repo (i.e resin-sync-device-side) to our device. We also need to set up an environment variable on the dashboard:
`TOKEN` = `<your_resin_token>`
You can get this Token from your preferences page.

You will also need to enable the resin device URL, this can be done from the Actions page on the device dashboard.

Once the device has pulled the code you can just change directory to `src` and sync it to your device like this:
```
cd /src
resin watch <RESIN_DEVICE_UUID>
```
replacing <RESIN_DEVICE_UUID> with the UUID of your resin.io device.

Now any time you save any of the python files in the `/src` directory they will automatically be synced to the device and the container will be restarted. It should only take about 20 seconds to have the new code running.

Obviously if you need to install any dependencies or pip install stuff, you will need to add them to the Dockerfile or requirements.txt file.

Another nice side affect of this base image is that you can ssh into the container using:
```
ssh root@<MY_DEVICE_IP> -p80
```
and the passphrase is `resin`
