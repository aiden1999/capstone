#!/bin/bash
echo "Installing requirements"
pip install -r requirements.txt
echo "Installing scripts"
pip install -e .
