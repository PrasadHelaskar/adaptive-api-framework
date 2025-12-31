#!/bin/bash

CURRENT_DIR="/mnt/k/adaptive-api-framework/codebase"

case ":$PYTHONPATH:" in
  *":$CURRENT_DIR:"*)
    echo "PYTHONPATH already contains $CURRENT_DIR"
    ;;
  *)
    export PYTHONPATH="$PYTHONPATH:$CURRENT_DIR"
    echo "Added $CURRENT_DIR to PYTHONPATH"
    ;;
esac

echo "Current PYTHONPATH:"
echo "$PYTHONPATH"
