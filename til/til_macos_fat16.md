Format USB Stick as FAT16 From Mac OS X
=======================================

**Warning:** This will destroy data. Ensure that you have a backup and that you target the correct disk(s).

1. Find drive to format with `mount`, if filesystem mounted.
1. Unmount target filesystem with `diskutil unmountDisk disk7` (whichever disk).
1. Format target disk: `sudo newfs_msdos -F 16 -v NAME /dev/disk7` (whichever disk).
1. Mount filesystem: `diskutil mount /dev/disk7`.
