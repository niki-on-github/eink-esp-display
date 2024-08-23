This is the firmware code for https://harrystern.net/halldisplay.html

This directory contains esp-idf/esp-rs based firmware to download an image over wifi and display it on a waveshare e-ink display.

# Building

You must create a `src/config.rs` file containing your Wifi connection credentials and the location of the file to download and display.

Sample file:

```
use super::WifiConfig;

// APN must support WPA3
pub const WIFI_CONFIG_DATA: WifiConfig = WifiConfig {
    ssid: "your_ssid",
    psk: "your_psk",
};

pub const IMAGE_DATA_URL: &str = "https://example.com/data_file.img";
```

Then you can run `just build` to build assuming you have the rest of your environment set up as in the [embedded rust book](https://docs.rust-embedded.org/book/intro/install.html).

If you have an esp device plugged in over usb, you should be able to use `just run` to upload your code to the device. This is configured in `.cargo/config.toml` in the current directory.

## Build Setup

Create VM:

```sh
quickget ubuntu 24.04
echo "disk_size=\"60G\"" >> ubuntu-24.04.conf
lsusb # get usb id XXXX:XXXX of esp32
echo "usb_devices=(\"XXXX:XXXX\")" >> ubuntu-24.04.conf
quickemu --vm ubuntu-24.04.conf
```

Install Ubuntu, then setup toolchain:

```sh
sudo apt update
sudo apt install -y libudev-dev python3-virtualenv python3-pip gcc build-essential curl pkg-config git
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup toolchain install stable
cargo install espup
espup install
. $HOME/export.esp.sh
cargo install ldproxy
cargo install espflash
sudo usermod -a -G dialout $USER
reboot
```
