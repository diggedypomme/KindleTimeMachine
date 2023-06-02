#!/bin/sh

# Pre-section
echo "pre:"

# Find the PIDs of processes running "mayclock.sh"
pids=$(pgrep -f mayclock.sh)
echo "$pids"

# Kill the processes
echo "Killing the processes..."
for pid in $pids; do
  kill "$pid"
done

# Post-section
echo "post:"

# Find the PIDs of processes running "mayclock.sh" again
pgrep -f mayclock.sh
