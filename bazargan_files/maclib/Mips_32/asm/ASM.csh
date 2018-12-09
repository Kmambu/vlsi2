#!/bin/csh

  echo "=== $1 ==="
  $HOME/bin/asm -set noreorder -s $1.sym -ld mips32_ld -mips32 -o $1.mem $1.r $1.u $1.x
