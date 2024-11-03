# Plugin installation
As mentioned in the README, GFMS2 has built in support for plugins. These plugins are simply Python scripts that are contained in folders. These can all be found in the resources path.

This is an alpha WIP, so the definite architecture of the plugin system is still undecided. Thus there may be changes to the specification of plugins.

## Installing plugins
To install plugins, you will have to add a file containing the plugin to the resources path. Then, you will have to add the name of the plugin to a resources config file (Plugins), with each newline serving as an indicator for a new plugin. Whatever configuration that the plugin supports will be accessed through the plugin file.

## Default/Recommended plugins
Although it is possible to use GFMS2 without plugins, there will be many features missing. Most of the features in GFMS2 will be implemented as plugins, so there will be a curated list for the recommended plugins.

