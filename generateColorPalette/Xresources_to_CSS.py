#!/usr/bin/env python3

import sys

color_map = { 'color0': 'black',
              'color8': 'lblack',
              'color1': 'red',
              'color9': 'lred',
              'color2': 'green',
              'color10': 'lgreen',
              'color3': 'yellow',
              'color11': 'lyellow',
              'color4': 'blue',
              'color12': 'lblue',
              'color5': 'magenta',
              'color13': 'lmagenta',
              'color6': 'cyan',
              'color14': 'lcyan',
              'color7': 'white',
              'color15': 'lwhite',
              'foreground': 'fg',
              'background': 'bg',
              'cursorColor': 'cursor',
              }

lookup = {}

for line in open(sys.argv[1]):
  if line.startswith("!"): continue
  if line.startswith("*."):
    sp = line.strip().split(":")
    label = color_map[sp[0][2:].strip()]
    color = sp[1].strip()
    lookup[label] = color

print(":root {")

for key in lookup:
  print('  --color-%s: %s;' % (key, lookup[key]))

print("}")
