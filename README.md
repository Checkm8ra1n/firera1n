# firera1n

## DISCLAIMER

This is a fork of icera1n, so most of the credits are to the original developer. I just want to reimplement in python his project

Compatible OS:

- macOS (Tested on 15.5 Sequoia)
- Linux (Not tested)
- Windows (Tested on 11)

## DEPENDENCIES (Linux):
usbmuxd libimobiledevice unzip git libimobiledevice-utils

## DEPENDENCIES (Windows):
libimobiledevice usbmuxd libimobiledevice-utils

## Install Steps:

<code> git clone https://github.com/Checkm8ra1n/firera1n --recursive </code>

## To run:

<code> cd </code> into the directory where firera1n is installed

then run <code>python3 firera1n.py</code>

## Check out [Getting Started](https://github.com/Checkm8ra1n/firera1n/blob/main/Guides/getstarted.md)

Note: Apple silicon might not work as expected
Note: USB-C to Lightning cables are kinda wonky so don't use them

## What is firera1n?

Firera1n a fork of icera1n, rewritten in Python with also with Windows binaries compiled with mingw64

## What can it do for you?

It can help you jailbreak, down / upgrade using futurerestore, and backup and restore activation files from your iDevice.

## Backing up and restoring activation files? What's that for ???

Backing up and restoring activation files is necessary when you downgrade a device using iOS 16 / 17 SEP or in simple terms when you downgrade a device which supports iOS 16 / 17 to iOS 15. If you don't backup and restore your activation files you will be stuck in setup after you finish the restore.

## What about Windows?

The windows addition for futurestore it's a my idea, in fact I put the Windows binaries of futurestore and gaster as for Linux/macOS, also you have to install the drivers, so see [here](Guides/Windows%20Drivers.md)

# Want more features?

Go to original icera1n repo and ask to developer for new feature, no spamming of course

## Future features?

I'm planning to making a GUI, for macOS in SwiftUI, I think I'll call it Icera1n-GUI
I'm planning also to add Turdus Merula section, an A10(X)/A9(X) downgrader