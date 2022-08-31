## KDEConnect Ping All (Devices)

### Why?

This is a simple KDE Connect CLI wrapper that automatically pings any available devices with an optional message. 
By default, the kdeconnect-cli does not send messages to all connected devices when using the ping or pingmsg flags.
While this could and probably should be patched into the kdeconnect-cli, I decided to make my own wrapper for immediate use.

### Installation

Running the following command should install the script to your system's path. 

```
python3 -m pip install .
```


### Example Use

A simple use case for this script is wanting to be notified when building a large code base has finished or are otherwise running a command in 
the terminal that will take a significant period of time. 

For example,

```
cmake ../src && make install -j4; kdeconnect-pingall -m "Compile finished."
```

This will compile your project while you take your phone with you to make a coffee or otherwise live your life
for a brief intermission. You might even want to step over to another machine in another room to do some
other task. Regardless of the purpose, as long as you have another device with you that a paired to one
another via the lovely KDE Connect application, you will eventually be notified that your machine is once
again idle.

### Future Possibilities

- [ ] It might be nice to make this script act as a wrapper for your intended command chain. This way, you could
actually make unique notification messages for success or failure (exit 0 vs exit > 0 messages.)
- [ ] Sound playback might also be nice on the local device for non kdeconnect based usage (for example, reading
a book or playing a musical instrument.)


